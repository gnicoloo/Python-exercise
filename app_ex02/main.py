import customtkinter as ctk

# =========================
# Configurazione tema globale
# =========================
ctk.set_appearance_mode("dark")   # Tema scuro
ctk.set_default_color_theme("blue")  # Colore principale

# =========================
# Funzioni
# =========================
def calcola_sconto():
    """
    Legge il prezzo dall'entry, calcola lo sconto e aggiorna la label.
    """
    try:
        # Legge il testo e lo converte in float
        prezzo = float(entry_prezzo.get())

        # Calcolo sconto
        if prezzo > 100:
            prezzo_finale = prezzo * 0.8  # Sconto 20%
            messaggio = f"Sconto applicato! Totale: {prezzo_finale:.2f}€"
        else:
            messaggio = f"Nessun sconto. Totale: {prezzo:.2f}€"

        # Aggiorna la label del risultato
        label_risultato.configure(text=messaggio, text_color="yellow")

    except ValueError:
        # Se l'utente inserisce testo non numerico
        label_risultato.configure(text="Inserisci un numero valido!", text_color="red")


# =========================
# Creazione finestra principale
# =========================
app = ctk.CTk()
app.title("Calcolatore Sconti Pro")
app.geometry("400x350")

# =========================
# Widget GUI
# =========================
# Titolo
label_titolo = ctk.CTkLabel(
    app, 
    text="Gestore Cassa Moderno", 
    font=("Arial", 20, "bold")
)
label_titolo.pack(pady=20)

# Entry per prezzo
entry_prezzo = ctk.CTkEntry(
    app, 
    placeholder_text="Inserisci prezzo articolo..."
)
entry_prezzo.pack(pady=10)

# Bottone per calcolo
btn_calcola = ctk.CTkButton(
    app, 
    text="Applica Sconto", 
    command=calcola_sconto
)
btn_calcola.pack(pady=20)

# Label risultato
label_risultato = ctk.CTkLabel(
    app, 
    text="In attesa di dati...", 
    font=("Arial", 14)
)
label_risultato.pack(pady=20)

# =========================
# Avvio loop principale
# =========================
app.mainloop()

