file1 = open("input.txt","r")
l=file1.readlines()
d={}
for i in l:
    i=i.replace("\n","")

    k=i.split(" ")
    for j in k:
        if(j in d):
                d[j]=d[j]+1
        else:
            d[j]=1
file2=open("output.txt","w+")
for i in d:
    k=i+":"+str(d[i])+"\n"
    file2.write(k)
    


    




