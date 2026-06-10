import math
from hashtable import CustomHashTable

class NaiveBayesClassifier:
    def __init__(self):
        self.spam_counts = CustomHashTable()
        self.ham_counts = CustomHashTable()
        self.total_spam = 0
        self.total_ham = 0

    def fit_sample(self, token_list, label):
        if label == "spam":
            self.total_spam += len(token_list)
            for token in token_list:
                current_count = self.spam_counts.get(token)
                self.spam_counts.put(token, current_count + 1)
        else:
            self.total_ham += len(token_list)
            for token in token_list:
                current_count = self.ham_counts.get(token)
                self.ham_counts.put(token, current_count + 1)

    def calculate_log_prob(self, token_list, label):
        """Applies Laplace smoothing parameters internally via the scratch Hash Table."""
        vocab_size = 1000
        if label == "spam":
            log_prob = math.log(0.5)
            for token in token_list:
                count = self.spam_counts.get(token) + 1
                log_prob += math.log(count / (self.total_spam + vocab_size))
        else:
            log_prob = math.log(0.5)
            for token in token_list:
                count = self.ham_counts.get(token) + 1
                log_prob += math.log(count / (self.total_ham + vocab_size))
        return log_prob
