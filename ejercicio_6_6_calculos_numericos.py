import math
import tkinter as tk
from tkinter import ttk


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor: float) -> float:
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo "
                                  "para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> float:
        if valor < 0:
            raise ArithmeticError("El valor debe ser un número positivo "
                                  "para calcular la raíz cuadrada.")
        return math.sqrt(valor)


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__campo_valor = None
        self.__etiqueta_logaritmo = None
        self.__etiqueta_raiz = None
        self.__inicio()
        self.title("Cálculos numéricos")
        self.resizable(False, False)

    def __inicio(self) -> None:
        contenedor = ttk.LabelFrame(self, text="Cálculos numéricos", padding=12)
        contenedor.pack(padx=12, pady=12)
        ttk.Label(contenedor, text="Valor numérico:").grid(row=0, column=0, sticky="w")
        self.__campo_valor = ttk.Entry(contenedor, width=18)
        self.__campo_valor.grid(row=0, column=1, padx=(10, 0))
        ttk.Button(contenedor, text="Calcular", command=self.__al_calcular).grid(
            row=1, column=0, columnspan=2, pady=10)
        self.__etiqueta_logaritmo = ttk.Label(contenedor, text="", wraplength=320)
        self.__etiqueta_logaritmo.grid(row=2, column=0, columnspan=2, sticky="w", pady=2)
        self.__etiqueta_raiz = ttk.Label(contenedor, text="", wraplength=320)
        self.__etiqueta_raiz.grid(row=3, column=0, columnspan=2, sticky="w", pady=2)

    def __al_calcular(self) -> None:
        texto = self.__campo_valor.get().replace(",", ".")
        operaciones = [
            (self.__etiqueta_logaritmo, "Logaritmo neperiano",
             CalculosNumericos.calcular_logaritmo_neperiano),
            (self.__etiqueta_raiz, "Raíz cuadrada", CalculosNumericos.calcular_raiz_cuadrada),
        ]
        for etiqueta, nombre, metodo in operaciones:
            try:
                resultado = metodo(float(texto))
                etiqueta.config(text=f"{nombre} = {resultado:.4f}", foreground="black")
            except ValueError:
                etiqueta.config(text=f"{nombre}: el valor debe ser numérico.",
                                foreground="red")
            except ArithmeticError as error:
                etiqueta.config(text=f"{nombre}: {error}", foreground="red")


class Principal:

    @staticmethod
    def main() -> None:
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()
