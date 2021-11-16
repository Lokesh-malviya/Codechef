from sys import stdin, stdout
n = int(stdin.readline())
for i in range(n):
    A = int(stdin.readline())
    if A>=1 and A<100:
        stdout.write("Easy"+"\n")
    elif A>=100 and A<200:
        stdout.write("Medium"+"\n")
    elif A>=200 and A<=300:
        stdout.write("Hard"+"\n")