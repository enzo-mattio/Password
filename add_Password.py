import tkinter as tk
import customtkinter as ctk
import random


car_spécial = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",  "[", "]", "|", ":", ";", "-", "_", "+", "=", "{", "}", "<", ">", ",", ".", "?"]

# Fonction qui permet de vérifier les conditions qu'on veut pour le mot de passe.

def verif_password(mot_de_passe):
  
  global car_spécial
  
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
  
  # print(contient_special)
  # print(contient_chiffre)
  # print(contient_majuscule)
  # print(contient_minuscule)
  
# print(verif_password("zdvhjbvzeion"))
