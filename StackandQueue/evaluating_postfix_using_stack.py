def evaluate_postfix(postfix):
    stack = []

    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            x = stack.pop()
            y = stack.pop

            if i == "+":
                stack.append(y + x)
            elif i == "-":
                stack.append(y - x)
            elif i == "*":
                stack.append(y * x)
            elif i == "/":
                stack.append(y / x)
            elif i == "%":
                stack.append(y % x)
            elif i == "^":
                stack.append(y ^ x)
    return stack.pop()
