def is_isogram(word):
    return len(word) == len(set(word.lower() or word.upper())) or len(word)==0

print(is_isogram("ClArUswAY"))