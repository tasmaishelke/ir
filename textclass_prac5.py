import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv(r"IRPrac4Dataset.csv - Sheet1.csv")
data = df["covid"]+ " " +df["fever"]

x = data.astype(str)
y = df['flu']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
x_train_counts = vectorizer.fit_transform(x_train)
x_test_counts = vectorizer.transform(x_test)

classifier = MultinomialNB()
classifier.fit(x_train_counts, y_train)

data1 = pd.read_csv(r"IRPrac4Dataset.csv - Sheet1.csv")
new_data=data1["covid"] + " " + data1["fever"]
new_data_counts = vectorizer.transform(new_data.astype(str))

predictions = classifier.predict(new_data_counts)
new_data = predictions

print(new_data)

accuracy = accuracy_score(y_test, classifier.predict(x_test_counts))

print(f"\nAccuracy: {accuracy:.2f}")
print("Classification Report: ")
print(classification_report(y_test, classifier.predict(x_test_counts)))