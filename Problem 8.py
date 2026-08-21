def reverse_and_swap(s):
    words = s.split(' ')
    result = ' '.join(word[::-1].swapcase() for word in words)
    return result

s = input("Enter a string: ")
print(reverse_and_swap(s))