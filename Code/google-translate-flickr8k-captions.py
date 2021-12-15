import json
import sys
import six
import csv
from google.cloud import translate_v2 as translate
translate_client = translate.Client()

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    #print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"]

fin = open("/Users/sayalighodekar/DLCV_project/flickr8k_images/captions.txt","r")
fout = open("/Users/sayalighodekar/DLCV_project/flickr8k_images/hindi_captions.txt","w")

nreader = csv.reader(fin, delimiter=",")
nwriter = csv.writer(fout, delimiter=",")
next(nreader, None)

from tqdm import tqdm
for row in tqdm(nreader):
    try:
        nwriter.writerow([row[0],translate_text(target="hi",text=row[1])])

    except Exception as e:
        print(e)
        
fout.close()


#translate_text("hi","Hello!")
# fin = json.load(open("cocoapi/annotations/captions_train2014.json","r"))
# annotations  = fin['annotations']
# #annotations = annotations[:10]

# new_annotations = []
# from tqdm import tqdm

# for a in tqdm(annotations):
#     try:
#         hindi_caption = translate_text(target="hi",text=a['caption'])
#         a['hindi_caption'] = hindi_caption
#         new_annotations.append(a)
#     except:
#         print("Google translation API error")
#         break
    
    
# fout = open("cocoapi/annotations/hindi_captions_train2014.json","w",encoding="utf-8")
# data = [{'info':fin['info'],'images':fin['images'],'licenses':fin['licenses'],'annotations':new_annotations}]
# #data = [{'info':fin['info'],'licenses':fin['licenses'],'annotations':new_annotations}]
# json.dump(data, fout,ensure_ascii=False)
