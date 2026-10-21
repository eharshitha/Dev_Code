while True:
    try:
        x = int(input("\nEnter a number: "))
        break
    except ValueError:
        print("Please enter a number!")
        continue
while True:
    try:
        r = int(input("Enter a range [10 recommended]:"))
        break
    except ValueError:
        print("Please enter a range!")
        continue

for i in range(r):
    print(f"{x} x {i+1} = {(i + 1) * x } ")