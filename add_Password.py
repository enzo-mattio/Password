import tkinter as tk
from tkinter import *
import customtkinter as ctk
import random

input = ""
car_spécial = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",  "[", "]", "|", ":", ";", "-", "_", "+", "=", "{", "}", "<", ">", ",", ".", "?"]

NOIR = "#1A1A1A"
GRIS = ""
VERT_BRUUU = "#436D35"
VERT_BRUUU_CLAIR = "#799C65"

attest_mdp = ""


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
  
  if contient_chiffre == True and contient_majuscule == True and contient_minuscule == True and contient_special == True:
    attest_mdp = "Mot de passe valide"
   
  print(contient_special)
  print(contient_chiffre)
  print(contient_majuscule)
  print(contient_minuscule)
  
  
  
def add():
  password = motdepasse.get()
  verif_password(password)
  
  
# print(verif_password("zdvhjbvzeion"))
master = Tk()
master.title("Crypteur de mot de passe")
master.geometry("400x400")
master.config(
  bg= VERT_BRUUU
)


bg = PhotoImage(file="BRUUUU.png")
label1 = Label( 
  master, 
  image = bg
  )
label1.place(
  x = 0,
  y = 0, 
  height=400,
  width=400
  )



motdepasse = ctk.CTkEntry(
  master,
  border_color = NOIR,
  corner_radius= 15,
  text_color= NOIR,
  fg_color="transparent",
  justify=CENTER,
  font=("arial", 25),
)

motdepasse.place(
  x= 50,
  y= 50,
  width= 300,
  height= 100,
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
  text="Voir MDP"
)

bouton_voir_mdp.place(
  x=250,
  y=200,
  height=50,
  width=100
)

texte_mdp = ctk.CTkEntry(
  master,
  text_color=NOIR,
  textvariable= attest_mdp,
  fg_color="transparent",
  justify=CENTER
)
texte_mdp.place(
  x=100,
  y=300,
  height=50,
  width=200
)
master.mainloop()