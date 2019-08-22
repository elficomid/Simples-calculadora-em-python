sinal = ['+','-','*','/']
while True:
    algoritmo = input('Digite uma operação:')
    i = 0
    opera = num1 = num2 = 0
    for c in algoritmo:
        for s in sinal:
            if s == c:
                opera = s
                num1=int(algoritmo[:i])
                num2=int(algoritmo[i+1:])
                if opera == '+':
                    print(num1+num2)
                if opera == '-':
                    print(num1-num2)
                if opera == '*':
                    print(num1*num2)
                if opera == '/':
                    print(num1/num2)
        i+=1
    ler = input('Deseja continuar? ')
    if ler.upper() == 'N' or ler.upper() == 'NAO':
        break





#print(f'O valor de A é {num1} e o valor de B é {num2}')
