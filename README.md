# README Documentation :wave:

 ## 1. Description :notebook_with_decorative_cover:

Notre application a pour but la mise en place d'un back-end pour un site internet d'une maison d'édition. Actuellement, la maison d'édition travaille uniquement avec des librairies de la manière suivante :
- Les libraires reçoivent hebdomadairement une newsletter (par mail) leur indiquant les sorties à venir
- Un catalogue papier leur est également envoyé 2 fois par an.
- Les commandes sont prises par téléphone ou via des e-mails.
- Les paiements sont effectués par virement.

 ## 2. Les objetcifs :dart:

L’objectif principal est d'ouvrir le service aux particulier grâce l'élaboration d'un site permettant aux internautes de rechercher des ouvrages par thème, auteur, mot-clé, etc., de se constituer un panier virtuel, puis de pouvoir les commander et les payer directement sur le Web.

## 3. Fonctionnalités :gear:
Pour les clients : 
- Création d'un compte utilisateur, possibilité de le mettre à jour. 
- Recherche d'ouvrage, vérification de la disponibilité d'un livre. 
- Passage d'une commande avec l'option de la modifier ou de la supprimer.
- Ajout d'un moyen de paiement, sa modification ou sa suppression.
- Ajouter un commantaire à un ouvrage, le modifier ou le supprimer.
    
Pour le gestionnaire du site:
- Ajout d'un ouvrage au site, modifier ses informations si besoin et également le supprimer du site.
- Mise en place de thème pour les ouvrages avec les fonctions de modification et de suppression.

## 4. Exigences :warning:

Voir fichier [requirement.text](requirement.txt)

## 5. Architecture :classical_building:
Nous avons utilisé une architecture similaire à l'architecture MVC.  
Nos différences sont :  
- Entités
- Contrôleurs
- Services
Les entités contiennent toutes les classes ("ouvrages", "commandes", etc ...).  
Chaque entité est relié à un contrôleur et un service.  
Le contrôleur contient tous les routes définis pour chaque entité qui va permettre d'identifier la demande du client.  
Exemple : getClients, getClientById  
Les services contiennent différentes méthodes qui vont nous permettres de communiquer avec la base de données avec la méthodologie CRUD (create, read, update, delete).  
Les routes au sein des contrôleurs vont appeler les méthodes des services.  

## 6. Outils et technologies :test_tube:

**IDE** :   
Visual Studio Code  
Version: 1.84.2 (user setup)  
Commit: 1a5daa3a0231a0fbba4f14db7ec463cf99d7768e  
Date: 2023-11-09T10:51:52.184Z  
Electron: 25.9.2  
ElectronBuildId: 24603566  
Chromium: 114.0.5735.289  
Node.js: 18.15.0  
V8: 11.4.183.29-electron.0  
OS: Windows_NT x64 10.0.19045  

**Solution stack** :   
WampServer version 3.3.0   
Apache 2.4.54.2 Port 80 - PHP 7.4.33  
MySQL 8.0.31 Port 3306  
PHP 7.4.33 for CLI (Command-Line Interface)  

**Gestion base de données** :  
PhpMyAdmin version 5.2.0  

**Langage de programmation** : Python v3.12  
Langage obligatoire pour l'exercice  
Bibliothèques utilisées :   
- Flask : pour les requêtes API
- Flask_sqlalchemey : Pour faire fonctionner Flask et SQLAlchemey
- SQLAlchemey : Boîte à outils pour réaliser en Python des oprétations sur une base de données relationnel. Il inclut en autre un ORM( : objet-relationnal mapper : Permet de manipuler la bdd dans l'application mère, ici Python. Sans SQL.)
- Pymysql : Définition des connexions avec phpmyadmin
- Cryptography : Recevoir correctement les requêtes HTTP
- Swagger : Solution API pour les tests

## 7. Equipe :raising_hand_man: :ok_woman: :man_shrugging:

Wasin Al Shami    
Angela Cruz   
Henri Pierre    









