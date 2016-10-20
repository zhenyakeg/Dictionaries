__author__ = 'student'
import string as str
Dictionary_file= open('en-ru.txt', 'r')
Output = open('output.txt', 'w')
Input = open('input.txt','r')
Dict  = {}
for x in Dictionary_file.readlines():
    Dict[x.strip().split( '\t-\t')[0]] = x.strip().split( '\t-\t')[1]
for x in Input.readlines():
    print(x,file=Output)
    tr = x.lower().split()
    for t in str.punctuation:
        for x in tr:
            x = x.replace(t,'')
    for i in range(len(tr)):
         if Dict.get(tr[i]) == None:
            tr[i] = tr[i]
         else:
             tr[i]= Dict.get(tr[i])
    print(*tr,file=Output)




