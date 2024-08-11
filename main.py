
def get_book_contents(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def get_wordcount(book_contents):
    return len(book_contents.split())

def parse_characters(book_contents):
    text = book_contents.lower()
    char_map = {}
    for c in text:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1
    return char_map

def sort_on(dict):
    return dict["count"]

def get_characters(book_contents):
    character_map = parse_characters(book_contents)

    # convert to list of dictionary
    cmap_list = []
    for key in character_map.keys():
        dict_entry = {}
        dict_entry["char"] = key
        dict_entry["count"] = character_map[key]
        cmap_list.append(dict_entry)

    cmap_list.sort(reverse=True, key=sort_on)
    return cmap_list

def main():
    book_path = "books/frankenstein.txt"
    
    try:
        book = get_book_contents(book_path)

        print(f"--- Begin report of {book_path} ---")
        print(f"{get_wordcount(book)} words found in the document\n")
        characters = get_characters(book)
        for item in characters:
            if item["char"].isalpha():
                print(f"The {item['char']} character was found {item['count']} times")      
        print("--- End report ---") 
    except FileNotFoundError:
        print(f"Book file {book_path} not found.")
    
main()