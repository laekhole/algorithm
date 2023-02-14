hap=":-)"
sa=":-("
word=input()
if word.count(hap)==word.count(sa):
    if word.count(hap)!=0:
        print('unsure')
    else:
        print('none')
elif word.count(hap)>word.count(sa):
    print('happy')
else:
    print('sad')