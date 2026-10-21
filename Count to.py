import time

x = int(input("Enter a number: "))
DOS = float(input("Enter a delay of seconds (0.75 / 0.0): "))
for i in range(x+1):
    print(i)
    time.sleep(DOS)