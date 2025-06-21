import re

def is_palindrome(s):
    if s is None:
        return False
    if not isinstance(s, (str, int, float)):
        return False
        
    if isinstance(s, (int, float)):
        s = str(s)
        
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s).lower()
    
    if not cleaned:
        return False
    
    return cleaned == cleaned[::-1]
