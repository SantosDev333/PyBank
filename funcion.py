import customtkinter as ctk
from time import sleep
from colorama import init, Fore   # type: ignore
init(autoreset=True)


def deposito(total):
    print('-='*15)
    print('Depósito'.center(30, '-'))
    print('-='*15, '\n')

    money = total

    try:
        quant = float(input('Quanto deseja depósitar R$: '))
        print('')
    except:
        print('##'*15)
        print(f'{Fore.LIGHTYELLOW_EX}Algo deu errado.{Fore.LIGHTWHITE_EX}'.center(40, '='))
        sleep(1)
        print(f'{Fore.LIGHTYELLOW_EX}Reiniciando o sistema...{Fore.LIGHTWHITE_EX}'.center(40, '='))
        print('##'*15, '\n')
        return total

    if quant > 0:
        money += quant
        print('##'*15)
        print(f'{Fore.LIGHTGREEN_EX}Depósito aprovado.{Fore.LIGHTWHITE_EX}'.center(40, '='))
        print('##'*15, '\n')

        Lista = [money, quant]

        return Lista
    else:
        print('##'*22)
        print(f'{Fore.LIGHTRED_EX}Não é permitido números negativos ou nulo.{Fore.LIGHTWHITE_EX}'.center(52, '='))
        print('##'*22, '\n')
        return total


def saque(quant, saldo):
    print('-='*15)
    print('Saque'.center(30, '-'))
    print('-='*15,'\n')

    menos_quant = quant 
    money = saldo

    if quant != 0:
        print('Valor max de saque: R$500.00')
        try:
            valor = float(input('Quanto deseja sacar R$: '))
            print('')
        except:
            print('##'*15)
            print(f'{Fore.LIGHTYELLOW_EX}Algo deu errado.{Fore.LIGHTWHITE_EX}'.center(40, '='))
            print(f'{Fore.LIGHTYELLOW_EX}Reiniciando o sistema...{Fore.LIGHTWHITE_EX}'.center(40, '='))
            print('##'*15, '\n')
            lista = [money, menos_quant]
            return lista
        
        if saldo < valor:
            print('##'*25)
            print(f'Seu saldo atual é de R${saldo:.2f} não é possivel sacar R${valor:.2f}')
            print('##'*25, '\n')
            lista = [money, menos_quant]
            return lista
        elif valor > 500:
            print('Não é permitido saquar mais de R$500.00.')
            lista = [money, menos_quant]
            return lista
        else:
            print('##'*15)
            print('Saque executado com sucesso.')
            print(f'R${valor} extraido.')
            print('##'*15, '\n')
            
            menos_quant -= 1
            money -= valor
            lista = [money, menos_quant, valor]
            return lista
    else:
        print('##'*25)
        print('Seu limite de saques diarios foi atingida, tente novamente amanhã.')
        print('##'*25, '\n')
        lista = [money, menos_quant]
        return lista


def extrato(list, cash):
    print('-='*15)
    print('Extrato'.center(30, '-'))
    print('-='*15,'\n')

    for i, v in enumerate(list):
        if v['ação'] == 'Depósito':
            print(f'{i+1}. {v["ação"]} - R${v["valor"]:.2f}')
        elif v['ação'] == 'Saque':
            print(f'{i+1}. {v["ação"]}    - R$-{v["valor"]:.2f}') 

    print()
    print(f'Total na conta R${cash:.2f}')


def app_deposito(app):
    deposito_Title = ctk.CTkLabel( #Titulo
        app,
        text='Bank Mahho'.center(30, '-'), 
        font=ctk.CTkFont(family='Arial', size=25)
    )
    deposito_Title.pack( #apli Titulo
        side='bottom',
        pady=30
    )
    