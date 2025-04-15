"""Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only."""
s = input("Enter words: ")
b = s.strip().split(" ")
num = len(b[-1])
print(f"The length of the last word is {num}")
