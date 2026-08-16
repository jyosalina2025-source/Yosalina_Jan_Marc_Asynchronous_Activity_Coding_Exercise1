s = input("Enter a string: ")
n = int(input("Enter the index: "))

if n < len(s):
    s = s[:n] + s[n+1:]

print(s)