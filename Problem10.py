def sort_reverse_characters(s):
    s = s.lower()
    words = s.split(' ')
    sorted_words = [''.join(sorted(word)) for word in words]
    result = ' '.join(sorted_words)
    return result

s = input("Enter a string: ")
print(sort_reverse_characters(s))