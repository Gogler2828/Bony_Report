print("文字列")
S = str(input())
print("間隔")
N = int(input())
mes = S[0]
for num in range(1,len(S)):
    mes = mes + " "*N + S[num]
print(mes)