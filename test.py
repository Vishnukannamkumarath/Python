dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000};l=[]
s="IX";t=0;j=0
for i in range(len(s)):
	l.append(s[i])
if(l[len(l)-1] in "IXC"):
	l.append("e")
while(j<len(l)):
	if(l[j]=='e'):
		break;
	elif(l[j]=="I" and l[j+1]=="e"):
		t=t+dict[l[j]];break;
	elif(l[j] in "XC" and l[j+1]=='e'):
		break;
	elif(l[j]=='I' and l[j+1]=="V"):
		t=t+(dict['V']-dict['I'])
		j+=2
	elif(l[j]=='I' and l[j+1]=="X"):
		t=t+(dict['X']-dict['I'])
		j+=2
	elif(l[j]=='X' and l[j+1]=='L'):
		t=t+(dict['L']-dict['X'])
		j+=2
	elif(l[j]=="X" and l[j+1]=='C'):
		t=t+(dict['C']-dict['X'])
		j+=2
	elif(l[j]=='C' and l[j+1]=='D'):
		t=t+(dict['D']-dict['C'])
		j+=2
	elif(l[j]=='C' and l[j+1]=='M'):
		t=t+(dict['M']-dict['C'])
		j+=2
	else:
		 t=t+dict[l[j]];j+=1
print(t)
		
		
