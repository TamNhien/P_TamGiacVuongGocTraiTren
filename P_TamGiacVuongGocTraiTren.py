n = int(input("Nhap chieu cao tam giac: "))
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print("* ", end="")
    print()