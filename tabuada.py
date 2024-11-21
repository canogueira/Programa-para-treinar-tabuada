# Faça um programa que solicite ao usuário um número que ele
# queira treinar a tabuada. Você irá solicitar ao mesmo a resposta
# do cálculo do número informado multiplicado por 1, 2 até 10.
# A cada resposta você deverá validar e imprimir :”CORRETO” ou
# “QUE PENA, VOCÊ ERROU, O VALOR CORRETO É X “, no lugar
# de ”X“ coloque o valor correto Ao final imprima “Total de
# acertos: y” e “Total de erros z”, onde “y“ deverá ser o total de
# acertos e “z“ o total de erros. Ao final da sequencia deve-se
# perguntar se deseja começar denovo.

while True:
    numero = int(input("digite o numero que você quer treinar a tabuada: "))
    acertos = 0
    erros = 0
    multiplicador = 0
    while multiplicador < 10:
        multiplicador += 1 
        resposta = int(input(f"quanto é {numero} x {multiplicador} = "))
       
        resultado_correto = numero * multiplicador 

        if resposta == resultado_correto:
            print("correto")
            acertos += 1 
        else:
            print(f"que pena você errou, o resultado correto é {resultado_correto} ")
            erros += 1 
    print(f"total de acertos {acertos} ")
    print(f"total de erros {erros} ")
    refazer = input("deseja fazer novamente (s/n) ? ").lower()
    if refazer == "n":
       break












