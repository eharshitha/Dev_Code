y = []
command = "~*</>*~"
def secret_command(s,l):
    if s == command:
        print(sorted(l,key = len))
        exit()

print("\n")
while True:
    x = input(">> ")
    y.append(x)
    secret_command(x,y)