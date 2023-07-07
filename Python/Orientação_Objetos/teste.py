def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] = conta["saldo"] + valor
    return

def sacar(conta, valor):
    conta["saldo"] = conta["saldo"] - valor
    return  

def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))
    return