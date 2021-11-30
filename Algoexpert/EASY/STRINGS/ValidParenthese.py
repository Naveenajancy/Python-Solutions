#That's not always the case, there are subtle differences:
# if not bar: will execute if bar is any kind of zero or empty container, or False.
# Many people do use not bar where they really do mean bar is not None
# Time O(n)
# Space
def balancedBrackets(string):
    # Write your code here.
    stack = []
    mapping = {"}": "{", ")": "(", "]": "["}
    openingBrackets = "({["
    closingBrackets = ")}]"
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

def validParentheses(str):
    stack = []
    openingBrackets = "({["
    closingBrackets = ")}]"
    mapping = {")":"(",  "}":"{", "]":"["}
    for char in str:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack.pop() != mapping[char]:
                return False
    return not stack

string = "(141[])(){waga}((51afaw))()hh()"
string = "aafwgaga()[]a{}{gggg"
string = "(()agwg())((()agwga()())gawgwgag)"

#print(validParentheses("([{}])[]"))
print(validParentheses("{{[[[[]]]]}}"))

