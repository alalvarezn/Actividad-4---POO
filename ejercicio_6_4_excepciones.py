import tkinter as tk
from tkinter import ttk


class PruebaExcepciones:

    @staticmethod
    def ejecutar() -> list:
        mensajes = []
        try:
            mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0
            mensajes.append("Después de la división")
        except ArithmeticError:
            mensajes.append("División por cero")
        finally:
            mensajes.append("Ingresando al primer finally")

        try:
            mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.upper()
            mensajes.append("Imprimiendo objeto")
        except ArithmeticError:
            mensajes.append("División por cero")
        except Exception:
            mensajes.append("Ocurrió una excepción")
        finally:
            mensajes.append("Ingresando al segundo finally")
        return mensajes


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__salida = None
        self.__inicio()
        self.title("Prueba de excepciones")
        self.resizable(False, False)

    def __inicio(self) -> None:
        contenedor = ttk.LabelFrame(self, text="try / except / finally", padding=12)
        contenedor.pack(padx=12, pady=12)
        botones = ttk.Frame(contenedor)
        botones.pack(pady=(0, 8))
        ttk.Button(botones, text="Ejecutar", command=self.__al_ejecutar).grid(
            row=0, column=0, padx=(0, 8))
        ttk.Button(botones, text="Limpiar", command=self.__al_limpiar).grid(row=0, column=1)
        self.__salida = tk.Text(contenedor, width=40, height=7, state="disabled")
        self.__salida.pack()

    def __al_ejecutar(self) -> None:
        mensajes = PruebaExcepciones.ejecutar()
        self.__salida.config(state="normal")
        self.__salida.delete("1.0", tk.END)
        self.__salida.insert(tk.END, "\n".join(mensajes))
        self.__salida.config(state="disabled")

    def __al_limpiar(self) -> None:
        self.__salida.config(state="normal")
        self.__salida.delete("1.0", tk.END)
        self.__salida.config(state="disabled")


class Principal:

    @staticmethod
    def main() -> None:
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()
