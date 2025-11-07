def get_num_words(path):
    with open(path) as f:
        content = f.read()
    split_contents = content.split()
    return len(split_contents)

chars = []

def letter_count(path):
    with open(path) as f:
        content = f.read()
    individual_letters = content.split()
    for word in individual_letters:
        letters = tuple(word)
        for entry in letters:
            lower = entry.lower()
            found = False
            for entries in chars:
                if entries["char"] == lower:
                    entries["count"] += 1
                    found = True
            if not found:
                chars.append({"char": lower, "count": 1})
    return chars

def sort(list):
    return list["count"]

from main import path

letter_count(path)

chars.sort(reverse=True, key=sort)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(path)} total words")
print("--------- Character Count -------")
for i in chars:
    if(i["char"].isalpha()):
        print(f"{i["char"]}: {i["count"]}")
print("============= END ===============")
