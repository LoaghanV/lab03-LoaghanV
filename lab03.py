# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    word_to_change = word.lower()
    if word_to_change[0] in 'aeiou':
        return word + 'way' 
    else:
        return word[1:] + word_to_change[0] + 'ay'


def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    words_to_count = sentence.split()
    number_of_letters = []
    for words in range(len(words_to_count)):
        letter_count = 0
        for letters in range(len(words_to_count[words])):
            letter_count += 1
        number_of_letters.append(letter_count)
    return number_of_letters


def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    words_to_reverse = sentence.split()
    words_to_reverse = words_to_reverse[::-1]
    reversed_sentence = ''
    for words in range(len(words_to_reverse)):
        reversed_sentence += words_to_reverse[words]
        if words != len(words_to_reverse) - 1:
            reversed_sentence += ' '
    return reversed_sentence


def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    word_to_count = text.lower()
    letter_count_dict = {}
    for letter in word_to_count:
        if letter.isalpha():
            if letter in letter_count_dict:
                letter_count_dict[letter] += 1
            else:
                letter_count_dict[letter] = 1
    return letter_count_dict


def main():
    # Optional scratch space - use this to try your functions with sample values.
    #print(pig_latin("banana"))                    # ananabay
    #print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    #print(reverse_words("the quick brown fox"))   # fox brown quick the
    #print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
