def longestWord(text):
    terms = []
    term = ""
    for c in text:
        if c.isalpha():
            term += c
        else:
            if term != "": 
                terms.append(term)
            term = ""
    if term != "": 
        terms.append(term)
    length = max(len(term) for term in terms)
    for term in terms:
        if len(term) == length:
            return term
