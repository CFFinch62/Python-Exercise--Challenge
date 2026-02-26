"""
Reference solutions for Python Exercises for Beginners
by Al Sweigart. Matches exercises in exercises_data.py.
Note: Function and variable names use PEP 8 snake_case,
which differs slightly from the original book's camelCase.
"""

SOLUTIONS = {
    1: '''# Print "Hello, world!" on the screen:
print('Hello, world!')
# Ask the user for their name:
print('What is your name?')
# Get the user's name from their keyboard input:
name = input()
# Greet the user by their name:
print('Hello, ' + name)''',

    2: '''def convert_to_fahrenheit(degrees_celsius):
    return degrees_celsius * (9 / 5) + 32

def convert_to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * (5 / 9)''',

    3: '''def is_odd(number):
    return number % 2 == 1

def is_even(number):
    return number % 2 == 0''',

    4: '''def area(length, width):
    return length * width

def perimeter(length, width):
    return length * 2 + width * 2

def volume(length, width, height):
    return length * width * height

def surface_area(length, width, height):
    return ((length * width) + (length * height) + (width * height)) * 2''',

    5: '''def fizz_buzz(up_to):
    for number in range(1, up_to + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' ')
        elif number % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(number, end=' ')

fizz_buzz(35)''',

    6: '''def ordinal_suffix(number):
    number_str = str(number)
    if number_str[-2:] in ('11', '12', '13'):
        return number_str + 'th'
    if number_str[-1] == '1':
        return number_str + 'st'
    if number_str[-1] == '2':
        return number_str + 'nd'
    if number_str[-1] == '3':
        return number_str + 'rd'
    return number_str + 'th' ''',

    7: '''def print_ascii_table():
    for i in range(32, 127):
        print(i, chr(i))

print_ascii_table()''',

    8: '''def write_to_file(filename, text):
    with open(filename, 'w') as file_obj:
        file_obj.write(text)

def append_to_file(filename, text):
    with open(filename, 'a') as file_obj:
        file_obj.write(text)

def read_from_file(filename):
    with open(filename) as file_obj:
        return file_obj.read()''',

    9: '''def get_chess_square_color(column, row):
    if column < 1 or column > 8 or row < 1 or row > 8:
        return ''
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black' ''',

    10: '''def find_and_replace(text, old_text, new_text):
    replaced_text = ''
    i = 0
    while i < len(text):
        if text[i:i + len(old_text)] == old_text:
            replaced_text += new_text
            i += len(old_text)
        else:
            replaced_text += text[i]
            i += 1
    return replaced_text''',

    11: '''def get_hours_minutes_seconds(total_seconds):
    if total_seconds == 0:
        return '0s'
    hours = total_seconds // 3600
    total_seconds = total_seconds % 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    hms = []
    if hours > 0:
        hms.append(str(hours) + 'h')
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    if seconds > 0:
        hms.append(str(seconds) + 's')
    return ' '.join(hms)''',

    12: '''def get_smallest(numbers):
    if len(numbers) == 0:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def get_biggest(numbers):
    if len(numbers) == 0:
        return None
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest''',

    13: '''def calculate_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def calculate_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result''',

    14: '''def average(numbers):
    if len(numbers) == 0:
        return None
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)''',

    15: '''def median(numbers):
    if len(numbers) == 0:
        return None
    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle_index] + numbers[middle_index - 1]) / 2
    else:
        return numbers[middle_index]''',

    16: '''def mode(numbers):
    if len(numbers) == 0:
        return None
    number_count = {}
    most_freq_number = None
    most_freq_number_count = 0
    for number in numbers:
        if number not in number_count:
            number_count[number] = 0
        number_count[number] += 1
        if number_count[number] > most_freq_number_count:
            most_freq_number = number
            most_freq_number_count = number_count[number]
    return most_freq_number''',

    17: '''import random

def roll_dice(number_of_dice):
    total = 0
    for i in range(number_of_dice):
        total += random.randint(1, 6)
    return total''',

    18: '''def get_cost_of_coffee(number_of_coffees, price_per_coffee):
    number_of_free_coffees = number_of_coffees // 9
    number_of_paid_coffees = number_of_coffees - number_of_free_coffees
    return number_of_paid_coffees * price_per_coffee''',

    19: '''import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def generate_password(length):
    if length < 12:
        length = 12
    password = []
    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.append(UPPER_LETTERS[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL[random.randint(0, 12)])
    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 74)])
    random.shuffle(password)
    return ''.join(password)''',

    20: '''def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False''',

    21: '''def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def is_valid_date(year, month, day):
    if not (1 <= month <= 12):
        return False
    if is_leap_year(year) and month == 2 and day == 29:
        return True
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False
    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False
    elif month == 2 and not (1 <= day <= 28):
        return False
    return True''',

    22: '''def rps_winner(move1, move2):
    if move1 == 'rock' and move2 == 'paper':
        return 'player two'
    elif move1 == 'rock' and move2 == 'scissors':
        return 'player one'
    elif move1 == 'paper' and move2 == 'scissors':
        return 'player two'
    elif move1 == 'paper' and move2 == 'rock':
        return 'player one'
    elif move1 == 'scissors' and move2 == 'rock':
        return 'player two'
    elif move1 == 'scissors' and move2 == 'paper':
        return 'player one'
    else:
        return 'tie' ''',

    23: '''for number_of_bottles in range(99, 1, -1):
    print(number_of_bottles, 'bottles of beer on the wall,')
    print(number_of_bottles, 'bottles of beer,')
    print('Take one down,')
    print('Pass it around,')
    if (number_of_bottles - 1) == 1:
        print('1 bottle of beer on the wall,')
    else:
        print(number_of_bottles - 1, 'bottles of beer on the wall,')
print('1 bottle of beer on the wall,')
print('1 bottle of beer,')
print('Take one down,')
print('Pass it around,')
print('No more bottles of beer on the wall!')''',

    24: '''for meridiem in ['am', 'pm']:
    for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        for minutes in ['00', '15', '30', '45']:
            print(hour + ':' + minutes + ' ' + meridiem)''',

    25: '''print('   | 1  2  3  4  5  6  7  8  9 10')
print('---+------------------------------')
for column in range(1, 11):
    print(str(column).rjust(2) + '|', end='')
    for row in range(1, 11):
        print(str(column * row).rjust(3) + ' ', end='')
    print()''',

    26: '''def print_handshakes(people):
    number_of_handshakes = 0
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], 'shakes hands with', people[j])
            number_of_handshakes += 1
    return number_of_handshakes''',

    27: '''def draw_rectangle(width, height):
    if width < 1 or height < 1:
        return
    for row in range(height):
        for column in range(width):
            print('#', end='')
        print()

draw_rectangle(5, 3)''',

    28: '''def draw_border(width, height):
    if width < 2 or height < 2:
        return
    print('+' + ('-' * (width - 2)) + '+')
    for i in range(height - 2):
        print('|' + (' ' * (width - 2)) + '|')
    print('+' + ('-' * (width - 2)) + '+')

draw_border(6, 4)''',

    29: '''def draw_pyramid(height):
    for row_number in range(height):
        left_side_spaces = ' ' * (height - (row_number + 1))
        pyramid_row = '#' * (row_number * 2 + 1)
        print(left_side_spaces + pyramid_row)

draw_pyramid(5)''',

    30: '''def draw_box(size):
    if size < 1:
        return
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')
    print('+' + '-' * (size * 2) + '+')

draw_box(2)''',

    31: '''def convert_int_to_str(integer_num):
    if integer_num == 0:
        return '0'
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    if integer_num < 0:
        is_negative = True
        integer_num = -integer_num
    else:
        is_negative = False
    string_num = ''
    while integer_num > 0:
        ones_place_digit = integer_num % 10
        string_num = DIGITS_INT_TO_STR[ones_place_digit] + string_num
        integer_num //= 10
    if is_negative:
        return '-' + string_num
    else:
        return string_num''',

    32: '''def convert_str_to_int(string_num):
    DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    if string_num[0] == '-':
        is_negative = True
        string_num = string_num[1:]
    else:
        is_negative = False
    integer_num = 0
    for i in range(len(string_num)):
        digit = DIGITS_STR_TO_INT[string_num[i]]
        integer_num = (integer_num * 10) + digit
    if is_negative:
        return -integer_num
    else:
        return integer_num''',

    33: '''def comma_format(number):
    number = str(number)
    if '.' in number:
        fractional_part = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractional_part = ''
    triplet = ''
    comma_number = ''
    for i in range(len(number) - 1, -1, -1):
        triplet = number[i] + triplet
        if len(triplet) == 3:
            comma_number = triplet + ',' + comma_number
            triplet = ''
    if triplet != '':
        comma_number = triplet + ',' + comma_number
    return comma_number[:-1] + fractional_part''',

    34: '''LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
    'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M',
    'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
    'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

def get_uppercase(text):
    uppercase_text = ''
    for character in text:
        if character in LOWER_TO_UPPER:
            uppercase_text += LOWER_TO_UPPER[character]
        else:
            uppercase_text += character
    return uppercase_text''',

    35: '''def get_title_case(text):
    titled_text = ''
    for i in range(len(text)):
        if i == 0:
            titled_text += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titled_text += text[i].upper()
        else:
            titled_text += text[i].lower()
    return titled_text''',

    36: '''def reverse_string(text):
    text = list(text)
    for i in range(len(text) // 2):
        mirror_index = len(text) - 1 - i
        text[i], text[mirror_index] = text[mirror_index], text[i]
    return ''.join(text)''',

    37: '''def make_change(amount):
    change = {}
    if amount >= 25:
        change['quarters'] = amount // 25
        amount = amount % 25
    if amount >= 10:
        change['dimes'] = amount // 10
        amount = amount % 10
    if amount >= 5:
        change['nickels'] = amount // 5
        amount = amount % 5
    if amount >= 1:
        change['pennies'] = amount
    return change''',

    38: '''import random

def shuffle(values):
    for i in range(len(values)):
        swap_index = random.randint(0, len(values) - 1)
        values[i], values[swap_index] = values[swap_index], values[i]''',

    39: '''def collatz(starting_number):
    if starting_number < 1:
        return []
    sequence = [starting_number]
    num = starting_number
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num // 2
        sequence.append(num)
    return sequence''',

    40: '''def merge_two_lists(list1, list2):
    result = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1
    if i1 < len(list1):
        for j in range(i1, len(list1)):
            result.append(list1[j])
    if i2 < len(list2):
        for j in range(i2, len(list2)):
            result.append(list2[j])
    return result''',

    41: '''def rot13(text):
    encrypted_text = ''
    for character in text:
        if not character.isalpha():
            encrypted_text += character
        else:
            rotated_letter_ordinal = ord(character) + 13
            if character.islower() and rotated_letter_ordinal > 122:
                rotated_letter_ordinal -= 26
            if character.isupper() and rotated_letter_ordinal > 90:
                rotated_letter_ordinal -= 26
            encrypted_text += chr(rotated_letter_ordinal)
    return encrypted_text''',

    42: '''def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers''',
}
