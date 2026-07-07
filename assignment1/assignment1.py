# ---- Task 1 ----

def hello():
    return "Hello!"

# ---- Task 2 ----

def greet(name):
    return f"Hello, {name}!"

# ---- Task 3 ----

def calc(val1, val2, operation="multiply"):
    if operation == "add":
        return val1 + val2
    elif operation == "subtract":
        try:
            return val1 - val2
        except TypeError:
            return "You can't subtract those values!"
    elif operation == "multiply":
        try:
            return val1 * val2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "divide":
        try:
            return val1 / val2
        except TypeError:
            return "You can't divide those values!"
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "modulo":
        try:
            return val1 % val2
        except TypeError:
            return "You can't modulo those values!"
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "int_divide":
        try:
            return val1 // val2
        except TypeError:
            return "You can't integer divide those values!"
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "exponent":
        try:
            return val1 ** val2
        except TypeError:
            return "You can't exponent those values!"
        
# ---- Task 4 ----

def data_type_conversion(value, new_type):
    try:
        if new_type == "int":
            return int(value)
        elif new_type == "float":
            return float(value)
        elif new_type == "str":
            return str(value)
        else:
            return f"Invalid data type: {new_type}"
    except ValueError:
        return f"You can't convert {value} into a {new_type}."   
    
# --- Task 5 ----

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# --- Task 6 ----

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result;

# --- Task 7 ----

def student_scores(parameter, **kwargs):
    if parameter == "best":
        best_student = None
        best_score = 0
        for key, value in kwargs.items():
            if value > best_score:
                best_score = value
                best_student = key
        return best_student

    elif parameter == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
# --- Task 8 ----

def titleize(string):
    words = string.split()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()

    for i, word in enumerate(words):
        if word not in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            words[i] = word.capitalize()
    return " ".join(words)

# --- Task 9 ----

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# --- Task 10 ----

def pig_latin(string):
    words = string.split()
    vowel = "aeiou"
    for word in words:
        if word[0] in vowel:
            words[words.index(word)] = word + "ay"
        else: 
            i = 0
            while word[i] not in vowel: 
                if word[i] == "q" and word[i+1] == "u":
                    i += 2
                else:
                    i += 1
            words[words.index(word)] = word[i:] + word[:i] + "ay"
   
    return " ".join(words)


