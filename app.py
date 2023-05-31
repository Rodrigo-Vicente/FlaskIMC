
from tokenize import String
from flask import Flask
app = Flask(__name__)

@app.route("/")
def Resultado():
         peso = 50.0
         altura = 1.72
         imc = CalcularImc(peso,altura)
         if(imc):
                exibir = StatusIMC(imc)
                # return "O seu imc é:" + str(imc) + "Status: " + exibir
                return f"O seu imc é: {imc} , Status: {exibir}"
         else:
                return "Valor invalido"

def CalcularImc(peso, altura):
        validate = ValidateValues(peso, altura)
        if(validate):
                imcResultado = peso/(altura*altura)
                return imcResultado
        else:
                return False

def ValidateValues(peso, altura):
        if(peso >0 and altura > 0) :
                return True
        else:
                return False

def StatusIMC(imc):
        if(imc <= 18.5) :
                return ("Magreza")
        elif(imc > 18.5 and imc <= 24.9):
                return ("Normal")
        elif(imc > 25 and imc <= 29.9):
                return ("SOBREPESO")
        elif(imc > 30 and imc <= 39.9):
                return ("OBESIDADE")
        else:
                return ("OBESIDADE GRAVE")