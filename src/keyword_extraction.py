from rake_nltk import Rake

def extract_keywords(text, max_keywords=5):
    try:
        rake = Rake()
        
        rake.extract_keywords_from_text(text)
        
        keywords = rake.get_ranked_phrases()[:max_keywords]
        
        return keywords
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return []

if __name__ == "__main__":
    text = """
    The Indian economy has undergone a significant transformation over the past few decades, driven by rapid industrialization, globalization, and digitalization. 
    As one of the fastest-growing economies in the world, India has witnessed a surge in innovation and entrepreneurship. However, challenges such as income inequality, 
    unemployment, and environmental degradation persist. The government has implemented various policies to address these issues, including reforms in education, 
    healthcare, and infrastructure development. With a young and dynamic workforce, India is poised to become a global leader in technology and services in the coming years.
    """
    keywords = extract_keywords(text)
    print(f"Keywords: {keywords}")
