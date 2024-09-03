import tkinter as tk
from tkinter import messagebox


# Clase CuentaBancaria para manejar el cálculo de intereses
class CuentaBancaria:
    def __init__(self, saldo_inicial, tasa_interes, tiempo):
        self.saldo_inicial = saldo_inicial
        self.tasa_interes = tasa_interes
        self.tiempo = tiempo

    def calcular_interes(self):
        # Cálculo de interés simple
        interes = self.saldo_inicial * (self.tasa_interes / 100) * self.tiempo
        saldo_final = self.saldo_inicial + interes
        return interes, saldo_final


# Clase para manejar la interfaz gráfica
class InterfazCuentaBancaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Multifuncional")

        # Botón para seleccionar la funcionalidad de cálculo de intereses
        tk.Button(root, text="Calcular Interés Bancario", command=self.mostrar_interes).grid(row=0, column=0)
        # Botón para seleccionar la funcionalidad de ordenar números
        tk.Button(root, text="Ordenar Números", command=self.mostrar_ordenar_numeros).grid(row=0, column=1)

        # Frame para calcular intereses
        self.interes_frame = tk.Frame(root)
        tk.Label(self.interes_frame, text="Saldo Inicial:").grid(row=0, column=0)
        tk.Label(self.interes_frame, text="Tasa de Interés (%):").grid(row=1, column=0)
        tk.Label(self.interes_frame, text="Tiempo (años):").grid(row=2, column=0)

        self.saldo_inicial = tk.Entry(self.interes_frame)
        self.tasa_interes = tk.Entry(self.interes_frame)
        self.tiempo = tk.Entry(self.interes_frame)

        self.saldo_inicial.grid(row=0, column=1)
        self.tasa_interes.grid(row=1, column=1)
        self.tiempo.grid(row=2, column=1)

        tk.Button(self.interes_frame, text="Calcular Interés", command=self.calcular_interes).grid(row=3, columnspan=2)

        self.resultado_interes = tk.Label(self.interes_frame, text="Interés: ")
        self.resultado_interes.grid(row=4, columnspan=2)

        self.resultado_saldo_final = tk.Label(self.interes_frame, text="Saldo Final: ")
        self.resultado_saldo_final.grid(row=5, columnspan=2)

        # Frame para ordenar números
        self.ordenar_frame = tk.Frame(root)
        tk.Label(self.ordenar_frame, text="Introduce el primer número:").grid(row=0, column=0)
        tk.Label(self.ordenar_frame, text="Introduce el segundo número:").grid(row=1, column=0)
        tk.Label(self.ordenar_frame, text="Introduce el tercer número:").grid(row=2, column=0)

        self.num1 = tk.Entry(self.ordenar_frame)
        self.num2 = tk.Entry(self.ordenar_frame)
        self.num3 = tk.Entry(self.ordenar_frame)

        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)
        self.num3.grid(row=2, column=1)

        tk.Button(self.ordenar_frame, text="Ordenar", command=self.ordenar_numeros).grid(row=3, columnspan=2)

        self.resultado_orden = tk.Label(self.ordenar_frame, text="Números ordenados: ")
        self.resultado_orden.grid(row=4, columnspan=2)

    def mostrar_interes(self):
        self.ordenar_frame.grid_forget()
        self.interes_frame.grid(row=1, columnspan=2)

    def mostrar_ordenar_numeros(self):
        self.interes_frame.grid_forget()
        self.ordenar_frame.grid(row=1, columnspan=2)

    def calcular_interes(self):
        try:
            saldo_inicial = float(self.saldo_inicial.get())
            tasa_interes = float(self.tasa_interes.get())
            tiempo = float(self.tiempo.get())

            cuenta = CuentaBancaria(saldo_inicial, tasa_interes, tiempo)

            interes, saldo_final = cuenta.calcular_interes()

            self.resultado_interes.config(text=f"Interés: ${interes:.2f}")
            self.resultado_saldo_final.config(text=f"Saldo Final: ${saldo_final:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def ordenar_numeros(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            num3 = float(self.num3.get())

            numeros = [num1, num2, num3]
            numeros.sort()

            self.resultado_orden.config(text=f"Números ordenados: {numeros}")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")


# Función principal para ejecutar el programa
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCuentaBancaria(root)
    root.mainloop()