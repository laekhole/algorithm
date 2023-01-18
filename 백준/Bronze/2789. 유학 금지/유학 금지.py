word=input()
# word=word.upper()
li=[]
for e in word:
    li.append(e)
# print(li)
taboo="CAMBRIDGE"

tbli=[]
for e in taboo:
    tbli.append(e)
# print(tbli)

ans=[]
for e in word:
    if e not in tbli:
        ans.append(e)
print(*ans,sep="")