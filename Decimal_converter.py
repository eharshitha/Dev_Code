print("\nWelcome to the Binary Converter")

x = int(input("Enter a decimal number: "))

print("\nChoose a conversion:")
print("1. Decimal → Binary")
print("2. Decimal → Octal")
print("3. Decimal → Hexadecimal\n")

choice = input(">> ")

if choice == "1":
    print("Binary:", bin(x)[2:])

elif choice == "2":
    print("Octal:", oct(x)[2:])

elif choice == "3":
    print("Hexadecimal:", hex(x)[2:])

else:
    print("Invalid choice!")