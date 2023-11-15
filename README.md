# README Documentation :wave:

## 1.Introduction

 ### 1. Description

    Notre application a pour but la mise en place d'un back-end pour un site internet d'une maison d'édition. Actuellement, la maison d'édition travaille uniquement avec des librairies de la manière suivante :
        - Les libraires reçoivent hebdomadairement une newsletter (par mail) leur
        indiquant les sorties à venir
        - Un catalogue papier leur est également envoyé 2 fois par an.
        - Les commandes sont prises par téléphone ou via des e-mails.
        - Les paiements sont effectués par virement.

 ## 2. Les objetcifs

    L’objectif principal est d'ouvrir le service aux particulier grâce l'élaboration d'un site permettant aux internautes de rechercher des ouvrages par thème, auteur, mot-clé, etc., de se constituer un panier virtuel, puis de pouvoir les commander et les payer directement sur le Web.

## 3. Fonctionnalités
    Pour les clients : 
        Création d'un compte utilisateur, possibilité de le mettre à jour. 
        Recherche d'ouvrage, vérification de la disponibilité d'un livre. 
        Passage d'une commande avec l'option de la modifier ou de la supprimer.
        Ajout d'un moyen de paiement, sa modification ou sa suppression.
        Ajouter un commantaire à un ouvrage, le modifier ou le supprimer.
    
    Pour le gestionnaire du site:
        Ajout d'un ouvrage au site, modifier ses informations si besoin et également le supprimer du site.
        Mise en place de thème pour les ouvrages avec les fonctions de modification et de suppression.

## 4. Exigences

Voir fichier requirements.text [link to File]

## 5. Architecture
Nous avons utilisé une architecture similaire à l'architecture MVC. 
Nos différences sont : 
    Nous disposons de : 
        - Entités
        - Contrôleurs
        - Services
    Les entités contiennent toutes les classes ("ouvrages", "commandes", etc ...)
    Chaque entité est relié à un contrôleur et un service. 

    Le contrôleur contient tous les routes définis pour chaque entité qui va permettre d'identifier la demande du client.  
        Exemple : getClients, getClientById
    
    
    Les services contiennet différentes méthodes qui vont nous permettres de communiquer avec la base de données avec la méthodologie CRUD (create, read, update, delete). 
    Les routes au sein des contrôleurs vont appeler les méthodes des services.

    Diagramme : 
    ```mermaid
    graph TD;
    App --> Contrôleur;
    Contrôleur --> Service;
    Service --> Entités;
    Service --> Base de données;
    ```







