# Write a function that takes in a list of numbers and prints out each number that is less than 10.
print('Less Than 10')

def less_than_10(list_num):
    """Function will take in a list of numbers and print each less than 10"""
    for num in list_num:
        if num < 10:
            print(num)

list_of_numbers = [1, 40, 4, 7, 73, 12, 80, 110]
less_than_10(list_of_numbers)
print('---------------')

# Write a function that takes in a list of words. For each word, the function should print a tuple of (first_letter_of_word, word).
print('Word Tupe')

def word_tupe(list_words):
    """Function will take in a list of words and print a tuple containing the 1st letter and the word"""
    for word in list_words:
        print((word[0], word ))

list_of_words = ['bull', 'noon', 'raisin', 'fairy', 'lilly']
word_tupe(list_of_words)
print('---------------')

# Write a function that takes in a list of numbers. It should print every other number, starting with the number at index 0
print('Every Other')

def every_other(list_num):
    """Function wil take in a list of numbers and print every other number"""
    for num in list_num[::2]:
        print(num)

every_other(list_of_numbers)
print('---------------')

# Write a function that takes in a list and an item. It should return True if the list contains the item. Otherwise, return False.
print('Contains Item')

def contains_item(list_item, chosen_item):
    """Function takes in a list of items and a item, then returns True or False depending on if it's in the list"""
    if chosen_item in list_item:
        return True

    return False

list_of_items = ['brush', 'jacket', 'wrench', 'bottle', 'shovel']

print(contains_item(list_of_items, 'brush'))
print(contains_item(list_of_items, 'bucket'))

print('---------------')
# Write a function that takes in a string and returns the length of that string. You cannot use the len function.
print('String Length')

def string_length(string):
    """Function takes in a string and returns the length of the string"""
    count = 0
    for char in string:
        count += 1
    return count

print(string_length('bob'))
print(string_length('videographer'))

print('---------------')

# Write a function that takes in a sentence as a string. The function should print the length of each word in the sentence.
#  Your sentence will not contain any punctuation.
print('Each Word Length')

def each_word_length(sentence):
    sentence = sentence.split(' ')
    for word in sentence:
        print(len(word))

phrase = 'The bee is looking for pollen in the field'
each_word_length(phrase)
print('---------------')

# Write a function that takes in a list of numbers and returns the largest number in the list. You cannot use the max function.
print('Largest Num')

def largest_num(list_of_numbers):
    max = 0
    for num in list_of_numbers:
        if num < max:
            max = num

    return max
