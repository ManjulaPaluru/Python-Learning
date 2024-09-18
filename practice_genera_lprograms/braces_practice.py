def braces_test(input_string):
    stack = []
    for char in input_string:
        if char == "{":
            stack.push()
        elif char == '}':
            current_value = stack.pop()
            if current_value != '{':
                return False
    if stack:
        return False
    return True

input_string = ()
result = braces_test(input_string)
if result ==True:

    print("Braces are balanced ")
else:
    print("Bracess are not balanced")