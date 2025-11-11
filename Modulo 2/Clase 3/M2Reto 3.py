# --- Clase Padre ---
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        self._encendido = False  # atributo protegido

    # Métodos públicos
    def arrancar(self):
        if not self._encendido:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El vehículo ya estaba en marcha.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El vehículo ya estaba apagado.")

    def get_kilometraje(self):  # Getter
        return self.kilometraje

    def mostrar_info_base(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.anio}")


# --- Clase Hija: Coche ---
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def conducir(self, km):
        if self._encendido:  # Accede al atributo protegido del padre
            self.kilometraje += km
            print(f"Conduciendo {km} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir.")


# --- Clase Hija: Camion ---
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0  # atributo privado

    # Setters y Getters
    def cargar(self, kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print("Carga exitosa.")
        else:
            print("Error: Sobrecarga.")

    def descargar(self, kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
            print("Descarga completada.")
        else:
            print("Error: No puedes descargar más de lo que hay cargado.")

    def get_carga_actual(self):  # Getter
        return self.__carga_actual_kg


# --- Código Principal (Pruebas) ---
print("\n--- Prueba del Coche ---")
mi_coche = Coche("Toyota", "Corolla", 2020, 4)
mi_coche.conducir(100)         # debe fallar
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()
print(f"Kilometraje final: {mi_coche.get_kilometraje()} km")

print("\n--- Prueba del Camión ---")
mi_camion = Camion("Volvo", "FH16", 2022, 5000)
mi_camion.cargar(3000)
mi_camion.cargar(3000)          # debe fallar (sobrecarga)
mi_camion.descargar(1000)
print(f"Carga actual: {mi_camion.get_carga_actual()} kg")
