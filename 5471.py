line0=list(map(int,input().split()))
line1=list(map(int,input().split()))
line2=list(map(int,input().split()))
if(len(line1)>len(line2)):
    exc=line1
    line1=line2
    line2=exc
def onehitonemiss(a,b):
    # ab是第一个数对的两个数，cd是第二个数对的，如果满足“1命中1不命中”，则完成一次匹配
    if ((a[0] in b) and (a[1] not in b)) or ((a[1] in b) and (a[0] not in b)):
        return 1
    else:return 0


def findnum(line1,line2):
    slice1=[line1[i:i+2] for i in range(0,len(line1),2)]
    slice2=[line2[i:i+2] for i in range(0,len(line2),2)]
    hit=[]
    
    for pairs1 in slice1:
        tmphit=[]
        for pairs2 in slice2:
            if onehitonemiss(pairs1,pairs2):
                tmpres=list(set(pairs1) & set(pairs2))
                if(tmpres) not in hit:
                    hit.append(tmpres)
                    tmphit.append(tmpres)
                if (len(tmphit)>1):return [[-1]]
    return hit

res=findnum(line1,line2)
if(len(res)==1):
    if(res[0][0]!=-1):
        print(res[0][0])
    else:print(-1)
else:print(0)