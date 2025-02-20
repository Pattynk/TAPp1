import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Ventana")
ventana.geometry("300x200")  # Tamaño de la ventana

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, bienvenido a Tkinter!", font=("Arial", 12))

# Crear una caja de texto
entrada = tk.Entry(ventana, width=25)
entrada.pack(pady=5)

# Función cuando se presiona el botón
def mostrar_mensaje():
    texto = entrada.get()
    etiqueta.config(text=f"Hola, {texto}!")  # Cambia el texto de la etiqueta
     ventana.config(bg="lightblue")

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack(pady=10)

# Iniciar el bucle de la aplicación
ventana.mainloop()
