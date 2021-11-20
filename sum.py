def sum(a,b):
    return (a+b)


if __name__ =="__main__":
    a,b=map(int,input().split())
    ans = sum(a,b)
    print("sum of",a,"and",b,"is: ",ans)