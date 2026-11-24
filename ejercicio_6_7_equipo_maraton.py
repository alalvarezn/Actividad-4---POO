import tkinter as tk
from tkinter import messagebox, ttk


class Programador:

    def __init__(self, nombre: str, apellidos: str):
        self.__nombre = nombre
        self.__apellidos = apellidos

    def get_nombre(self) -> str:
        return self.__nombre

    def get_apellidos(self) -> str:
        return self.__apellidos


class EquipoMaratonProgramacion:

    TAMANO_MAXIMO = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.__nombre_equipo = nombre_equipo
        self.__universidad = universidad
        self.__lenguaje_programacion = lenguaje_programacion
        self.__programadores = []

    def get_nombre_equipo(self) -> str:
        return self.__nombre_equipo

    def get_tamano_equipo(self) -> int:
        return len(self.__programadores)

    def esta_lleno(self) -> bool:
        return len(self.__programadores) == EquipoMaratonProgramacion.TAMANO_MAXIMO

    def anadir(self, programador: Programador) -> None:
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.__programadores.append(programador)

    @staticmethod
    def validar_campo(campo: str) -> None:
        if campo.strip() == "":
            raise ValueError("El campo no puede estar vacío.")
        for caracter in campo:
            if caracter.isdigit():
                raise ValueError("El nombre no puede tener dígitos.")
        if len(campo) >= 20:
            raise ValueError("La longitud debe ser menor a 20 caracteres.")


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__equipo = None
        self.__campo_equipo = None
        self.__campo_universidad = None
        self.__campo_lenguaje = None
        self.__campo_nombre = None
        self.__campo_apellidos = None
        self.__etiqueta_equipo = None
        self.__lista = None
        self.__inicio()
        self.title("Equipo maratón de programación")
        self.resizable(False, False)

    def __inicio(self) -> None:
        datos_equipo = ttk.LabelFrame(self, text="Datos del equipo", padding=10)
        datos_equipo.pack(fill="x", padx=12, pady=(12, 6))
        self.__campo_equipo = self.__crear_campo(datos_equipo, "Nombre del equipo:", 0)
        self.__campo_universidad = self.__crear_campo(datos_equipo, "Universidad:", 1)
        self.__campo_lenguaje = self.__crear_campo(datos_equipo, "Lenguaje:", 2)
        ttk.Button(datos_equipo, text="Crear equipo", command=self.__al_crear_equipo).grid(
            row=3, column=0, columnspan=2, pady=(8, 0))

        datos_programador = ttk.LabelFrame(self, text="Datos del programador", padding=10)
        datos_programador.pack(fill="x", padx=12, pady=6)
        self.__campo_nombre = self.__crear_campo(datos_programador, "Nombre:", 0)
        self.__campo_apellidos = self.__crear_campo(datos_programador, "Apellidos:", 1)
        ttk.Button(datos_programador, text="Añadir programador",
                   command=self.__al_anadir).grid(row=2, column=0, columnspan=2, pady=(8, 0))

        self.__etiqueta_equipo = ttk.Label(self, text="Aún no se ha creado el equipo.")
        self.__etiqueta_equipo.pack(anchor="w", padx=12)
        self.__lista = tk.Listbox(self, height=3)
        self.__lista.pack(fill="x", padx=12, pady=(4, 12))

    @staticmethod
    def __crear_campo(padre: ttk.Frame, texto: str, fila: int) -> ttk.Entry:
        ttk.Label(padre, text=texto).grid(row=fila, column=0, sticky="w", pady=3)
        campo = ttk.Entry(padre, width=26)
        campo.grid(row=fila, column=1, padx=(10, 0), pady=3)
        return campo

    def __al_crear_equipo(self) -> None:
        nombre = self.__campo_equipo.get().strip()
        universidad = self.__campo_universidad.get().strip()
        lenguaje = self.__campo_lenguaje.get().strip()
        if nombre == "" or universidad == "" or lenguaje == "":
            messagebox.showwarning("Datos incompletos", "Ingrese todos los datos del equipo.",
                                   parent=self)
            return
        self.__equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
        self.__lista.delete(0, tk.END)
        self.__etiqueta_equipo.config(text=f"Equipo: {nombre} (0 de 3 integrantes)")

    def __al_anadir(self) -> None:
        if self.__equipo is None:
            messagebox.showwarning("Equipo", "Primero debe crear el equipo.", parent=self)
            return
        nombre = self.__campo_nombre.get().strip()
        apellidos = self.__campo_apellidos.get().strip()
        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            self.__equipo.anadir(Programador(nombre, apellidos))
        except ValueError as error:
            messagebox.showerror("Error de validación", str(error), parent=self)
            return
        except Exception as error:
            messagebox.showerror("Equipo completo", str(error), parent=self)
            return
        self.__lista.insert(tk.END, f"{nombre} {apellidos}")
        self.__campo_nombre.delete(0, tk.END)
        self.__campo_apellidos.delete(0, tk.END)
        self.__etiqueta_equipo.config(
            text=f"Equipo: {self.__equipo.get_nombre_equipo()} "
                 f"({self.__equipo.get_tamano_equipo()} de 3 integrantes)")


class Principal:

    @staticmethod
    def main() -> None:
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()
