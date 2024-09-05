# Autor: Jonathan Hernández
# Fecha: 04 Septiembre 2024
# Descripción: Código para una simulación de batalla Pokémon de estilo retro
# GitHub: https://github.com/Jona163

#Importacion de librerias 
import time
import numpy as np
import sys

# Función para imprimir con retraso
def delay_print(s):
    # Imprime un carácter a la vez
    # Referencia: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()  # Actualiza el buffer de salida inmediatamente
        time.sleep(0.05)  # Pausa de 0.05 segundos entre caracteres

# Crear la clase Pokémon
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # Guarda las variables como atributos de la clase
        self.name = name  # Nombre del Pokémon
        self.types = types  # Tipo de Pokémon (Fuego, Agua, Planta, etc.)
        self.moves = moves  # Movimientos del Pokémon
        self.attack = EVs['ATTACK']  # Valor de ataque
        self.defense = EVs['DEFENSE']  # Valor de defensa
        self.health = health  # Salud inicial representada con barras
        self.bars = 20  # Cantidad de barras de salud

    # Función para que los Pokémon se enfrenten en combate
    def fight(self, Pokemon2):
        # Permite que dos Pokémon peleen entre sí

        # Información del combate
        print("-----BATALLA POKÉMON-----")
        print(f"\n{self.name}")
        print("TIPO/", self.types)
        print("ATAQUE/", self.attack)
        print("DEFENSA/", self.defense)
        print("NIVEL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TIPO/", Pokemon2.types)
        print("ATAQUE/", Pokemon2.attack)
        print("DEFENSA/", Pokemon2.defense)
        print("NIVEL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Considera las ventajas de tipo
        version = ['Fire', 'Water', 'Grass']  # Lista de tipos para comparación
        for i,k in enumerate(version):
            if self.types == k:
                # Ambos Pokémon son del mismo tipo
                if Pokemon2.types == k:
                    string_1_attack = '\nNo es muy efectivo...'
                    string_2_attack = '\nNo es muy efectivo...'

                # Pokémon2 es fuerte contra el tipo de self
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nNo es muy efectivo...'
                    string_2_attack = '\n¡Es súper efectivo!'

                # Pokémon2 es débil contra el tipo de self
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\n¡Es súper efectivo!'
                    string_2_attack = '\nNo es muy efectivo...'

        # Comienza el combate real
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Imprime la salud de cada Pokémon
            print(f"\n{self.name}\t\tSALUD\t{self.health}")
            print(f"{Pokemon2.name}\t\tSALUD\t{Pokemon2.health}\n")

            print(f"¡Adelante {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)  # Muestra los movimientos disponibles
            index = int(input('Elige un movimiento: '))
            delay_print(f"\n{self.name} usó {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determina el daño
            Pokemon2.bars -= self.attack  # Reduce la salud del oponente
            Pokemon2.health = ""

            # Restaura las barras de salud con un pequeño impulso de defensa
            for j in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tSALUD\t{self.health}")
            print(f"{Pokemon2.name}\t\tSALUD\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Verifica si el Pokémon2 se ha debilitado
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' se ha debilitado.')
                break

            # Turno de Pokémon2
            print(f"¡Adelante {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)  # Muestra los movimientos disponibles
            index = int(input('Elige un movimiento: '))
            delay_print(f"\n{Pokemon2.name} usó {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determina el daño
            self.bars -= Pokemon2.attack  # Reduce la salud del Pokémon actual
            self.health = ""

            # Restaura las barras de salud con impulso de defensa
            for j in range(int(self.bars + 0.1 * self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tSALUD\t{self.health}")
            print(f"{Pokemon2.name}\t\tSALUD\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Verifica si el Pokémon actual se ha debilitado
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' se ha debilitado.')
                break

        # Recompensa monetaria al ganar la batalla
        money = np.random.choice(5000)
        delay_print(f"\nEl oponente te ha pagado ${money}.\n")


# Ejecución principal
if __name__ == '__main__':
    # Crear Pokémon
    Charizard = Pokemon('Charizard', 'Fire', ['Lanzallamas', 'Vuelo', 'Anillo Ígneo', 'Puño Fuego'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Pistola Agua', 'Hidrobomba', 'Surf', 'Acua Jet'], {'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Látigo Cepa', 'Hoja Afilada', 'Terremoto', 'Planta Feroz'], {'ATTACK':8, 'DEFENSE':12})

    # Iniciar una batalla
    Charizard.fight(Blastoise)
