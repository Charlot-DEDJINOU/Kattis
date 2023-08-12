def gcd(a,b) :
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)

num , dem = map(int , input().split('/'))
num = (num - 32*dem)*5
dem = 9 * dem
signe = 1 if num * dem >= 0 else -1
num = abs(num)
dem = abs(dem)
tmp = gcd(max(num,dem) , min(num,dem))
num = signe*(num//tmp)
dem = dem//tmp
print(num,dem,sep='/')