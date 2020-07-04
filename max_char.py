x=raw_input('Enter the String: ')
count={}
for i in x:
    count.setdefault(i,0)
    count[i]=count[i]+1
    
for j in count.keys():
    if ' ' in j:
        del count[j]

print(max(count.items(),key=lambda k:k[1]))
