# importação das bibliotecas para efeitos de interatividade com o usuário
from time import sleep
import pyautogui

# função de mostrar números primos para o usuário
def primos():
    primos = []
    # verifica todos os números primos do intervalo definido (50 ~ 100)
    for num in range(50, 100):
        div = 2
        contador = 0
        # verifica se o número é divisível por outro número além de 1 e dele mesmo
        while div < num:
            if num % div == 0:
                contador = contador + 1
                div = div + 1
            else:
                div = div + 1
                # adiciona o número a lista caso seja validado pelo loop
        if contador == 0:
            primos.append(num)
        else:
            contador = 0
    print(primos)

# cálculo do máximo divisor comum de a e b
def mdc(a, b):
    # realiza o cálculo do mdc até que "b" seja "0" e atribui o último valor de "b" antes de ser "0" a "a"
    while b != 0:
        resto = a % b
        a = b
        b = resto
        # retorna o valor "a" como resultado
    return a

# verificação de números válidos para a chave "E" em um determina intervalo (0 ~  100)
def opcoes_chaves_E(n):
    opcoes_chaves_e = []
    # verifica todos os números no intervalo determinado
    for num in range(0, 50):
        # adiciona o número que obedecer a condição de ser menor que a chave "N" e mdc de "N" e número seja 1
        if 1 < num <= n and mdc(n, num) == 1:
            opcoes_chaves_e.append(num)
            # retorna a lista de números válidos
    return opcoes_chaves_e

# função de criptografar a mensagem
def cifrar_msg(e, n):
    msg = (input("\033[34mDigite o texto a ser criptografado: "))
    # codifica cada letra da frase
    for letra in msg:
        # converte a letra em seu número correspondente da tabela ASCII
        ord_letra = ord(letra)
        # muda o valor da letra elevando a "E" e depois resultado módulo "N"
        letra_crip = (ord_letra ** e) % n
        # transforma o valor encontrado anteriormente em seu caráter respectivos da tabela ASCII e adiciona a lista
        msg_criptografada.append(chr(letra_crip))
        # mostra a mensagem criptografada para o usuário
    pyautogui.typewrite("Texto Criptografado: ", interval=0.10)
    for letra_cifrada in msg_criptografada:
        print(letra_cifrada, end="",)

# função de descriptografar a mensagem
def descriptografar(msg_crip, d, n):
    # descripta cada carácter da mensagem
    for letra in msg_crip:
        # converte o carácter em seu número correspondente da tabela ASCII
        ord_letra = ord(letra)
        # muda o valor do carácter elevando a "D" e depois resultado módulo "N"
        letra_descrip = (ord_letra ** d) % n
        msg_descriptografada.append(chr(letra_descrip))
        # mostra a mensagem descriptografada para o usuário
    print("\033[34mTexto descriptografado:")
    for letra_descrp in msg_descriptografada:
        print(letra_descrp, end="")

# cálculo do inverso multiplicativo
def inverso_multiplicativo(e, n):
    # realiza o cálculo para todos os números no intervalo 1 ~ chave "N"
    for x in range(1, n):
        # cálculo para encontrar e retornar o inverso multiplicativo no intervalo definido
        if (e % n) * (x % n) % n == 1:
            return x
        # mensagem mostrada ao usuário caso o inverso multiplicatvo não seja encontrado
    print("\033[34mInverso multiplicativo não encontrado.")


msg_criptografada = []
msg_descriptografada = []
opcao = 0
# menu de opções para o usuário selecionar
while opcao != 3:
    print('''\033[34m   
Por favor selecione uma opção abaixo    
[1] Criptografar uma mensagem
[2] Descriptografar uma mensagem
[3] Sair do programa''')
    opcao = int(input('\033[34m>>>>>Qual sua opção?: '))
# criptografia de mensagens    
    if opcao == 1:
        primos()
        P = int(input("\033[34mEscolha um  número primo (sugestão acima): "))
        primos()
        Q = int(input("\033[34mEscolha outro número primo (sugestão acima): "))
        N = P * Q
        tot_n = (P - 1) * (Q - 1)
        E = int(input(f"\033[34mEscolha a chave E {opcoes_chaves_E(tot_n)}: "))
        cifrar_msg(E, N)
        D = inverso_multiplicativo(E, tot_n)
        print("\n\033[34mGerando chaves criptográficas")
        for cont in range(3, 0, -1):
            print(cont)
            sleep(1)
        print(f"D: {D}, E: {E}, N: {N}")
# descriptografia das mensagens
    elif opcao == 2:
        msg_criptografada = input("\033[34mDigite o texto criptografado: ")
        D = int(input("\033[34mDigite a chave D: "))
        N = int(input("\033[34mDigite a chave N: "))
        print("\n\033[34mDescriptografando sua mensagem")
        for cont in range(3, 0, -1):
            print(cont)
            sleep(1)
        descriptografar(msg_criptografada, D, N)
# finalização do programa        
    elif opcao == 3:
        pyautogui.typewrite('Finalizando...', interval=0.10)
        pyautogui.typewrite('\n.' * 3, interval=0.35)
        pyautogui.typewrite('\nFim do programa! Volte sempre!', interval=0.10)
# mensagem de erro caso o usuário digite algo diferente de 1, 2 ou 3        
    else:
        pyautogui.typewrite('\033[34mOpção invalida! Tente novamente.', interval=0.10)
