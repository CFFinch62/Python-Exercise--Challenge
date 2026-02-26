"""
Exercise data for Python Programming Exercises, Gently Explained
by Al Sweigart. 42 exercises extracted from the book.
"""

EXERCISES = [
    {
        "number": 1,
        "title": "Hello, World!",
        "description": """Write a program that, when run, greets the user by printing "Hello, world!" on the screen. Then it prints a message on the screen asking the user to enter their name. The program greets the user by name by printing "Hello," followed by the user's name.

Your program's output should look like this (using "Alice" as an example name):

Hello, world!
What is your name?
Alice
Hello, Alice""",
        "expected_output": "Hello, world!\nWhat is your name?\nAlice\nHello, Alice",
        "validation_type": "interactive",
        "asserts": [],
        "prerequisites": "print(), strings, string concatenation",
        "validation_note": "Run your program. When prompted, enter 'Alice' as the name. The output should show 'Hello, Alice'."
    },
    {
        "number": 2,
        "title": "Temperature Conversion",
        "description": """Write a convert_to_fahrenheit() function with a degrees_celsius parameter that returns the temperature in Fahrenheit. Then write a convert_to_celsius() function with a degrees_fahrenheit parameter that returns the temperature in Celsius.

Use these formulas:
  Fahrenheit = Celsius × (9 / 5) + 32
  Celsius = (Fahrenheit - 32) × (5 / 9)

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert convert_to_celsius(0) == -17.77777777777778",
            "assert convert_to_celsius(180) == 82.22222222222223",
            "assert convert_to_fahrenheit(0) == 32",
            "assert convert_to_fahrenheit(100) == 212",
            "assert convert_to_celsius(convert_to_fahrenheit(15)) == 15",
            "assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001",
        ],
        "prerequisites": "math operators",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 3,
        "title": "Odd & Even",
        "description": """Write two functions, is_odd() and is_even(), each with a single numeric parameter named number.

- is_odd() returns True if number is odd, False if even.
- is_even() returns True if number is even, False if odd.
- Both return False for numbers with fractional parts (like 3.14).
- Zero is considered an even number.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert is_odd(42) == False",
            "assert is_odd(9999) == True",
            "assert is_odd(-10) == False",
            "assert is_odd(-11) == True",
            "assert is_odd(3.1415) == False",
            "assert is_even(42) == True",
            "assert is_even(9999) == False",
            "assert is_even(-10) == True",
            "assert is_even(-11) == False",
            "assert is_even(3.1415) == False",
        ],
        "prerequisites": "modulo operator",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 4,
        "title": "Area & Volume",
        "description": """Write four functions: area(), perimeter(), volume(), and surface_area().

- area(length, width) → area = L × W
- perimeter(length, width) → perimeter = L + W + L + W
- volume(length, width, height) → volume = L × W × H
- surface_area(length, width, height) → surface area = (L×W×2) + (L×H×2) + (W×H×2)

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert area(10, 10) == 100",
            "assert area(0, 9999) == 0",
            "assert area(5, 8) == 40",
            "assert perimeter(10, 10) == 40",
            "assert perimeter(0, 9999) == 19998",
            "assert perimeter(5, 8) == 26",
            "assert volume(10, 10, 10) == 1000",
            "assert volume(9999, 0, 9999) == 0",
            "assert volume(5, 8, 10) == 400",
            "assert surface_area(10, 10, 10) == 600",
            "assert surface_area(9999, 0, 9999) == 199960002",
            "assert surface_area(5, 8, 10) == 340",
        ],
        "prerequisites": "math operators, operator precedence",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 5,
        "title": "Fizz Buzz",
        "description": """Write a fizz_buzz() function with a single integer parameter named up_to.

For numbers 1 up to and including up_to, print:
- 'FizzBuzz' if the number is divisible by both 3 and 5
- 'Fizz' if divisible only by 3
- 'Buzz' if divisible only by 5
- The number itself otherwise

Print them on one line separated by spaces (use end=' ' in print()).

Example: fizz_buzz(35) should produce:
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz""",
        "expected_output": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz ",
        "validation_type": "output",
        "run_code": "fizz_buzz(35)",
        "asserts": [],
        "prerequisites": "modulo operator, end keyword argument for print(), for loops, range()",
        "validation_note": "Call fizz_buzz(35) and compare your output to the expected output."
    },
    {
        "number": 6,
        "title": "Ordinal Suffix",
        "description": """Write an ordinal_suffix() function with an integer parameter named number that returns a string of the number with its ordinal suffix.

Examples: ordinal_suffix(42) → '42nd', ordinal_suffix(1) → '1st'

Rules:
- Numbers ending in 11, 12, 13 get 'th'
- Numbers ending in 1 (but not 11) get 'st'
- Numbers ending in 2 (but not 12) get 'nd'
- Numbers ending in 3 (but not 13) get 'rd'
- All others get 'th'

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert ordinal_suffix(0) == '0th'",
            "assert ordinal_suffix(1) == '1st'",
            "assert ordinal_suffix(2) == '2nd'",
            "assert ordinal_suffix(3) == '3rd'",
            "assert ordinal_suffix(4) == '4th'",
            "assert ordinal_suffix(10) == '10th'",
            "assert ordinal_suffix(11) == '11th'",
            "assert ordinal_suffix(12) == '12th'",
            "assert ordinal_suffix(13) == '13th'",
            "assert ordinal_suffix(14) == '14th'",
            "assert ordinal_suffix(101) == '101st'",
        ],
        "prerequisites": "strings, in operator, slices, string concatenation",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 7,
        "title": "ASCII Table",
        "description": """Write a print_ascii_table() function that displays the ASCII number and its corresponding text character, from 32 to 126. Then call it.

Your output should look like:
32  
33 !
34 "
35 #
...
124 |
125 }
126 ~

(Note: character 32 is a space, so it appears blank next to 32.)

Use Python's chr() function to convert integers to characters.""",
        "expected_output": "\n".join([f"{i} {chr(i)}" for i in range(32, 127)]),
        "validation_type": "output",
        "run_code": "print_ascii_table()",
        "asserts": [],
        "prerequisites": "for loops, range(), chr(), print()",
        "validation_note": "Call print_ascii_table() and check the output matches ASCII values 32-126."
    },
    {
        "number": 8,
        "title": "Read Write File",
        "description": """Write three functions for file I/O:

1. write_to_file(filename, text) — opens filename in write mode and writes text to it.
2. append_to_file(filename, text) — opens filename in append mode and writes text to it.
3. read_from_file(filename) — returns the full text of the file as a string.

These instructions should work:

write_to_file('greet.txt', 'Hello!\\n')
append_to_file('greet.txt', 'Goodbye!\\n')
assert read_from_file('greet.txt') == 'Hello!\\nGoodbye!\\n'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "write_to_file('greet.txt', 'Hello!\\n')",
            "append_to_file('greet.txt', 'Goodbye!\\n')",
            "assert read_from_file('greet.txt') == 'Hello!\\nGoodbye!\\n'",
        ],
        "prerequisites": "text file reading and writing, open(), with statement",
        "validation_note": "The assert statement must pass without errors."
    },
    {
        "number": 9,
        "title": "Chess Square Color",
        "description": """Write a get_chess_square_color() function with parameters column and row. Return 'black' or 'white' depending on the square's color. Column and row go from 1 to 8. If out of bounds, return ''.

Note: The top-left square (column=1, row=8 in standard notation, or use 1-based indexing with white at top-left) — check the pattern: even+even or odd+odd = white, otherwise black.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_chess_square_color(1, 1) == 'white'
assert get_chess_square_color(2, 1) == 'black'
assert get_chess_square_color(8, 8) == 'white'
assert get_chess_square_color(0, 0) == ''
assert get_chess_square_color(9, 9) == ''""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_chess_square_color(1, 1) == 'white'",
            "assert get_chess_square_color(2, 1) == 'black'",
            "assert get_chess_square_color(8, 8) == 'white'",
            "assert get_chess_square_color(0, 0) == ''",
            "assert get_chess_square_color(9, 9) == ''",
        ],
        "prerequisites": "modulo operator, if/else, comparison operators",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 10,
        "title": "Find and Replace",
        "description": """Write a find_and_replace() function with three parameters: text, old_text, new_text. Return text with all occurrences of old_text replaced by new_text. Do NOT use Python's built-in replace() method.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'",
            "assert find_and_replace('fox', 'fox', 'dog') == 'dog'",
            "assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'",
            "assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'",
            "assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'",
        ],
        "prerequisites": "slices, indexes, len(), augmented assignment operator",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 11,
        "title": "Hours, Minutes, Seconds",
        "description": """Write a get_hours_minutes_seconds() function with a total_seconds parameter. Convert the seconds into a human-readable string with 'h', 'm', 's' suffixes. Skip zero amounts (except return '0s' for 0).

Examples:
- 90 seconds → '1m 30s'
- 3601 seconds → '1h 1s'

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '25h 42s'
assert get_hours_minutes_seconds(0) == '0s'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_hours_minutes_seconds(30) == '30s'",
            "assert get_hours_minutes_seconds(60) == '1m'",
            "assert get_hours_minutes_seconds(90) == '1m 30s'",
            "assert get_hours_minutes_seconds(3600) == '1h'",
            "assert get_hours_minutes_seconds(3601) == '1h 1s'",
            "assert get_hours_minutes_seconds(3661) == '1h 1m 1s'",
            "assert get_hours_minutes_seconds(90042) == '25h 42s'",
            "assert get_hours_minutes_seconds(0) == '0s'",
        ],
        "prerequisites": "while loops, integer division, string concatenation, lists",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 12,
        "title": "Smallest & Biggest",
        "description": """Write get_smallest() and get_biggest() functions, each with a numbers parameter (a list). Return the smallest/biggest value, or None for empty lists. Do NOT use Python's min() or max() functions.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) == None
assert get_biggest([1, 2, 3]) == 3
assert get_biggest([28, 25, 42, 2, 28]) == 42
assert get_biggest([]) == None""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_smallest([1, 2, 3]) == 1",
            "assert get_smallest([3, 2, 1]) == 1",
            "assert get_smallest([28, 25, 42, 2, 28]) == 2",
            "assert get_smallest([1]) == 1",
            "assert get_smallest([]) == None",
            "assert get_biggest([1, 2, 3]) == 3",
            "assert get_biggest([28, 25, 42, 2, 28]) == 42",
            "assert get_biggest([]) == None",
        ],
        "prerequisites": "len(), for loops, lists, None value",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 13,
        "title": "Sum & Product",
        "description": """Write calculate_sum() and calculate_product() functions, each with a numbers parameter (a list of integers/floats). calculate_sum() returns the sum (0 for empty list). calculate_product() returns the product (1 for empty list). Do NOT use Python's sum() function.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert calculate_sum([]) == 0
assert calculate_sum([2, 4, 6, 8, 10]) == 30
assert calculate_product([]) == 1
assert calculate_product([2, 4, 6, 8, 10]) == 3840""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert calculate_sum([]) == 0",
            "assert calculate_sum([2, 4, 6, 8, 10]) == 30",
            "assert calculate_product([]) == 1",
            "assert calculate_product([2, 4, 6, 8, 10]) == 3840",
        ],
        "prerequisites": "lists, for loops, augmented assignment operator",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 14,
        "title": "Average",
        "description": """Write an average() function with a numbers parameter. Return the statistical average of the list. Return None for an empty list. Do NOT use Python's sum() function.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
assert average([]) == None""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert average([1, 2, 3]) == 2",
            "assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2",
            "assert average([12, 20, 37]) == 23",
            "assert average([0, 0, 0, 0, 0]) == 0",
            "assert average([]) == None",
        ],
        "prerequisites": "for loops, len(), division",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 15,
        "title": "Median",
        "description": """Write a median() function with a numbers parameter. Return the statistical median. For odd-length lists, it's the middle number when sorted. For even-length lists, it's the average of the two middle numbers. Return None for empty lists.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert median([]) == None",
            "assert median([1, 2, 3]) == 2",
            "assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5",
            "assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6",
        ],
        "prerequisites": "lists, sort(), integer division, modulo",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 16,
        "title": "Mode",
        "description": """Write a mode() function with a numbers parameter. Return the most frequently appearing number in the list. Return None for an empty list.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert mode([]) == None",
            "assert mode([1, 2, 3, 4, 4]) == 4",
            "assert mode([1, 1, 2, 3, 4]) == 1",
        ],
        "prerequisites": "dictionaries, for loops, augmented assignment operators",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 17,
        "title": "Dice Roll",
        "description": """Write a roll_dice() function with a number_of_dice parameter. Return the sum of rolling that many 6-sided dice. Import Python's random module and use random.randint().

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert roll_dice(0) == 0
for i in range(100):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert roll_dice(0) == 0",
            "for i in range(100):\n    assert 1 <= roll_dice(1) <= 6",
            "for i in range(100):\n    assert 2 <= roll_dice(2) <= 12",
            "for i in range(100):\n    assert 3 <= roll_dice(3) <= 18",
        ],
        "prerequisites": "import statements, random module, randint(), for loops, range()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 18,
        "title": "Buy 8 Get 1 Free",
        "description": """A coffee shop gives a free coffee for every 8 purchased. Write get_cost_of_coffee(number_of_coffees, price_per_coffee) that returns the total cost, accounting for free coffees.

Example: Buying 9 coffees at $2.50 = $20.00 (8 paid, 1 free).

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_cost_of_coffee(7, 2.50) == 17.50
assert get_cost_of_coffee(8, 2.50) == 20
assert get_cost_of_coffee(9, 2.50) == 20
assert get_cost_of_coffee(10, 2.50) == 22.50
assert get_cost_of_coffee(18, 1) == 16
assert get_cost_of_coffee(19, 1) == 17""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_cost_of_coffee(7, 2.50) == 17.50",
            "assert get_cost_of_coffee(8, 2.50) == 20",
            "assert get_cost_of_coffee(9, 2.50) == 20",
            "assert get_cost_of_coffee(10, 2.50) == 22.50",
            "assert get_cost_of_coffee(18, 1) == 16",
            "assert get_cost_of_coffee(19, 1) == 17",
        ],
        "prerequisites": "integer division, modulo, while loops",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 19,
        "title": "Password Generator",
        "description": """Write a generate_password() function with a length parameter. Generate a random password with at least: one lowercase letter, one uppercase letter, one digit, and one special character (~!@#$%^&*()_+). Minimum length is 12. Import random module.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
assert len(generate_password(8)) == 12
pw = generate_password(14)
assert len(pw) == 14
assert any(c in LOWER_LETTERS for c in pw)
assert any(c in UPPER_LETTERS for c in pw)
assert any(c in NUMBERS for c in pw)
assert any(c in SPECIAL for c in pw)""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'",
            "UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
            "NUMBERS = '1234567890'",
            "SPECIAL = '~!@#$%^&*()_+'",
            "assert len(generate_password(8)) == 12",
            "pw = generate_password(14)",
            "assert len(pw) == 14",
            "assert any(c in LOWER_LETTERS for c in pw)",
            "assert any(c in UPPER_LETTERS for c in pw)",
            "assert any(c in NUMBERS for c in pw)",
            "assert any(c in SPECIAL for c in pw)",
        ],
        "prerequisites": "import statements, random module, lists, strings",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 20,
        "title": "Leap Year",
        "description": """Write an is_leap_year() function with an integer year parameter. Return True if it's a leap year, False otherwise.

Rules:
- Divisible by 400 → leap year
- Divisible by 100 (but not 400) → NOT a leap year
- Divisible by 4 (but not 100) → leap year
- All others → not a leap year

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert is_leap_year(1999) == False
assert is_leap_year(2000) == True
assert is_leap_year(2001) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2400) == True""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert is_leap_year(1999) == False",
            "assert is_leap_year(2000) == True",
            "assert is_leap_year(2001) == False",
            "assert is_leap_year(2004) == True",
            "assert is_leap_year(2100) == False",
            "assert is_leap_year(2400) == True",
        ],
        "prerequisites": "modulo operator, elif statements",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 21,
        "title": "Validate Date",
        "description": """Write an is_valid_date() function with parameters year, month, and day. Return True if it's a valid date, False otherwise.

Rules:
- Month must be 1-12
- Days per month vary (31, 30, 28, or 29 for Feb on leap years)
- September, April, June, November have 30 days
- February has 28 days (29 on leap years)

You can use your is_leap_year() function from Exercise #20 in your solution.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert is_valid_date(2005, 3, 29) == True
assert is_valid_date(2005, 13, 32) == False
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2005, 4, 31) == False""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert is_valid_date(2005, 3, 29) == True",
            "assert is_valid_date(2005, 13, 32) == False",
            "assert is_valid_date(2000, 2, 29) == True",
            "assert is_valid_date(2001, 2, 29) == False",
            "assert is_valid_date(2005, 4, 31) == False",
        ],
        "prerequisites": "if/elif/else, modulo, lists, Boolean operators",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 22,
        "title": "Rock, Paper, Scissors",
        "description": """Write an rps_winner() function with parameters move1 and move2. The moves are strings 'rock', 'paper', or 'scissors'. Return 'player one', 'player two', or 'tie'.

Rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert rps_winner('rock', 'rock') == 'tie'
assert rps_winner('rock', 'scissors') == 'player one'
assert rps_winner('rock', 'paper') == 'player two'
assert rps_winner('paper', 'rock') == 'player one'
assert rps_winner('scissors', 'paper') == 'player one'
assert rps_winner('scissors', 'rock') == 'player two'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert rps_winner('rock', 'rock') == 'tie'",
            "assert rps_winner('rock', 'scissors') == 'player one'",
            "assert rps_winner('rock', 'paper') == 'player two'",
            "assert rps_winner('paper', 'rock') == 'player one'",
            "assert rps_winner('scissors', 'paper') == 'player one'",
            "assert rps_winner('scissors', 'rock') == 'player two'",
        ],
        "prerequisites": "if/elif/else, string comparison",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 23,
        "title": "99 Bottles of Beer",
        "description": """Write a program (no function needed) that prints the lyrics to "99 Bottles of Beer on the Wall." Start from 99 and count down to 1. The last stanza ends with "No more bottles of beer on the wall!"

Use "bottle" (singular) when there is only 1 bottle.

Example stanza:
99 bottles of beer on the wall,
99 bottles of beer,
Take one down,
Pass it around,
98 bottles of beer on the wall,

The last stanza:
1 bottle of beer on the wall,
1 bottle of beer,
Take one down,
Pass it around,
No more bottles of beer on the wall!""",
        "expected_output": "",
        "validation_type": "output_contains",
        "output_must_contain": ["99 bottles of beer on the wall", "No more bottles of beer on the wall!"],
        "asserts": [],
        "prerequisites": "for loops, range() with step argument, if/else, print()",
        "validation_note": "Output must start with '99 bottles' and end with 'No more bottles of beer on the wall!'"
    },
    {
        "number": 24,
        "title": "Every 15 Minutes",
        "description": """Write a program that prints every time of day in 12-hour format at 15-minute intervals, from 12:00 am to 11:45 pm.

Output should look like:
12:00 am
12:15 am
12:30 am
12:45 am
1:00 am
...
11:45 pm""",
        "expected_output": "",
        "validation_type": "output_contains",
        "output_must_contain": ["12:00 am", "12:15 am", "1:00 am", "11:45 pm"],
        "asserts": [],
        "prerequisites": "nested for loops, string formatting",
        "validation_note": "Output must include '12:00 am', '12:15 am', '1:00 am', and '11:45 pm'."
    },
    {
        "number": 25,
        "title": "Multiplication Table",
        "description": """Write a program that prints a 10x10 multiplication table with formatted headers and aligned columns.

Output should look like:
   | 1  2  3  4  5  6  7  8  9 10
---+------------------------------
 1 | 1  2  3  4  5  6  7  8  9 10
 2 | 2  4  6  8 10 12 14 16 18 20
...
10 |10 20 30 40 50 60 70 80 90 100""",
        "expected_output": "",
        "validation_type": "output_contains",
        "output_must_contain": [" 1 ", " 2 ", "10", "100"],
        "asserts": [],
        "prerequisites": "nested for loops, rjust(), print() with end=",
        "validation_note": "Output must be a formatted 10x10 table including 100 (10x10)."
    },
    {
        "number": 26,
        "title": "Handshakes",
        "description": """Write a print_handshakes() function with a people parameter (a list of names). Print each unique pair shaking hands, and return the total number of handshakes.

Example: print_handshakes(['Alice', 'Bob', 'Carol']) prints:
Alice shakes hands with Bob
Alice shakes hands with Carol
Bob shakes hands with Carol
And returns 3.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
assert print_handshakes(['Alice']) == 0
assert print_handshakes([]) == 0""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3",
            "assert print_handshakes(['Alice']) == 0",
            "assert print_handshakes([]) == 0",
        ],
        "prerequisites": "nested for loops, range(), lists, len()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 27,
        "title": "Rectangle Drawing",
        "description": """Write a draw_rectangle() function with width and height parameters. Draw a rectangle of '#' characters. If width or height is less than 1, draw nothing.

Example: draw_rectangle(5, 3) prints:
#####
#####
#####

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:
Call draw_rectangle(5, 3) and verify it prints 3 rows of 5 # characters.""",
        "expected_output": "#####\n#####\n#####",
        "validation_type": "output",
        "run_code": "draw_rectangle(5, 3)",
        "asserts": [],
        "prerequisites": "nested for loops, print() with end=",
        "validation_note": "Call draw_rectangle(5, 3) and check for 3 rows of 5 '#' characters."
    },
    {
        "number": 28,
        "title": "Border Drawing",
        "description": """Write a draw_border() function with width and height parameters. Draw a rectangular border using '+', '-', and '|' characters. If width or height < 2, draw nothing.

Example: draw_border(6, 4) prints:
+----+
|    |
|    |
+----+

Call draw_border(6, 4) in your program and check the output.""",
        "expected_output": "+----+\n|    |\n|    |\n+----+",
        "validation_type": "output",
        "run_code": "draw_border(6, 4)",
        "asserts": [],
        "prerequisites": "for loops, string multiplication, print()",
        "validation_note": "Call draw_border(6, 4) and check the output matches the example."
    },
    {
        "number": 29,
        "title": "Pyramid Drawing",
        "description": """Write a draw_pyramid() function with a height parameter. Print a pyramid of '#' characters.

Example: draw_pyramid(5) prints:
    #
   ###
  #####
 #######
#########

Call draw_pyramid(5) in your program.""",
        "expected_output": "    #\n   ###\n  #####\n #######\n#########",
        "validation_type": "output",
        "run_code": "draw_pyramid(5)",
        "asserts": [],
        "prerequisites": "for loops, string multiplication, print()",
        "validation_note": "Call draw_pyramid(5) and check the pyramid shape."
    },
    {
        "number": 30,
        "title": "3D Box Drawing",
        "description": """Write a draw_box() function with a size parameter. Draw a 3D box using text characters.

Example: draw_box(2) prints a small 3D box shape. Then call draw_box() for sizes 1 through 5.

The box should have a top surface (with '/' and '|'), front face with '|', and edges with '+' and '-'.

Call draw_box(2) to test your solution.""",
        "expected_output": "",
        "validation_type": "output_contains",
        "output_must_contain": ["+", "-", "/", "|"],
        "asserts": [],
        "prerequisites": "for loops, range() with step argument, string multiplication",
        "validation_note": "Call draw_box(2) and verify the output contains '+', '-', '/', and '|' characters."
    },
    {
        "number": 31,
        "title": "Convert Integers To Strings",
        "description": """Write a convert_int_to_str() function with an integer_num parameter. Return the integer as a string WITHOUT using Python's str() function. Handle negative numbers.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert convert_int_to_str(0) == '0'
assert convert_int_to_str(42) == '42'
assert convert_int_to_str(-99) == '-99'
assert convert_int_to_str(12345) == '12345'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert convert_int_to_str(0) == '0'",
            "assert convert_int_to_str(42) == '42'",
            "assert convert_int_to_str(-99) == '-99'",
            "assert convert_int_to_str(12345) == '12345'",
        ],
        "prerequisites": "dictionaries, modulo, integer division, while loops",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 32,
        "title": "Convert Strings To Integers",
        "description": """Write a convert_str_to_int() function with a string_num parameter. Return the integer WITHOUT using Python's int() function. Handle negative number strings (starting with '-').

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert convert_str_to_int('0') == 0
assert convert_str_to_int('42') == 42
assert convert_str_to_int('-99') == -99
assert convert_str_to_int('12345') == 12345""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert convert_str_to_int('0') == 0",
            "assert convert_str_to_int('42') == 42",
            "assert convert_str_to_int('-99') == -99",
            "assert convert_str_to_int('12345') == 12345",
        ],
        "prerequisites": "dictionaries, for loops, string indexing",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 33,
        "title": "Comma-Formatted Numbers",
        "description": """Write a comma_format() function with a number parameter. Return a string of the number with commas inserted for thousands separators. Handle decimal numbers.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert comma_format(1000) == '1,000'
assert comma_format(1000000) == '1,000,000'
assert comma_format(999) == '999'
assert comma_format(1234567890) == '1,234,567,890'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert comma_format(1000) == '1,000'",
            "assert comma_format(1000000) == '1,000,000'",
            "assert comma_format(999) == '999'",
            "assert comma_format(1234567890) == '1,234,567,890'",
        ],
        "prerequisites": "strings, for loops, modulo, len()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 34,
        "title": "Uppercase Letters",
        "description": """Write a get_uppercase() function with a text parameter. Return the string converted to uppercase WITHOUT using Python's upper() method.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_uppercase('hello') == 'HELLO'
assert get_uppercase('Hello, World!') == 'HELLO, WORLD!'
assert get_uppercase('abc123') == 'ABC123'
assert get_uppercase('') == ''""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_uppercase('hello') == 'HELLO'",
            "assert get_uppercase('Hello, World!') == 'HELLO, WORLD!'",
            "assert get_uppercase('abc123') == 'ABC123'",
            "assert get_uppercase('') == ''",
        ],
        "prerequisites": "dictionaries, for loops, string methods",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 35,
        "title": "Title Case",
        "description": """Write a get_title_case() function with a text parameter. Return the string in title case (first letter of each word capitalized, rest lowercase) WITHOUT using Python's title() method.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert get_title_case('hello world') == 'Hello World'
assert get_title_case('HELLO WORLD') == 'Hello World'
assert get_title_case('hello, world!') == 'Hello, World!'
assert get_title_case('') == ''""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert get_title_case('hello world') == 'Hello World'",
            "assert get_title_case('HELLO WORLD') == 'Hello World'",
            "assert get_title_case('hello, world!') == 'Hello, World!'",
            "assert get_title_case('') == ''",
        ],
        "prerequisites": "strings, for loops, isalpha(), upper(), lower()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 36,
        "title": "Reverse String",
        "description": """Write a reverse_string() function with a text parameter. Return the string reversed WITHOUT using Python's [::-1] slice or reversed() function. Use a swap-based approach.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert reverse_string('hello') == 'olleh'
assert reverse_string('Hello, World!') == '!dlroW ,olleH'
assert reverse_string('') == ''
assert reverse_string('a') == 'a'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert reverse_string('hello') == 'olleh'",
            "assert reverse_string('Hello, World!') == '!dlroW ,olleH'",
            "assert reverse_string('') == ''",
            "assert reverse_string('a') == 'a'",
        ],
        "prerequisites": "lists, for loops, integer division, swapping values",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 37,
        "title": "Change Maker",
        "description": """Write a make_change() function with an amount parameter (in cents). Return a dictionary with the minimum coins needed: 'quarters' (25¢), 'dimes' (10¢), 'nickels' (5¢), 'pennies' (1¢). Only include denominations used.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert make_change(30) == {'quarters': 1, 'nickels': 1}
assert make_change(100) == {'quarters': 4}
assert make_change(99) == {'quarters': 3, 'dimes': 2, 'pennies': 4}
assert make_change(0) == {}""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert make_change(30) == {'quarters': 1, 'nickels': 1}",
            "assert make_change(100) == {'quarters': 4}",
            "assert make_change(99) == {'quarters': 3, 'dimes': 2, 'pennies': 4}",
            "assert make_change(0) == {}",
        ],
        "prerequisites": "dictionaries, integer division, modulo",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 38,
        "title": "Random Shuffle",
        "description": """Write a shuffle() function with a values parameter (a list). Shuffle the list IN-PLACE using random swaps. Do NOT use Python's random.shuffle(). Import the random module.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

import random
random.seed(42)
testList = [1, 2, 3, 4, 5]
shuffle(testList)
assert testList != [1, 2, 3, 4, 5]  # Should be shuffled
assert sorted(testList) == [1, 2, 3, 4, 5]  # Same elements""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "import random",
            "random.seed(42)",
            "testList = [1, 2, 3, 4, 5]",
            "shuffle(testList)",
            "assert sorted(testList) == [1, 2, 3, 4, 5]",
        ],
        "prerequisites": "random module, randint(), for loops, list swapping",
        "validation_note": "The list must be shuffled (same elements, different order)."
    },
    {
        "number": 39,
        "title": "Collatz Sequence",
        "description": """Write a collatz() function with a starting_number parameter. Return a list of numbers in the Collatz sequence starting from starting_number and ending at 1.

Rules:
- If the current number is odd: next = current * 3 + 1
- If the current number is even: next = current // 2
- Return [] for numbers less than 1.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert collatz(1) == [1]
assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
assert collatz(0) == []
assert collatz(-1) == []""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert collatz(1) == [1]",
            "assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]",
            "assert collatz(0) == []",
            "assert collatz(-1) == []",
        ],
        "prerequisites": "while loops, modulo, lists, append()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 40,
        "title": "Merging Two Sorted Lists",
        "description": """Write a merge_two_lists() function with parameters list1 and list2. Both lists are already sorted. Return a single sorted list containing all elements from both. Do NOT use sorted() or sort().

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]",
            "assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]",
            "assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]",
            "assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]",
            "assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]",
            "assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]",
        ],
        "prerequisites": "lists, while loops, Boolean operators, append(), for loops, len()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 41,
        "title": "ROT 13 Encryption",
        "description": """Write a rot13() function with a text parameter. Return the ROT-13 encrypted version. Uppercase stays uppercase, lowercase stays lowercase. Non-letters pass through unchanged.

ROT-13 replaces each letter with the letter 13 positions later in the alphabet, wrapping around.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert rot13('Hello, world!') == 'Uryyb, jbeyq!'",
            "assert rot13('Uryyb, jbeyq!') == 'Hello, world!'",
            "assert rot13(rot13('Hello, world!')) == 'Hello, world!'",
            "assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'",
            "assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'",
        ],
        "prerequisites": "strings, ord(), chr(), for loops, islower(), isupper()",
        "validation_note": "All assert statements must pass without errors."
    },
    {
        "number": 42,
        "title": "Bubble Sort",
        "description": """Write a bubble_sort() function with a list parameter named numbers. Sort the list IN-PLACE using the bubble sort algorithm and also return the sorted list. Do NOT use Python's sort() method or sorted() function.

Bubble sort compares every pair of adjacent elements and swaps them if they're in the wrong order.

The app tests your solution automatically — just write the required function(s) above.
When you click ✓ Submit, these checks will run in the background:

assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]
assert bubble_sort([]) == []
assert bubble_sort([1]) == [1]""",
        "expected_output": "",
        "validation_type": "assert",
        "asserts": [
            "assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]",
            "assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]",
            "assert bubble_sort([]) == []",
            "assert bubble_sort([1]) == [1]",
        ],
        "prerequisites": "lists, for loops, range(), nested loops, swapping values",
        "validation_note": "All assert statements must pass without errors."
    },
]
