fh=open("sum.txt","r");s=0
content=fh.readline()
for i in content:
    k=content.split(" ")
    s=s+k
print(s)

