import re
from collections import defaultdict

def count_words(text):
    if not text or not isinstance(text, str):
        return {}

    words = re.findall(r'\b[а-яa-z]+\b', text.lower())
    
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    
    return dict(word_freq)
