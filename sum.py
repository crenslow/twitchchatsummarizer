from summarizer import Summarizer
import sys



file = open('newrfd.txt', "r")
filedata = file.readlines()
#print(len(filedata[0]))


body = filedata[0]
text = body[0:999999]

model = Summarizer()
sents = sys.argv[1]
summary = model(text, num_sentences= int(sents))
#debug = model.run_embeddings(body, num_sentences= int(sents))

print(summary[0:int(len(summary)/2)] + "\n")
print(summary[int(len(summary)/2): len(summary)] + "\n")
print("Words in input: " + str(len(text)))
print("Words in summary: " + str(len(summary)))
print("Reduced to ~" +sents+ " sentences")

