word=input()
li=[]
li=['c=','c-','dz=','d-','lj','nj','s=','z=']
for element in li:
    word=word.replace(element,'a')
print(len(word))