import tkinter as tk
import random

# Variables globales para puntajes
puntaje_jugador = 0
puntaje_computadora = 0

# Función principal para jugar
def jugar(eleccion_jugador):
    global puntaje_jugador, puntaje_computadora

    # Opciones disponibles
    opciones = ["Piedra", "Papel", "Tijera"]
    eleccion_computadora = random.choice(opciones)

    # Mostrar selección del jugador y la computadora
    lbl_eleccion_jugador.config(text=f"Tu elección: {eleccion_jugador}")
    lbl_eleccion_computadora.config(text=f"Computadora: {eleccion_computadora}")

    # Determinar el resultado
    if eleccion_jugador == eleccion_computadora:
        resultado = "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
        resultado = "Ganaste"
        puntaje_jugador += 1
    else:
        resultado = "Perdiste"
        puntaje_computadora += 1

    # Actualizar el resultado y puntajes
    lbl_resultado.config(text=f"Resultado: {resultado}", fg="blue" if resultado == "Ganaste" else "red")
    lbl_puntaje_jugador.config(text=f"Jugador: {puntaje_jugador}")
    lbl_puntaje_computadora.config(text=f"Computadora: {puntaje_computadora}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.configure(bg="#ececec")  # Fondo gris claro

# Título
lbl_titulo = tk.Label(ventana, text="Juego: Piedra, Papel o Tijera", font=("Arial", 18, "bold"), bg="#ececec", fg="#333")
lbl_titulo.pack(pady=10)

# Opciones del jugador
lbl_instrucciones = tk.Label(ventana, text="Selecciona una opción:", font=("Arial", 14), bg="#ececec", fg="#555")
lbl_instrucciones.pack(pady=10)

frame_botones = tk.Frame(ventana, bg="#ececec")
frame_botones.pack(pady=10)

# Botones con colores diferentes
btn_piedra = tk.Button(frame_botones, text="Piedra", font=("Arial", 12), bg="#ff9999", fg="#000", width=10, command=lambda: jugar("Piedra"))
btn_piedra.grid(row=0, column=0, padx=10, pady=5)

btn_papel = tk.Button(frame_botones, text="Papel", font=("Arial", 12), bg="#99ccff", fg="#000", width=10, command=lambda: jugar("Papel"))
btn_papel.grid(row=0, column=1, padx=10, pady=5)

btn_tijera = tk.Button(frame_botones, text="Tijera", font=("Arial", 12), bg="#99ff99", fg="#000", width=10, command=lambda: jugar("Tijera"))
btn_tijera.grid(row=0, column=2, padx=10, pady=5)

# Mostrar selección del jugador y la computadora
lbl_eleccion_jugador = tk.Label(ventana, text="Tu elección: ", font=("Arial", 12), bg="#ececec", fg="#333")
lbl_eleccion_jugador.pack(pady=5)

lbl_eleccion_computadora = tk.Label(ventana, text="Computadora: ", font=("Arial", 12), bg="#ececec", fg="#333")
lbl_eleccion_computadora.pack(pady=5)

# Mostrar resultado
lbl_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14, "bold"), bg="#ececec", fg="#333")
lbl_resultado.pack(pady=10)

# Contador de puntuación
lbl_puntajes = tk.Label(ventana, text="Puntajes", font=("Arial", 14, "bold"), bg="#ececec", fg="#555")
lbl_puntajes.pack(pady=10)

frame_puntajes = tk.Frame(ventana, bg="#ececec")
frame_puntajes.pack(pady=10)

lbl_puntaje_jugador = tk.Label(frame_puntajes, text="Jugador: 0", font=("Arial", 12), bg="#ececec", fg="#198754")
lbl_puntaje_jugador.grid(row=0, column=0, padx=20)

lbl_puntaje_computadora = tk.Label(frame_puntajes, text="Computadora: 0", font=("Arial", 12), bg="#ececec", fg="#dc3545")
lbl_puntaje_computadora.grid(row=0, column=1, padx=20)

# Ejecutar la ventana principal
ventana.mainloop()
