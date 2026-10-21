end   = "----------------------------------"
end_2 = "__________________________________"
def print_end(t):
    print("Thank you for playing again!")
    if t == 1:
        print(end)
    if t == 2:
        print(end_2)

while True:
# Main loop
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number!!")
        continue

    # Checking
    if x % 2 == 0:
        print("It's even!")
    else:
        print("It's odd!")

    while True:

        a = input("Again[y/n]: ")

        if a.lower() == "y":
            print_end(1)
            break
        elif a.lower() == "n":
            print("Thank you for your time!")

            print("Bye!")
            exit()
        else:
            print("Please enter y or n!")