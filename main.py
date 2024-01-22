
def main():
    file_contents = open_file("books/frankenstein.txt")
    print(report(file_contents))

def open_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(str):
    words = str.split()
    return len(words)

def count_letters(str):
    str = str.lower()
    letters = {}

    for letter in str:
        if (letter in letters):
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters

def sort_f(element):
    return element["count"]

def report(str):
    result = f"--- Begin report of books/frankenstein.txt ---\n{count_words(str)} words found in the document\n\n"
    letters = count_letters(str)
    lst_letters = [{"ch": c, "count": letters[c]} for c in letters]
    lst_letters.sort(key=sort_f, reverse = True)
    for d in lst_letters:
        ch = d["ch"]
        count = d["count"]
        if (ch.isalpha()):
            result += f"The '{ch}' character was found {count} times\n"
    result += "--- End report ---"
    
    return result

main()
