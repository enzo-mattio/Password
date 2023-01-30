from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import hashlib
import json

voir_ident = False

input = ""
car_spécial = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",  "[", "]", "|", ":", ";", "-", "_", "+", "=", "{", "}", "<", ">", ",", ".", "?"]

NOIR = "#1A1A1A"
GRIS = ""
VERT_BRUUU = "#436D35"
VERT_BRUUU_CLAIR = "#799C65"

 
with open ("mdp.json", "r") as fichier:
  stock = json.load(fichier)

master = Tk()
master.title("Crypteur de mot de passe")
master.geometry("400x400")
master.resizable(False, False)
master.config()
zomb = PhotoImage(file="BRUUUU.png")
output = StringVar()
json_mdp = StringVar()
id_liste = Listbox()

label1 = Label(master, i=zomb)
label1.pack()
label1.place(
  x = 0,
  y = 0, 

  height=400,
  width=400
  )

# Fonction qui permet de vérifier les conditions qu'on veut pour le mot de passe.

def verif_password(mot_de_passe):
  
  global car_spécial, attest_mdp
  
  contient_minuscule = False
  contient_majuscule = False
  contient_chiffre = False
  contient_special = False
  
  if len(mot_de_passe) >= 8:
    for caractère in mot_de_passe:
      if caractère.islower():
        contient_minuscule = True
      if caractère.isupper():
        contient_majuscule = True
      if caractère.isdigit():
        contient_chiffre = True
      if caractère in car_spécial:
        contient_special = True
  else:
    return False
  
  print(contient_special)
  print(contient_chiffre)
  print(contient_majuscule)
  print(contient_minuscule)
  
  if contient_chiffre == True and contient_majuscule == True and contient_minuscule == True and contient_special == True:
    output.set("Mot de passe valide")
    return True
  else:
    output.set("Vérifier le mot de passe")
    return False
   
# print(verif_password("zdvhjbvzeion"))

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

  
def add():
  
  mdp = motdepasse.get()
  identifiants = identifiant.get()
  passw = hash_pass(mdp)
  if not verif_password(mdp):
    messagebox.showerror("Invalide",
      "Mot de passe invalide, Il doit contenir au minimum 8 carctères avec 1 majuscules, 1 Minuscules, 1 Chiffre et 1 caractère spécial.")
    return
  
  
  if identifiants not in [i for i in stock] and passw not in [stock[i] for i in stock]:
    stock[identifiants]=passw
    with open("mdp.json", 'w') as fichier:
      json.dump(stock, fichier, indent=4)
    messagebox.showinfo("Réussi",
    "Pseudo et Mot de passe, sauvegardé")
  else:
    messagebox.showerror("Utilisé",
    "Username et/ou password déjà utilisé.")


  with open("mdp.json", "w") as fichier:
    json.dump(stock, fichier)



def Voir():
  global voir_ident, ident, id_liste

  
  if voir_ident:
    id_liste.destroy()
    voir_ident = False
  else:
    id_liste = Listbox(master, fg="black", bg="light gray")
    id_liste.place(x=0, y=250, width=400, height=150)

    for key, value in stock.items():
        id_liste.insert(END, "Pseudo : " + key ) 
        id_liste.insert(END, "Mot de passe : " + value )
    voir_ident = True  

def on_clear():
  
  for i in stock:
    stock.pop(i)
  with open("mdp.json", "w") as fichier:
    json.dump(stock, fichier)
  
  id_liste.delete(0, END)

identifiant = ctk.CTkEntry(
  master,
  border_color = NOIR,
  corner_radius= 2,
  text_color= NOIR,
  fg_color="transparent",
  justify=CENTER,
  font=("arial", 20),
)

identifiant.place(
  x= 50,
  y= 50,
  width= 300,
  height= 50,
)



motdepasse = ctk.CTkEntry(
  master,
  border_color = NOIR,
  corner_radius= 2,
  text_color= NOIR,
  fg_color="transparent",
  justify=CENTER,
  font=("arial", 20),
)

motdepasse.place(
  x= 50,
  y= 100,
  width= 300,
  height= 50,
)

bouton_clear = ctk.CTkButton(
  master,
  corner_radius=2,
  fg_color=NOIR,
  text="Effacer dernier ID",
  command = on_clear
)
bouton_clear.place(
  x=100, 
  y=0, 
  height=50,
  width=200
)

bouton_envoie_mdp = ctk.CTkButton(
  master,
  corner_radius=2,
  fg_color=NOIR,
  text="Entrer",
  command = add
)

bouton_envoie_mdp.place(
  x=50, 
  y=200, 
  height=50,
  width=100
)

bouton_voir_mdp = ctk.CTkButton(
  master,
  corner_radius=2,
  fg_color=NOIR,
  text="Voir MDP",
  command=Voir
)

bouton_voir_mdp.place(
  x=250,
  y=200,
  height=50,
  width=100
)

texte_mdp = ctk.CTkLabel(
  master,
  text_color=NOIR,
  textvariable=output,
  fg_color=VERT_BRUUU_CLAIR,
  justify=CENTER
)
texte_mdp.place(
  x=100,
  y=300,
  height=50,
  width=200
)


master.mainloop()