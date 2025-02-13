def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(print_wordcount()) + " words found in the document")
    decreasing_letter_count = []
    char_count = letter_count()
    for i in char_count:
        to_append = {"letter": i,"count":char_count[i]}
        decreasing_letter_count.append(to_append)
    
    decreasing_letter_count.sort(reverse=True, key = sort_by)
    for i in decreasing_letter_count:
        if i["letter"].isalpha():
            print("The \'", i["letter"], "\' character was found ", i["count"], " times", sep='')

def print_wordcount():
    with open("books/frankenstein.txt") as f:
        frankenstein_contents = f.read()
        return(len(frankenstein_contents.split()))

def letter_count():
    with open("books/frankenstein.txt") as f:
        letter_count = {}
        frankenstein_contents = f.read()
        for letter in frankenstein_contents:
            if letter.lower() not in letter_count:
                letter_count[letter.lower()] = 1
            else:
                letter_count[letter.lower()] += 1
        return letter_count

def sort_by(dict):
    return dict["count"]

main()
#print_wordcount()
#letter_count()