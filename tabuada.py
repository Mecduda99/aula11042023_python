tabuada = 1
n2 = 1

# while tabuada <= 10:
#     while n2 <=10:
#         multiplicacao = tabuada * n2
#         print(str(tabuada) + " X " + str(n2) + " = " + str(multiplicacao))
#         n2 += 1
#     tabuada += 1
#     n2 = 1
while tabuada <= 10:
    for n2 in range(1,11):
        multiplicacao = tabuada * n2
        print(str(tabuada) + " X " + str(n2) + " = " + str(multiplicacao))
        n2 += 1
    tabuada += 1
    
