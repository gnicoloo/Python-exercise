import customtkinter as ctk
# 1. Configurazione per Mac (quella che abbiamo appena visto)
ctk.set_appearance_mode("dark")

def pulsante_cliccato():
 # Questa funzione viene eseguita quando clicchiamo
 nome = campo_testo.get() # Prende il testo scritto dall'utente
 label_risultato.configure(text=f"Ciao {nome}, benvenuto!")

app = ctk.CTk()
app.geometry("400x300")
app.title("Strumento Interattivo")

# Aggiungiamo un titolo
titolo = ctk.CTkLabel(app, text="Inserisci il tuo nome:", font=("Arial", 16))
titolo.pack(pady=10)

# Aggiungiamo un campo di input (dove l'utente scrive)
campo_testo = ctk.CTkEntry(app, placeholder_text="Scrivi qui...")
campo_testo.pack(pady=10)

# Aggiungiamo il bottone
bottone = ctk.CTkButton(app, text="Saluta!", command=pulsante_cliccato)
bottone.pack(pady=10)