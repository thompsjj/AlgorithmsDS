import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check_matches(text):
    
    opening_brackets = {'{','[','('}
    closing_brackets = {'}',']',')'}
    opening_stack = []
    
    for i, item in enumerate(text, start=1):
        if item in opening_brackets:
            opening_stack.append(Bracket(item,i))
        elif item in closing_brackets:
            # check top bracket on opening stack
            
            if not opening_stack:
                return i
            
            current_bracket = opening_stack.pop()
            if not current_bracket.match(item):
                return i
            
    if opening_stack:
        current_bracket = opening_stack.pop()
        return current_bracket.position
    
    return "Success"

text = sys.stdin.read()
print(check_matches(text))