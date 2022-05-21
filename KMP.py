def KMP(text, pattern):
    '''
    KMP algorithm
    '''
    # Preprocessing
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    fail = [0] * m
    j = 1
    k = 0
    while j < m and k < m:
        if pattern[j] == pattern[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    # Searching
    i = 0
    j = 0
    result = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j)
                j = fail[j - 1]
        elif j > 0:
            j = fail[j - 1]
        else:
            i += 1
    return (1 if (result != []) else 0)


