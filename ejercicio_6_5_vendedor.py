import tkinter as tk
from tkinter import messagebox, ttk


class Vendedor:

    def __init__(self, nombre: str, apellidos: str):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = 0

    def imprimir(self) -> str:
        return (f"Nombre del vendedor = {self.__nombre}\n"
                f"Apellidos del vendedor = {self.__apellidos}\n"
                f"Edad del vendedor = {self.__edad}")

    def verificar_edad(self, edad: int) -> None:
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.__edad = edad


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__campo_nombre = None
        self.__campo_apellidos = None
        self.__campo_edad = None
        self.__etiqueta_resultado = None
        self.__inicio()
        self.title("Vendedor")
        self.resizable(False, False)

    def __inicio(self) -> None:
        contenedor = ttk.LabelFrame(self, text="Datos del vendedor", padding=12)
        contenedor.pack(padx=12, pady=12)
        self.__campo_nombre = self.__crear_campo(contenedor, "Nombre:", 0)
        self.__campo_apellidos = self.__crear_campo(contenedor, "Apellidos:", 1)
        self.__campo_edad = self.__crear_campo(contenedor, "Edad:", 2)
        ttk.Button(contenedor, text="Registrar", command=self.__al_registrar).grid(
            row=3, column=0, columnspan=2, pady=10)
        self.__etiqueta_resultado = ttk.Label(contenedor, text="", justify="left")
        self.__etiqueta_resultado.grid(row=4, column=0, columnspan=2, sticky="w")

    @staticmethod
    def __crear_campo(padre: ttk.Frame, texto: str, fila: int) -> ttk.Entry:
        ttk.Label(padre, text=texto).grid(row=fila, column=0, sticky="w", pady=4)
        campo = ttk.Entry(padre, width=24)
        campo.grid(row=fila, column=1, padx=(10, 0), pady=4)
        return campo

    def __al_registrar(self) -> None:
        vendedor = Vendedor(self.__campo_nombre.get(), self.__campo_apellidos.get())
        try:
            edad = int(self.__campo_edad.get())
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.", parent=self)
            return
        try:
            vendedor.verificar_edad(edad)
        except ValueError as error:
            self.__etiqueta_resultado.config(text="")
            messagebox.showerror("Excepción", str(error), parent=self)
            return
        self.__etiqueta_resultado.config(text=vendedor.imprimir())


class Principal:

    @staticmethod
    def main() -> None:
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()
