
#? units: length, time, pressure, weight, speed, frequency, data storage, data transfer, power, temperature, electric current
#? electrical resistance, electric potencial, electric capacitance, force

#? Version 0.1 alternativa: en esta version se va a intentar a hacer lo mismo que es hacer la interfaz solo que con POO 
import sys
DISTANCE = ("mm","cm","dm","m","dam","hm","km")
TIME = ("s","m","h")
VOLUME = ("ml","cl","dl","l","dal","hl","kl")
HEIGHT = ("mg","cg","dg","g","dag","hg","kg","","","t")

EXP = {"1": 10,"2":60,"3":10,"4":10 }
UNITS = {"1": DISTANCE,"2":TIME,"3":VOLUME,"4":HEIGHT}
TITLE = """\t → CONVERSOR DE UNIDADES ←\n"""
ELECTION = {"1":"distancia","2":"tiempo","3":"volumen","4":"peso"}
TIME_INTERFACE="""
→→ UNIDADES SOPORTADAS ←←
segundos →→→ s 
minutos  →→→ m
horas    →→→ h"""
DISTANCE_INTERFACE="""
→→ UNIDADES SOPORTADAS ←←
milimetros  →→→ mm
centimetros →→→ cm
decimetros  →→→ dm
metros      →→→ m
decametros  →→→ dam
hectometros →→→ hm
kilometros  →→→ km"""

VOLUME_INTERFACE = """
→→ UNIDADES SOPORTADAS ←←
mililitros  →→→ mL
centilitros →→→ cL
decilitros  →→→ dL
litros      →→→ L
decalitros  →→→ daL
hectolitros →→→ hL
kilolitros  →→→ kL"""

WEIGHT_INTERFACE = """
→→ UNIDADES SOPORTADAS ←←
mililitros  →→→ mg
centilitros →→→ cg
decilitros  →→→ dg
litros      →→→ g
decalitros  →→→ dag
hectolitros →→→ hg
kilolitros  →→→ kg
tonelada    →→→ t"""

INTERFACES ={"1":DISTANCE_INTERFACE, "2":TIME_INTERFACE, "3":VOLUME_INTERFACE,"4":WEIGHT_INTERFACE}
CHOICE_INTERFACE="""
ELIGE QUE TIPO DE UNIDAD QUIERES CONVERTIR

999→→→  SALIR

1  →→→  DISTANCIA
2  →→→  TIEMPO   
3  →→→  VOLUMEN
4  →→→  PESO
COLOCA EL NUMERO DE TU ELECCION AQUI →→ """

class Convertions:

    def interface(self):
        print(TITLE)
        print("Version: 0.1 beta")

    def data_recolect(self):
        self.exponent = input(CHOICE_INTERFACE)
        if self.exponent == "999":
            sys.exit()
        print(f"\nSeleccionaste {ELECTION[self.exponent]}\n")
        self.units = UNITS[self.exponent]
        self.value1 = input("Ingresa el valor 1: ")
        self.unit1 = input(f"""{INTERFACES[self.exponent]}
ingresa la unidad de tiempo del valor 1: """)
        self.unit2 = input("ingresa la unidad de tiempo del valor que se va a calcular: ")

    def operation(self):
        
        index1,index2=int(self.units.index(self.unit1)),int(self.units.index(self.unit2))
        if index1 < index2: #ver que unidad es mayor para saber si multiplicar y dividir, luego contar el numero de caracteres desde valor 1 a valor2 y luego
            oper = "div"

        elif index1 > index2:
            oper = "mul"   #segun ese numero es si es 10 o 100 etc
            index1 = (index1+1)*-1      # esta multiplicacion es para que no de error cuando sea mayor el 1er indice
            index2 = (index2+1)*-1
        else:
            print("error")

        exp = len(self.units[index1:index2])
        
        if oper == "div":
            result = float(self.value1) / (EXP[self.exponent] ** exp)

        elif oper == "mul":
            result = float(self.value1) * (EXP[self.exponent] ** exp)

        round_result = str(round(result,11))
        round_result = round_result.replace("e", "^")
        return round_result

    def exit(self):
        sys.exit()
    

distancia_prueba = Convertions()
distancia_prueba.interface()
distancia_prueba.data_recolect()
print(distancia_prueba.operation(),distancia_prueba.unit2)
def repeat_program():
    input("presiona enter para continuar")
    distancia_prueba = Convertions()
    distancia_prueba.interface()
    distancia_prueba.data_recolect()
    print(distancia_prueba.operation())
    repeat_program()
repeat_program()