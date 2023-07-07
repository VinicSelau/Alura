class Conta:
    #construtor
    def __init__(self) -> None:
        print("Construindo objeto... {}".format(self))
        self.numero = 123
        self.titular = "Vini"
        self.saldo = 59.0
        self.limite = 3000.0 