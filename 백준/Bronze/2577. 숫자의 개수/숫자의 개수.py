num1=int(input())
num2=int(input())
num3=int(input())

quest=str(num1*num2*num3)
qli=[]
for indx in range(len(quest)):
    qli.append(quest[indx])

qli.sort()
answer=[]
ansdic={}
for i in range(len(qli)):
    if qli[i] not in answer:
        answer.append(qli[i])
        ansdic[qli[i]]=1
    elif qli[i] in answer:
        ansdic[qli[i]]+=1
for i in range(10):
    try:
        print(ansdic[str(i)])
    except:
        print(0)