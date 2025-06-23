def combine_anagrams(words):
    if not words:
        return []

    anagram_groups = {}
    
    for word in words:
        normalized = ''.join(sorted(word.lower()))
        
        if normalized not in anagram_groups:
            anagram_groups[normalized] = []
        anagram_groups[normalized].append(word)
    
    return list(anagram_groups.values())

input_words = ['cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream']
result = combine_anagrams(input_words)
print(result)
