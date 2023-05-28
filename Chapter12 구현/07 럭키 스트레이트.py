n = input()
n = list(n)

a = n[:(len(n)//2)]
b = n[(len(n)//2):]
a2 = [int(i) for i in a]
b2 = [int(i) for i in b]
if sum(a2) == sum(b2):
    print("LUCKY")
else:
    print("READY")
