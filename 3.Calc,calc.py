import decimal
decimal.getcontext().prec = 3
print("整数Nかもん")
N = decimal.Decimal(int(input()))
print("整数Mかもん")
M = decimal.Decimal(int(input()))
print("結果: ",N/M)