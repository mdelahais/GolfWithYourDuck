#!/usr/bin/env python
#-*- coding: utf-8 -*-

dictioplayers = {}
gameplayer = "oui"

while gameplayer == "oui":
	
	player = raw_input('Nom du joueur : ').lower()
	dictioplayers[player] = 0
	gameplayer = raw_input("Rajouter joueur ?\n").lower()

rounds = "oui"

print("\n")
print("Voici les joueur présent cela vous vas ?")
print(dictioplayers)
print("\n")

while rounds == "oui":
	for name in dictioplayers.keys():

		dictioplayers[name] += int(raw_input("Rentrer score du joueur " + name + " : \n"))

	rounds = raw_input("Nouvelle Partie ?\n")


dictList=zip(dictioplayers.values(),dictioplayers.keys())
dictList.sort()
premier=dictList[0][1]
print("\n")
print("Voici notre gagnant : " + premier)
print("Bravo sale con \n")

suite = raw_input("Voulez voir la suite ?").lower()

if suite == "oui":

	deuxieme = dictList[1][1]
	print("Voici notre 2éme : " + deuxieme + "\n")


	troisieme = dictList[2][1]
	print("Voici notre 3éme : " + troisieme + "\n")

	print(dictioplayers) 
if suite == "non":

	print("tu n'est qu'un sale con, pute\n")
	suite = raw_input('Bon tu veux voir le score connard quand meme ?').lower()

	if suite == "oui":

		deuxieme = dictList[1][1]
		print("Voici notre 2éme : " + deuxieme + "\n")


		troisieme = dictList[2][1]
		print("Voici notre 3éme : " + troisieme + "\n")

		print(dictioplayers) 