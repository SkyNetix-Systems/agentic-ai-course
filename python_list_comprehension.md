# Python List Comprehension

## 1. What is List Comprehension?

**List comprehension** is a short and readable way to create a new list
from an existing iterable, such as a list, tuple, or range. It can also
filter items using a condition.

## 2. Basic Syntax

```python
new_list = [expression for item in iterable if condition]
```

- `expression`: What should be added to the new list.
- `item`: The current item being processed.
- `iterable`: The collection being looped through.
- `if condition`: Optional filter; only matching items are included.

## 3. Example: Create a List of Squares

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

**Explanation:** Python takes each number, squares it, and adds the
result to the new list.

## 4. Example: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

**Explanation:** The condition `number % 2 == 0` selects only even
numbers.

## 5. Example: Convert Names to Uppercase

```python
names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)
```

**Output:**

```text
['ALICE', 'BOB', 'CHARLIE']
```

**Explanation:** The `upper()` method converts each name to uppercase.

## 6. Example: List Comprehension with a Dictionary

The `items()` method returns each dictionary key and value as a pair.

```python
required_variables = {
    "OPENAI_API_KEY": "key123",
    "CLAUDE_MODEL": "",
    "GEMINI_API_KEY": "key456"
}

missing_variables = [
    variable
    for variable, value in required_variables.items()
    if not value
]

print(missing_variables)
```

**Output:**

```text
['CLAUDE_MODEL']
```

**Explanation:** - `required_variables.items()` iterates over dictionary
key-value pairs. - `variable` represents the key. - `value` represents
the corresponding value. - `if not value` selects entries with an empty
or otherwise false value. - The resulting list contains the names of
missing variables.

## 7. The Same Logic Using a Traditional For Loop

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

Both approaches produce the same result.

## 8. List Comprehension vs. Traditional For Loop

---

List Comprehension Traditional For Loop

---

Short and concise More lines of code

Creates a list directly Often uses `append()` to build a
list

Useful for simple transformations Useful for complex logic and
and filtering multiple steps

---

## 9. Important Points to Remember

1.  List comprehension creates a new list.
2.  The `if` condition is optional.
3.  You can transform items, filter items, or do both.
4.  Use it when it makes the code easier to read.
5.  For complicated logic, a traditional `for` loop may be clearer.

## 10. Practice Exercises

1.  Given `[2, 4, 6, 8]`, create a list containing the square of each
    number.
2.  Given `[10, 15, 20, 25, 30]`, create a list containing only numbers
    greater than 20.
3.  Given `["python", "java", "javascript"]`, create a list of uppercase
    names.
4.  Given `[1, 2, 3, 4, 5, 6, 7, 8]`, create a list containing only odd
    numbers.

### Quick Challenge

What will this code print?

```python
numbers = [1, 2, 3, 4, 5]
result = [number * 10 for number in numbers if number > 2]
print(result)
```

**Answer:** `[30, 40, 50]`

---

**Key takeaway:** Read a list comprehension as: _"For each item in a
collection, include the result in a new list if the condition is
satisfied."_
