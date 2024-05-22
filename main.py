def main():
    bookpath = "books/frankenstein.txt"
    text = get_text(bookpath)
    print(f"--- Begin report of {bookpath} ---")
    number_of_words = word_counter(text)
    print(f"{number_of_words} words found in the document\n")
    letter_dict = count_letters(text)
    sorted_dict = sorted(letter_dict)
    for letter in sorted_dict:
        print(f"The '{letter}' character was found {letter_dict[letter]} times")
    print("--- End report ---")


def count_letters(text):
    text_lowered = text.lower()
    letter_dict = {}
    for letter in text_lowered:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict
        


def get_text(path):
     with open(path) as f: #the file is opened using its relative path (relative to where we run the program)
        return f.read() #the content of the file is retrieved through the read() function and put in a variable

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

main()
