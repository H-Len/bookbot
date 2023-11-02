def main():
    book_path = "github.com/H-Len/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    print(get_word_count(book_path))
    print(get_report(get_letter_count(book_path)))

def get_word_count(path):
    word_count = 0
    with open(path) as f:
        text = f.read()
    split_text = text.split()
    for i in split_text:
        word_count += 1
    return f"{word_count} words found in the document"

# Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any uppercase letters to lowercase letters, we don't want duplicates.
def get_letter_count(path):
    letter_count = {}
    with open(path) as f:
        text = f.read()
    split_text = text.split()
    for word in split_text:
        low_word = word.lower()
        for i in low_word:
            if i in letter_count:
            # print(i)
                letter_count[i] += 1
            else:
                letter_count[i] = 1

    return letter_count

def get_report(letter_count):
    report = []
    report.append("--- Begin report of books/frankenstein.txt ---")
    for entry in letter_count:
        if entry.isalpha():
            report.append(f"The {entry} character was found {letter_count[entry]} times")
    return report
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()