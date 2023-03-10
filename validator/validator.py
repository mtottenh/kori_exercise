from sys import stdin

""""
Things you might need:
1. A list! To hold things. In python, we can use a list like list:

# creating a new list:
my_list = []

# Adding an element to the list:
my_list.append('a')

# Print out what is in the list
print(my_list)

# Remove an element from the end of the list
element = my_list.pop()
"""

def validate_parens(input: str) -> bool:
    '''
    Input: String to validate
    Output: True/False
    '''
    stack = []
    for character in input:
            match character:
                case '{':
                    stack.append(character)
                case '[':
                    stack.append(character)
                case '(':
                    stack.append(character)
                case '}':
                    top = stack.pop()
                    if top != '{':
                        return False
                case ']':
                    top = stack.pop()
                    if top != '[':
                        return False
                case ')':
                    top = stack.pop()
                    if top != '(':
                        return False
    return len(stack) == 0

if __name__ == "__main__":
    for line in stdin:
        print(f"Valid: {validate_parens(line)}")