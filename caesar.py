a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
d=len(a)
n=input("ENTER PLAIN TEXT MESSAGE:\n")
#CONVERT INTO CAESAR SUBSTITUITION CIPHER TEXT
l=len(n)
for i in range(0,l):
    for j in range(0,d):
        if(a[j]==n[i]):
              j+=3
              if j>d:
                  j=j%26
                  print(a[j],end=" ")
              print(a[j],end=" ")
