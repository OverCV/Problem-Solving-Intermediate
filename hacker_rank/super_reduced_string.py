def super_reduced_string(s: str):
    removed: bool = True
    while removed:
        removed: bool = False
        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                s = s[: i - 1] + s[i + 1 :]
                removed = True
            i += 1
    return s
