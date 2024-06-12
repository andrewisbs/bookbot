def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    # print(words_by_first(text))
    unsorted_list = char_in_text(text)
    mid_list = []
    # for k, v in unsorted_list.items():
    #     mid_list.append({k:v})
    # print(mid_list)
    mid_list = sorted(unsorted_list.items(), key=lambda x:x[1], reverse=True) 
    # print(mid_list)
    # print(char_in_text(text))
    for group in mid_list:
        if group[0].isalpha():
            print(f"The '{group[0]}' character was fround {group[1]} times.") 
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def words_by_first(input_text):
    word_dict = {}
    text = input_text.lower()
    for word in text:

        try:
            value = word_dict[word[0]]
            word_dict[word[0]] = value + 1
        except:
            word_dict[word[0]] = 1
    return word_dict


def char_in_text(input_text):
    char_dict = {}
    text = input_text.lower()
    for word in text:
        for let in word:
            try:
                value = char_dict[let]
                char_dict[let] = value + 1
            except:
                char_dict[let] = 1
    return char_dict 




# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):

    return dict["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]

main()