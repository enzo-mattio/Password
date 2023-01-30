import json
import hashlib

with open('mdp.json') as f:
  content= json.load(f)

# print([content[i] for i in content])

# empty_arr=[]
# for i in content:
#   empty_arr.append(content[i])
  
# print(empty_arr)

# #-------------------------------------------------------

# liste_bruh=[1,5,6,9]
# print([i**2 for i in liste_bruh])

# temporary_arr=[]
# for i in liste_bruh:
#   temporary_arr.append(i**2)
# print(temporary_arr)  


#-----------------------------------------------------

# facebook_data=content[[i for i in content][0]]
# instagram_data=content[[i for i in content][1]]

# print('Facebook Data: \n',facebook_data)
# print('Instagram Data: \n',instagram_data)


identifiants = "Enzo"
mdp= "Ejnioucqgy58*"

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

print(hash_pass(mdp))

if identifiants not in [i for i in content] and hash_pass not in [content[i] for i in content]:
   content[identifiants]=hash_pass(mdp)
   with open("mdp.json", 'w') as fichier:
    json.dump(content, fichier, indent=4)
pass

print(content)
