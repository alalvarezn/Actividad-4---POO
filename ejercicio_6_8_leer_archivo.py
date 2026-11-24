import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class LeerArchivo:

    def __init__(self, nombre_archivo: str):
        self.__nombre_archivo = nombre_archivo

    def leer(self) -> str:
        with open(self.__nombre_archivo, "rb") as flujo_bytes:
            datos = flujo_bytes.read()
        return datos.decode("utf-8")


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.__campo_archivo = None
        self.__contenido = None
        self.__inicio()
        self.title("Leer archivo")
        self.resizable(False, False)

    def __inicio(self) -> None:
        superior = ttk.Frame(self, padding=10)
        superior.pack(fill="x")
        ttk.Label(superior, text="Nombre del archivo:").grid(row=0, column=0)
        self.__campo_archivo = ttk.Entry(superior, width=36)
        self.__campo_archivo.grid(row=0, column=1, padx=6)
        self.__campo_archivo.insert(0, "prueba.txt")
        ttk.Button(superior, text="Examinar...", command=self.__al_examinar).grid(
            row=0, column=2)
        ttk.Button(superior, text="Leer archivo", command=self.__al_leer).grid(
            row=0, column=3, padx=(6, 0))

        self.__contenido = tk.Text(self, width=70, height=14, state="disabled")
        self.__contenido.pack(padx=10, pady=(0, 10))

    def __al_examinar(self) -> None:
        ruta = filedialog.askopenfilename(parent=self,
                                          filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            self.__campo_archivo.delete(0, tk.END)
            self.__campo_archivo.insert(0, ruta)

    def __al_leer(self) -> None:
        archivo = LeerArchivo(self.__campo_archivo.get().strip())
        try:
            texto = archivo.leer()
        except (OSError, UnicodeDecodeError):
            messagebox.showerror("Error", "No se pudo leer el archivo.", parent=self)
            return
        self.__contenido.config(state="normal")
        self.__contenido.delete("1.0", tk.END)
        self.__contenido.insert(tk.END, texto)
        self.__contenido.config(state="disabled")


class Principal:

    @staticmethod
    def main() -> None:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()
