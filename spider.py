import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
from math import pi

# Funktion zum Erstellen und Speichern des Spider-Diagramms
def create_spider_chart(task_name, values, labels):
    N = len(labels)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Erstellen des Plots
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Werte und Füllung
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    
    # Achsenbeschriftungen
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    # Titel setzen
    plt.title(task_name)
    
    # Speichern des Plots im Downloads-Verzeichnis
    downloads_folder = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_folder, f"{task_name}_spider_chart.png")
    plt.savefig(file_path)
    plt.close()
    
    # Erfolgsmeldung
    messagebox.showinfo("Erfolg", f"Das Spider-Diagramm wurde unter '{file_path}' gespeichert.")

# Funktion zum Sammeln der Eingaben und Erstellen des Diagramms
def generate_chart():
    try:
        task_name = entry_task_name.get()
        automation = int(entry_automation.get())
        creativity = int(entry_creativity.get())
        decision_autonomy = int(entry_decision_autonomy.get())
        context_dependence = int(entry_context_dependence.get())

        if task_name == "":
            raise ValueError("Der Aufgabenname darf nicht leer sein.")
        
        # Prüfen, ob alle Werte zwischen 1 und 4 liegen
        values = [automation, creativity, decision_autonomy, context_dependence]
        if any(v < 1 or v > 4 for v in values):
            raise ValueError("Alle Werte müssen zwischen 1 und 4 liegen.")
        
        labels = ['Automatisierungsgrad', 'Kreativität', 'Entscheidungsautonomie', 'Kontextabhängigkeit']
        create_spider_chart(task_name, values, labels)
    
    except ValueError as e:
        messagebox.showerror("Fehler", str(e))

# GUI erstellen
root = tk.Tk()
root.title("Spider-Diagramm-Generator")

# Label und Eingabefelder für die Aufgabe und die vier Dimensionen
tk.Label(root, text="Name der Aufgabe:").pack()
entry_task_name = tk.Entry(root)
entry_task_name.pack()

tk.Label(root, text="Automatisierungsgrad (1-4):").pack()
entry_automation = tk.Entry(root)
entry_automation.pack()

tk.Label(root, text="Kreativität (1-4):").pack()
entry_creativity = tk.Entry(root)
entry_creativity.pack()

tk.Label(root, text="Entscheidungsautonomie (1-4):").pack()
entry_decision_autonomy = tk.Entry(root)
entry_decision_autonomy.pack()

tk.Label(root, text="Kontextabhängigkeit (1-4):").pack()
entry_context_dependence = tk.Entry(root)
entry_context_dependence.pack()

# Button zum Erstellen des Spider-Diagramms
button_generate = tk.Button(root, text="Spider-Diagramm erstellen", command=generate_chart)
button_generate.pack()

# Button zum Zurücksetzen der Eingabefelder für eine neue Aufgabe
def reset_fields():
    entry_task_name.delete(0, tk.END)
    entry_automation.delete(0, tk.END)
    entry_creativity.delete(0, tk.END)
    entry_decision_autonomy.delete(0, tk.END)
    entry_context_dependence.delete(0, tk.END)

button_reset = tk.Button(root, text="Neues Diagramm erstellen", command=reset_fields)
button_reset.pack()

# Start der GUI
root.mainloop()