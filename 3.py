__author__ = 'student'
import string as str
Lic = open('LICENSE', 'r')
s = Lic.read()
for t in str.punctuation:
    s=s.replace(t,' ')
s = s.lower()
Dic = {}
for x in s.split():
    if x in Dic:
        Dic[x] += 1
    else:
        Dic[x]  = 1
def Max(A):
    m1=0
    k1=None
    for k,v in A.items():
        if v > m1:
            m1=v
            k1=k

    return(k1,m1)
def Get_k(A):
    return A[1]
Dic = sorted(Dic.items(), key = Get_k, reverse=True)
print(*Dic[:10],sep='\n')
