def gcd(a,b) :
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)

def solution(num , dem) :
    tmp = gcd(max(num,dem) , min(num,dem))
    num = num//tmp
    dem = dem//tmp
    print(num,dem,sep='/')

n = int(input())
s = list(map(int , input().split()))
for x in s[1:] :
    solution(s[0] , x)