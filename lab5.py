 #1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_and_display(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = "anudip.txt"
read_and_display(filename)



#2. Write a function in Python to count and display the total number of words in a text file "ABC.txt"

def count_and_display_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
count_and_display_words(filename)


# 3.Write a function in Python to count uppercase character in a text file "ABC.txt"

def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print(f"Total number of uppercase characters in '{filename}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
count_uppercase_characters(filename)


# 4.Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words_less_than_4_characters(filename):
    try:
        with open(filename, 'r') as file:
            words = []
            for line in file:
                line_words = line.strip().split()
                words.extend([word for word in line_words if len(word) < 4])
            
            print(f"Words less than 4 characters in '{filename}':")
            for word in words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
display_words_less_than_4_characters(filename)