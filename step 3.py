a = []
print("Вводите строки матрици отдельно, элементы через пробел")
for i in range(3):
    b = list(input().split())
    a.append(b)
for i in range(3):
    for j in range(3):
        a[i][j] = float(a[i][j])
A = -1
B = a[0][0] + a[1][1] + a[2][2]
C = a[2][0] * a[0][2] + a[2][1] * a[1][2] + a[0][1] * a[1][0] - a[1][1] * a[2][2] - a[0][0] * a[2][2] - a[0][0] * a[1][1]
D = a[2][0] * a[0][1] * a[1][2] + a[1][0] * a[2][1] * a[0][2] + a[1][1] * a[2][2] * a[0][0] - a[0][2] * a[2][0] * a[1][1] - a[2][1] * a[1][2] * a[0][0] - a[1][0] * a[0][1] * a[2][2]
if B >= 0:
    B = '+ ' + str(B)
elif C >= 0:
    C = '+ ' + str(C)
elif D >= 0:
    D = '+ ' + str(D)

print (A,'xxx ', B,'xx ', C,'x ', D, sep = '')