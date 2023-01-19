l=list(map(int,input("enter heights").split()))
l1=[round(l[i]/2.2049,2) for i in range(0,len(l))]

print(l1)