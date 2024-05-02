# A) Precision, Recall, F-measure

def calculate_metrics(retrieved_set, relevant_set):
  true_positive = len(retrieved_set.intersection(relevant_set))
  false_positive = len(retrieved_set.difference(relevant_set))
  false_negative = len(relevant_set.difference(retrieved_set))

  print("True Positive: ", true_positive, "\nFalse Positive: ", false_positive, "\nFalse Negative: ", false_negative, "\n")

  precision = true_positive / (true_positive + false_positive)
  recall = true_positive / (true_positive + false_negative)
  f_measure = 2 * precision * recall / (precision + recall)
  return precision, recall, f_measure

retrieved_set = set(["doc1", "doc2", "doc3"])  #predicted set
relevant_set = set(["doc1", "doc4"])           #actually needed set (relevant)
precision, recall, f_measure = calculate_metrics(retrieved_set, relevant_set)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-measure: {f_measure}")


# B) Average precision

from sklearn.metrics import average_precision_score
y_true = [0, 1, 1, 0, 1, 1]   #binary prediction
y_scores = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]   #model's estimation score
average_precision = average_precision_score(y_true, y_scores)
print(f'Average precision-recall score: {average_precision}')