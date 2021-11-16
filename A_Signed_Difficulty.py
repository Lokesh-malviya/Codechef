n = input()
S = len(n)
if S>=4:
    if int(n[3:])>=0 and int(n[3:])<=2:
        print(f"{n[0:2]}-")
    elif int(n[3:])>=3 and int(n[3:])<=6:
        print(f"{n[0:2]}")
    elif int(n[3:])>=7 and int(n[3:])<=9:
        print(f"{n[0:2]}+")
elif S<4:
    if int(n[2:])>=0 and int(n[2:])<=2:
        print(f"{n[0:1]}-")
    elif int(n[2:])>=3 and int(n[2:])<=6:
        print(f"{n[0:1]}")
    elif int(n[2:])>=7 and int(n[2:])<=9:
        print(f"{n[0:1]}+")