from rake_nltk import Rake
import nltk

nltk.download('stopwords')
nltk.download('punkt')

rake = Rake()

file_text = open("text.txt","r")

text = file_text.read()

rake.extract_keywords_from_text(text)
kws = rake.get_ranked_phrases()

ans_file = open("ans.txt","r")
ans = ans_file.read()

for i in kws:
    if (" " in i):
        kws.remove(i)
        i = i.split(' ')
        for x in i:
            kws.append(x)

print(kws)

marks = 0

for i in kws:
    if(i in ans):
        marks += 1
        print(i)

score = (marks/5)
print(marks)
print(score)
