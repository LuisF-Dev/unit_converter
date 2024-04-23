import os
from time import sleep
try:
    from colorama import init, Fore

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
    print("Error: Porvafor instale las dependencias !!!")

### Initialization of colorama ###
init(autoreset=True)

### Unit measurement constants ###
DISTANCE = ("mm","cm","dm","m","dam","hm","km")
TIME = ("s","m","h")
VOLUME = ("ml","cl","dl","l","dal","hl","kl")
HEIGHT = ("mg","cg","dg","g","dag","hg","kg","","","t")

EXP = {"1": 10,"2":60,"3":10,"4":10 }
UNITS = {"1": DISTANCE,"2":TIME,"3":VOLUME,"4":HEIGHT}
ELECTION = {"1":"distancia","2":"tiempo","3":"volumen","4":"peso"}

""" Variables of colors """
magenta = [Fore.MAGENTA, Fore.RESET]    ## For sms             
green = [Fore.GREEN, Fore.RESET]        ## For titles           
cyan = [Fore.CYAN, Fore.RESET]          ## For menu options
blue = [Fore.BLUE, Fore.RESET]          ## For entry user
red = [Fore.RED, Fore.RESET]            ## For error about app

"""
open_file: Utiliza "with open()" para abrir un archivo txt de la 
carpeta interface en modo lectura, "r - read", la ruta del archivo es 
obtenida como  arguemto en la variable "path_file".La funcion retora el
contenido de los archivo, "Las interfazces". Luego de ello, cierras los
archivos. En caso de no encontrar el archivo, la funcion retorna un mensaje
de error.
"""
def open_file(path_file):

    try:
        with open(path_file, 'r') as text_interface:
            interface = text_interface.read()
        
        return interface
    
    except FileNotFoundError:
        return "Error: Archivo no encontrado !!!"

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')


### Files of interface ###
time_interface = open_file('interfaces/TIME_INTERFACE.txt')
distance_interface = open_file('interfaces/DISTANCE_INTERFACE.txt')
volumen_interface = open_file('interfaces/VOLUMEN_INTERFACE.txt')
weight_interface = open_file('interfaces/WEIGHT_INTERFACE.txt')
main_interface = open_file('interfaces/MAIN_INTERFACE.txt')

INTERFACES = {
    "1":distance_interface,
    "2":time_interface,
    "3":volumen_interface,
    "4":weight_interface
    }


class Convertions:

    def interface(self):
        clear_screen()

        add_color_interface = main_interface.format(
            ### Title of app ###
            green[0], green[1],
            
            ### Sms for user###
            magenta[0], magenta[1],

            ### Color for menu options main ###
            cyan[0], cyan[1],

            ### Input options for user ###
            blue[0], blue[1]

            )
        
        interface = add_color_interface

        return interface


    def data_recolect(self):

        try:
            self.exponent = input(self.interface())

            if self.exponent == "5":

                print(f"{magenta[0]} Gracias por usar la app !!{magenta[1]}")
                sleep(1)
                exit()
            
            else:

                print(f"\nSeleccionaste {ELECTION[self.exponent]}\n")
        
                self.units = UNITS[self.exponent]
                self.num_value = input("Ingresa el valor 1: ")
                self.origin_unit = input(f"""{INTERFACES[self.exponent]}                                                  
        ingresa la unidad de tiempo del valor 1: """)
                self.unit2 = input("ingresa la unidad de tiempo del valor que se va a calcular: ")

        except ValueError:
            print(f"{red[0]}Error: Caracter invalido !!!{red[1]}")
            input("Enter para continuar")
            self.data_recolect()
        
        except KeyError:
            print(f"{red[0]}Error: Opcion invalida !!!{red[1]}")
            input("Enter para continuar")
            self.data_recolect()

    def operation(self):
        
        ### SI recive ints debe tener un sitema de errores para no detener el programa
        index1,index2=int(self.units.index(self.origin_unit)),int(self.units.index(self.unit2))
        
        """
        #ver que unidad es mayor para saber si multiplicar y dividir, luego contar 
        # el numero de caracteres desde valor 1 a valor2 y luego
        """
        if index1 < index2: 
            oper = "div"

        elif index1 > index2:
            oper = "mul"   #segun ese numero es si es 10 o 100 etc (Ser mas espeficico)
            index1 = (index1+1)*-1 # esta multiplicacion es para que no de error cuando sea mayor el 1er indice
            index2 = (index2+1)*-1

        else:
            print("error") # Explicar cual ha sido el error

        exp = len(self.units[index1:index2]) 
        
        if oper == "div":
            result = float(self.num_value) / (EXP[self.exponent] ** exp)

        elif oper == "mul":
            result = float(self.num_value) * (EXP[self.exponent] ** exp)

        round_result = str(round(result,11))
        round_result = round_result.replace("e", "^")
        return round_result



distancia_prueba = Convertions()

distancia_prueba.interface()

distancia_prueba.data_recolect()

print(distancia_prueba.operation(),distancia_prueba.unit2)


### Funcion con recursividad ###
def repeat_program():

    input("presiona enter para continuar")

    distancia_prueba = Convertions()

    distancia_prueba.interface()

    distancia_prueba.data_recolect()

    print(distancia_prueba.operation())

    repeat_program()

repeat_program()