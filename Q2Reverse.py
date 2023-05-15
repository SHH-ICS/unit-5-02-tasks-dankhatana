# Create a program that will accept a word and output the word one letter at a time in reverse.
word = input("Enter a word: ")
reverse_word = word[::-1]
for letter in reverse_word:
    print(letter)