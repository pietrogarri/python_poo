class Carro:
    modelo : str
    marca : str
    consumo = 0.0
    tanque = 0.0
    cor : str
    odometro = 0.0
    motor_on = False

    def __init__(self, modelo : str, marca : str, consumo : float, tanque : float, cor : str,
                       odometro : float, motor : bool):
        self.modelo = modelo
        self.marca = marca
        self.consumo = consumo
        self.tanque = tanque
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor

    def ligar(self):
        if not self.motor_on and self.tanque > 0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!, ou tanque vazio!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on and self.tanque > 0:
            km = velocidade * tempo
            litros = km/self.consumo
            if self.tanque >= litros:
                self.odometro += km
                self.tanque -= litros
            else:
                km = self.tanque * self.consumo
                self.odometro += km
                self.tanque = 0
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'tanque {self.tanque}, consumo medio {self.consumo} Km/L,'
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}')
        return info

