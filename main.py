def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = words(file_contents)   # Calls function and sends file_contents to it
    print(f"{word_count} words found in the document")
    count = charcount(file_contents)
    alphalist = sort(count)
    
    for line in alphalist:
        print(f"The '{line['letter']}' character was found '{line['times']}' times")


def words(file_contents):
    total = 0
    words = file_contents.split()
    for word in words:
        total += 1
    return total

def charcount(file_contents):
    count = {}
    lowered_string = file_contents.lower()
    chars = list(lowered_string)
    for char in chars:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            elif char in count:
                count[char] += 1
    return count

def sort(count):
    alphalist = []
    for l, t in count.items():  # *** Changed from iterating on count to use count.items() ***
        alphalist.append({"letter": l, "times": t})  # *** Changed assignment to append (it's a list, dont overwrite) ***
    alphalist.sort(reverse=True, key=lambda x: x['times'])  
    return alphalist  # *** Returned alphalist from the sort function ***

main()