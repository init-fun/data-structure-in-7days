def matching_bracket(start, end):
    if start == "(" and end == ")":
        return True
    if start == "{" and end == "}":
        return True
    if start == "[" and end == "]":
        return True
    return False


def is_valid(exp):
    lst = []
    for i in exp:
        if i in "{[(":
            lst.append(i)
        if i in "}])":
            if len(lst) == 0:
                return False
            popped_item = lst.pop()
            if not matching_bracket(popped_item, i):
                return False

    if len(lst) == 0:
        return True
    return False


print(is_valid("([{}{}])"))
