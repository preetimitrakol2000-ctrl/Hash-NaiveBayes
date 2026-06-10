from model import NaiveBayesClassifier

if __name__ == "__main__":
    print("🗄️  Activating Hash-NaiveBayes Optimized String Lookup Map Array...")

    nb_model = NaiveBayesClassifier()
    nb_model.fit_sample(["prize", "claim", "free", "cash"], "spam")
    nb_model.fit_sample(["meeting", "project", "research", "team"], "ham")

    test_words = ["claim", "free", "project"]
    
    spam_score = nb_model.calculate_log_prob(test_words, "spam")
    ham_score = nb_model.calculate_log_prob(test_words, "ham")

    verdict = "🚨 SPAM DETECTION VERIFIED" if spam_score > ham_score else "✅ LEGITIMATE INCOMING COMMUNICATIONS"
    print(f"📥 Query Words: {test_words}")
    print(f"🔮 Automated NLP Pipeline Prediction: [{verdict}]")
