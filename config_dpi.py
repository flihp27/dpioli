/* Une touche sur mon clavier doit permettre d'augmenter le nombre de dpi de ma souris au maximum, soit de 4200.
Je veux pouvoir utiliser la même touche du clavier qui a permit d'augmenter les dpi au maximum pour remettre le nombre de dpi par défault de ma souris, soit de 1800.
L'exécution du code doit se faire sous windows 11.
Il faut un interface graphique qui permet de configurer et de lier la touche du clavier que l'utilisateur désire utiliser pour modifier le nombre de dpi. 
L'application doit pouvoir s'exécuter pendant l'utilisation d'un jeu vidéo. */

import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import ctypes

# Constantes pour les DPI
DPI_MAX = 4200
DPI_DEFAULT = 1800

# Variables globales
current_dpi = DPI_DEFAULT
selected_key = None

# Fonction pour changer les DPI de la souris
def set_mouse_dpi(dpi):
    ctypes.windll.user32.SystemParametersInfoW(113, 0, dpi, 0)

# Fonction pour gérer la pression de la touche configurée
def on_press(key):
    global current_dpi
    try:
        if key.char == selected_key:
            if current_dpi == DPI_DEFAULT:
                set_mouse_dpi(DPI_MAX)
                current_dpi = DPI_MAX
            else:
                set_mouse_dpi(DPI_DEFAULT)
                current_dpi = DPI_DEFAULT
    except AttributeError:
        pass

# Fonction pour configurer la touche
def configure_key():
    global selected_key
    selected_key = key_entry.get()
    if selected_key:
        messagebox.showinfo("Configuration", f"Touche configurée: {selected_key}")
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer une touche valide.")

# Création de l'interface graphique
root = tk.Tk()
root.title("Configuration de la touche DPI")

tk.Label(root, text="Entrez la touche du clavier:").pack(pady=10)
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

tk.Button(root, text="Configurer", command=configure_key).pack(pady=10)

# Démarrage de l'écouteur de touches
listener = keyboard.Listener(on_press=on_press)
listener.start()

root.mainloop()