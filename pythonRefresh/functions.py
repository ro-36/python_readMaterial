def palandrome (st):
    for i in range (len(st)//2):
        if(st[i]!=st[len(st)-1-i]):
            return False
    return True
        
ans = palandrome("naman")
print(ans)