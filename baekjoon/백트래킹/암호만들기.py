#1759 #12:40
#L:자릿수,C:문자의 종류
#in_perm 리스트의 크기는 C, #아스키코드-97
#리스트에 있는 알파벳들
import sys
sys.stdin=open("암호만들기.text","r")

def perm(a,k):

    if k==L:
        vowel_cnt=0
        consonant_cnt=0
        for idx in range(L):
            if a[idx] in vowel:
                vowel_cnt+=1
            else:
                consonant_cnt+=1
        if vowel_cnt>=1 and consonant_cnt>=2:
            word=''
            for j in range(L):
                word+=a[j]
            print(word)
    else:
        in_perm=[False]*C

        for i in range(k):
            for idx,val in enumerate(data):
                if a[i]==val:
                    in_perm[idx]=True
                    break
        for i in range(C-1,-1,-1):
            if in_perm[i]:
                temp=i+1
                break
        else:
            temp=0

        cnt=0
        c=[0]*C
        for i in range(temp,C):
            if not in_perm[i]:
                c[cnt]=data[i]
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1)

L,C=map(int,input().split())
data=list(map(str,input().split()))
a=[0]*L
vowel=['a','e','i','o','u']
for i in range(len(data)):
    data[i] = ord(data[i])
data.sort()
for i in range(len(data)):
    data[i] = chr(data[i])

perm(a,0)
#14:02