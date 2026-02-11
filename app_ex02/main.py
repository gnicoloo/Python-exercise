import customtkinter as ctk
# Configurazione iniziale
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



def calcola_sconto():
   # Preleviamo i dati dagli strumenti di input
   prezzo = float(entry_prezzo.get())
  
   if prezzo > 100:
       prezzo_finale = prezzo * 0.8  # Sconto 20%
       messaggio = f"Sconto applicato! Totale: {prezzo_finale}€"
   else:
       messaggio ="Nessun sconto. Totale: {prezzo}€"
  
   # Aggiorniamo l'etichetta del risultato
   label_risultato.configure(text=messaggio, text_color="yellow")


app = ctk.CTk()
app.title("Calcolatore Sconti Pro")
app.geometry("400x350")

# Elementi Grafici
ctk.CTkLabel(app, text="Gestore Cassa Moderno", font=("Arial", 20, "bold")).pack(pady=20)
entry_prezzo = ctk.CTkEntry(app, placeholder_text="Inserisci prezzo articolo...")
entry_prezzo.pack(pady = 10)
btn_calcola = ctk.CTkButton(app, text="Applica Sconto", command=calcola_sconto)
btn_calcola.pack(pady=20)
label_risultato = ctk.CTkLabel(app, text="In attesa di dati...", font=("Arial", 14))
label_risultato.pack(pady=20)
app.mainloop()