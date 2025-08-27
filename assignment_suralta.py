def reverse_sentence(sntnce):
    return sntnce[::-1]

def count_vowels(sntnce):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in sntnce if ch in vowels)

def check_palindrome(sntnce):
    cleaned = ''.join(ch.lower() for ch in sntnce if ch.isalnum())
    return cleaned == cleaned[::-1]

def find_and_replace(sntnce, old, new):
    return sntnce.replace(old, new)

def format_title_case(sntnce):
    return sntnce.title()

def split_into_words(sntnce):
    return sntnce.split()

def word_frequency(sntnce):
    words = sntnce.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def swap_case(sntnce):
    return sntnce.swapcase()



sntnce = input("Enter a sentence: ")

while True:
    print("\nChoose an operation:")
    print("0. Enter a new sentence")
    print("1. Reverse the sentence")
    print("2. Count vowels")
    print("3. Check if palindrome")
    print("4. Find and replace a word")
    print("5. Format (title case)")
    print("6. Split into words")
    print("7. Word frequency counter")
    print("8. Swap case")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        sntnce = input("Enter a new sentence: ")
    elif choice == '1':
        print("Reversed:", reverse_sentence(sntnce))
    elif choice == '2':
        print("Vowel count:", count_vowels(sntnce))
    elif choice == '3':
        print("Palindrome?", check_palindrome(sntnce))
    elif choice == '4':
        old = input("Word to find: ")
        new = input("Word to replace with: ")
        sntnce = find_and_replace(sntnce, old, new)
        print("Updated sentence:", sntnce)
    elif choice == '5':
        print("Title case:", format_title_case(sntnce))
    elif choice == '6':
        print("Words:", split_into_words(sntnce))
    elif choice == '7':
        print("Word frequencies:", word_frequency(sntnce))
    elif choice == '8':
        print("Swapped case:", swap_case(sntnce))
    elif choice == '9':
        print("Exiting program. Thanks!")
        break
    else:
        print("Invalid choice, try again.")