# Projet Approx - Teamfight Tactics (TFT) - Exaltés

## Description

Ce projet vise à résoudre un problème inspiré du jeu vidéo Teamfight Tactics (TFT), où l'objectif est de déterminer le nombre maximum d'unités
 pouvant être exaltées simultanément sous certaines contraintes. Deux algorithmes ont été implémentés : 
un algorithme exact utilisant un brute force et un algorithme d'approximation.

## Structure du Projet

Le projet est organisé de la manière suivante :

- `main.py` : Script principal contenant l'appel aux fonctions contenues dans src/.
- `input` : Fichier d'entrée contenant les données des personnages (given file).
- `README` : Ce fichier, contenant des instructions sur la manière d'exécuter le projet.
- `src` : Dossier contenant le source code.

## Prérequis

- Python 3.x
- package networkx (pip install networkx)

### Instructions pour l'Utilisation

1. Télécharger et Installer Python 3.x : Assurez-vous d'avoir Python 3.x installé sur votre machine. 
Vous pouvez le télécharger depuis le site officiel [Python.org](https://www.python.org/).
2. Préparer le Fichier d'Entrée : Créez un fichier  avec les données des personnages selon le format spécifié 
ou faites python3 generate_data.py et mettez le contenu affiche dans un fichier.
`Grammaire de l’input` :
```
S → Id_L
Id → [a-zA-Z]+
L → T | T_L
T → [a-zA-Z0-9]+
```
4. Exécuter le Script : Lancez le script principal `main.py` à partir de la ligne de commande en utilisant la commande `python main.py` 
puis indiquez le nom de votre fichier.

## Instructions

### Format du Fichier d'Entrée

Le fichier d'entrée doit contenir les données des personnages, chaque ligne représentant un personnage avec d'abord son nom puis ses traits. 
Par exemple :
```
John Behemoth Forge
Smith Behemoth Void
Zorro Phantom Wolf
```

### Exécution du Script

1. Assurez-vous que Python 3.x est installé sur votre machine.
2. Placez le fichier avec les noms des personages ainsi que leurs traits dans le même répertoire que `main.py`.
3. Exécutez le script principal :
	python3 main.py
	Le script affichera: "Entrez le nom de l'input:"
	rentrez le nom du fichier avec l'input puis faites entree.
