__author__ = 'student'
N = int(input())
dic = {}
Input = open('input5.txt','r')
A = []
for x in Input.readlines():
    dic[x.strip().split(':')[0]] = x.strip().split( ':')[1]
for i in range(N):
    a = input()

    for x in dic:
        if dic[x].find(a) != -1:
            A.append(x)
    A.append('\n')
print(*A)
