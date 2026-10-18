import time
import keyboard

max = 10000

print("\nKeep on Clicking the Space key if you want to end it quickly!")

while True:
    MXL = int(input(f"Enter a countdown (below {max}): "))
    if MXL >= max:
        print(
            f"Enter a number below {max}!!!"
        )
    else:
        break

slp = 0.25
n = []

print(n)

for i in range(MXL+1):
    n.append(i)

for i in range(MXL+1):
    print(n[MXL - i])
    if keyboard.is_pressed("space"):
        slp = 0
    time.sleep(slp)
