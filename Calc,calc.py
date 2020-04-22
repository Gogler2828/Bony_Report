import decimal
print("整数Nかもん")
N = int(input())
print("整数Mかもん")
M = int(input())
decimal.getcontext().prec = 3
n = decimal.Decimal(N)
m = decimal.Decimal(M)
print("結果: ",n/m)