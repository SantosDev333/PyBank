from time import sleep
import funcion
import os

Ext = {}
Extrato = []

saques = 3
cash = 0.00


while True:

    os.system('cls')

    print('Bank Mahho'.center(30, '-'), '\n')

    print('[1] Depósito')
    print('[2] Saque')
    print('[3] Extrato')

    try:
        op = int(input('Escolha uma opção: '))
    except:
        print('Algo deu errado.')
        sleep(1)
        print('Reiniciando...')
        sleep(4)
        continue

    match op:
        case 1:
            valores = funcion.deposito(cash)
            cash = valores[0]
            Ext['ação'] = 'Depósito'
            Ext['valor'] = valores[1]
            Extrato.append(Ext.copy())
            Ext.clear()
            sleep(2)
        case 2:
            valores = funcion.saque(saques, cash)
            cash = valores[0]
            saques = valores[1]
            Ext['ação'] = 'Saque'
            Ext['valor'] = valores[2]
            Extrato.append(Ext.copy())
            Ext.clear()
            sleep(4)
        case 3:
            funcion.extrato(Extrato, cash)
            input('"Press Enter"')
