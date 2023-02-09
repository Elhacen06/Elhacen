  # # exercice 3
liste=[]
while True:
     n=int(input("Entrez un nombre entre 0 pour terminer la list :"))
     if n==0:
         break
     liste.append(n)

# #Afficher la liste
print("Voici la liste: ",liste)
listepos=[]
listeneg=[]
for n in liste:
     if n>=0:
         listepos.append(n)
     else:
         listeneg.append(n)
 #Afficher les deux listes
print("Voici la liste des nombres positifs: ",listepos)
print("Voici la liste des nombres négatifs: ",listeneg)

for n in liste:
     partieentiere=int(n)
     factoriel=1
for i in range(1,n+1):
        factoriel*=i
print("La partie entière de",n," est ",partieentiere,"et son factoriel est ",factoriel)