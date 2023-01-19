n=input()
def string_alternative(str1):
    for i in range(0,len(str1),2):
        print(str1[i],end="")
if __name__=="__main__":
    string_alternative(n)