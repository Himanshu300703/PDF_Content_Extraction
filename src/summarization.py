from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Define a function to generate a summary based on text length
def summarize_text(text, num_sentences=3):
    try:
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return text
        
        vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        sentence_vectors = vectorizer.fit_transform(sentences)
        sentence_scores = sentence_vectors.sum(axis=1).A1
        
        ranked_sentences = np.argsort(sentence_scores)[::-1]
        summary_sentences = [sentences[i] for i in ranked_sentences[:num_sentences]]
        summary = ' '.join(summary_sentences)
        
        return summary
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return text
