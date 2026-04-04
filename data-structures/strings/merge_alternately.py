def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    
    if len(word1) == 0:
        return word2
    if len(word2) == 0:
        return word1
    
    i = 0
    j = 0
    res = []

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1
            
    return ''.join(res)


print(mergeAlternately("ab", "pqrs"))