def bracket_check(brackets):
    stack = []
    for i in brackets:
        if i in "{[(":
            stack.append(i)
        if i in "}])":
            if i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return True


print(bracket_check("({{}])"))
print(bracket_check("({[{}]})"))
