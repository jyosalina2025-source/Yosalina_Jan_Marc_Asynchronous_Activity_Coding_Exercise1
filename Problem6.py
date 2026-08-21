import string

def is_pangram(s: str) -> bool:
    char_set = set(s.lower())
    alphabet_set = set(string.ascii_lowercase)
    
    return alphabet_set.issubset(char_set)

input_string = input("Enter a string: ")

print(is_pangram(input_string))                
                                    