N = int(input())

for i in range(N):
    A, B = input().split()
    print("encaixa" if A.endswith(B) else "nao encaixa")
