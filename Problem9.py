def count_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    repeated = [char for char in freq if freq[char] > 1]

    repeated.sort()
    return repeated


s = input("Enter a string: ")
result = count_characters(s)

print(len(result))
if result:
    print(' '.join(result))
else:
    print("None")