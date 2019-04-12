def longestWord(text):
    terms = text.split(' ')
    words = []
    for term in terms:
        words.append("".join([c for c in term if c.isalpha()]))
    length = max(len(word) for word in words)
    for word in words:
        if len(word) == length:
            return word
