n=int(input())
words=list(map(str,input().split()[:n]))
words.sort()
words.sort(key=len)
for i in words:
    print(i,end=" ")
