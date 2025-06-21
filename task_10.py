import re
from collections import defaultdict

def get_word_stats(text):
    if not text:
        return {}

    words = re.findall(r'\b[a-zа-я]+\b', text.lower())

    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    
    return dict(word_count)