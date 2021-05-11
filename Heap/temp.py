def distinct_chars(arr):
    win_start = 0
    freq = {}

    for i in range(len(arr)):
        right_char = arr[i]
        if right_char not in freq:
            freq[right_char] = 0
        freq[right_char] += 1

        while len(freq) > 2:
            left_char = arr[win_start]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            win_start += 1

    print(sum(freq.values()))


distinct_chars(["A", "B", "C", "B", "B", "C"])
