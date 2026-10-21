n1 = float(input("Enter num - 1: "))
n2 = float(input("Enter num - 2: "))
print("Enter"
        "\n+     for addition"
        "\n-     for subtraction"
        "\n*     for multiplication"
        "\n/     for division"
        "\n**    for power / exponent"
        "\n%     for modulo"
        "\n//    for floor division"
        "\n< > = for comparison")

i = input("\n>>")
def Calculate(f1,e,f2):
    if e == "+":
        return f1 + f2
    elif e == "-":
        return f1 - f2
    elif e == "*":
        return f1 * f2
    elif e == "/":
        return f1 / f2
    elif e == "**":
        return f1 ** f2
    elif e == "%":
        return f1 % f2
    elif e == "//":
        return f1 // f2
    elif e == "<" or e == ">" or e == "=":
        if n1 > n2:
            return f"{n1} > {n2}"
        elif n1 < n2:
            return f"{n1} < {n2}"
        else:
            return f"{n1} = {n2}"
print(Calculate(n1,i,n2))