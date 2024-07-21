from collections import Counter


def weightedUniformStrings(chain, queries):
    res = []
    words = Counter(chain)
    words = {
        (ord(k) - 96) * i
        for k, v in words.items()
        for i in range(
            1,
            v + 1,
        )
    }
    for q in queries:
        res.append('Yes' if q in words else 'No')
    print('\n'.join(res))
    return res


# weightedUniformStrings('abbcccdddd', [1, 7, 5, 4, 15])
# weightedUniformStrings('abccddde', [1, 3, 12, 5, 9, 10])
# weightedUniformStrings('aaabbbbcccddd', [9, 7, 8, 12, 5])

"""
    res = []
    words = Counter(chain)
    words = {
        f'{k*i}': (ord(k) - 96) * i
        for k, v in words.items()
        for i in range(
            1,
            v + 1,
        )
    }
    for q in queries:
        text = 'Yes'
        if q not in words.values():
            text = 'No'
        res.append(text)
"""
