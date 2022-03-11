def lengthOfLongestSubstring(s):
    start = 0
    d = dict()
    local_max, global_max = 0, 0
    for i, c in enumerate(s):
        if c in d and d[c] >= start:
            start = d[c] + 1
        d[c] = i
        local_max = i - start + 1
        global_max = max(global_max, local_max)
    return global_max


if __name__ == "__main__":
    s = "asdjklsdfgqweassda"
    print(lengthOfLongestSubstring(s))