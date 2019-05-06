from pycorenlp import StanfordCoreNLP
import sys
import re 

nlp = StanfordCoreNLP('http://localhost:9000')
#handle the invalid characters in input data
text = re.sub('[^a-zA-Z0-9 \n\.]','',sys.argv[1])
res = nlp.annotate(text,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
for s in res["sentences"]:
    print("'%s', %s , %s" % (
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"],s["sentiment"]))
