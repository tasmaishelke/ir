import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopWords = stopwords.words('english')
print(stopWords)

document1 = "The quick brown fox jumped over the lazy dog."
document2 = "The lazy dog slept in the sun."

tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

terms = list(set(tokens1 + tokens2))
print(tokens1)
print(tokens2)
print(terms)

inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stopWords:
        continue
    if term in tokens1:
        occ_num_doc1[term] = tokens1.count(term)
    if term in tokens2:
        occ_num_doc2[term] = tokens2.count(term)
print(occ_num_doc1)
print(occ_num_doc2)

for term in terms:
  if term in stopWords:
    continue
  documents = []
  if term in tokens1:
    documents.append("Document 1")
    occ_num_doc1[term] = tokens1.count(term)
  if term in tokens2:
    documents.append("Document 2")
    occ_num_doc2[term] = tokens2.count(term)
  inverted_index[term] = documents

print(occ_num_doc1)
print(occ_num_doc2)
print(inverted_index)

for term, documents in inverted_index.items():
  print(term, "->", end=" ")
  for doc in documents:
    if doc == "Document 1":
      print(f"{doc} ({occ_num_doc1.get(term, 0)}),", end= " ")
    else:
      print(f"{doc} ({occ_num_doc2.get(term, 0)}),", end= " ")