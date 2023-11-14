from entites.Ouvrage import Ouvrage  
import db

connection = db.db

class ServiceOuvrage:

    ''' GET
    Récupérer tous les ouvrages
    '''    
    def getAllOuvrages():
        return Ouvrage.query.all()
    

    ''' GET
    Récupérer un ouvrage par son ID
    '''
    def getOuvrageById(id_ouvrage):
        ouvrage = Ouvrage.query.get(id_ouvrage)
        return ouvrage


    ''' POST
    Créer un nouvel ouvrage dans la BDD
    Avec tous les paramètres
    '''
    def createOuvrage(titre,
                      auteur,
                      isbn,
                      langue,
                      prix,
                      date_parution,
                      categorie,
                      date_disponibilite_libraire,
                      date_disponibilite_particulier,
                      image,
                      table_des_matieres,
                      mot_cle,
                      description):
        # on se sert d'un objet Ouvrage pour y remplir les informations
        ouvrage = Ouvrage(titre_ouvrage = titre, 
                            auteur_ouvrage = auteur,
                            isbn_ouvrage = isbn,
                            langue_ouvrage = langue,
                            prix_ouvrage = prix,
                            date_parution_ouvrage = date_parution,
                            categorie_ouvrage = categorie,
                            date_disponibilite_libraire_ouvrage = date_disponibilite_libraire,
                            date_disponibilite_particulier_ouvrage = date_disponibilite_particulier,
                            image_ouvrage = image,
                            table_des_matieres_ouvrage = table_des_matieres,
                            mot_cle_ouvrage = mot_cle,
                            description_ouvrage = description
                            )
        # ouvrir la connexion et ajouter un client à la BDD
        connection.session.add(ouvrage)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return ouvrage
    

    ''' PUT
    Update d'un ouvrage par son ID
    '''
    def updateOuvrage(id_ouvrage,
                      titre,
                      auteur,
                      isbn,
                      langue,
                      prix,
                      date_parution,
                      categorie,
                      date_disponibilite_libraire,
                      date_disponibilite_particulier,
                      image,
                      table_des_matieres,
                      mot_cle,
                      description
                      ): 
        # on se sert d'un objet Ouvrage pour y remplir
        # l'ouvrage qu'on récupère en BDD par son ID
        ouvrage = Ouvrage.query.get(id_ouvrage)
        if ouvrage:

            # assignation des attributs
            ouvrage.titre_ouvrage = titre
            ouvrage.auteur_ouvrage = auteur
            ouvrage.isbn_ouvrage = isbn
            ouvrage.langue_ouvrage = langue
            ouvrage.prix_ouvrage = prix
            ouvrage.date_parution_ouvrage = date_parution
            ouvrage.categorie_ouvrage = categorie
            ouvrage.date_disponibilite_libraire_ouvrage = date_disponibilite_libraire
            ouvrage.date_disponibilite_particulier_ouvrage = date_disponibilite_particulier
            ouvrage.image_ouvrage = image
            ouvrage.table_des_matieres_ouvrage = table_des_matieres
            ouvrage.mot_cle_ouvrage = mot_cle
            ouvrage.description_ouvrage = description

            # sauvegarder et fermer la connexion avec la BDD
            connection.session.commit()
            return ouvrage
        return None
    

    ''' DELETE
    Supprimer un ouvrage par son ID
    '''    
    def deleteOuvrage(id_ouvrage):
        # récupération de l'ouvrage en BDD par ID
        ouvrage = Ouvrage.query.get(id_ouvrage)
        if ouvrage:
            # supprimer l'ouvrage de la BDD
            connection.session.delete(ouvrage)
            # sauvegarder et fermer la connexion avec la BDD
            connection.session.commit()
            return True
        # retourne False si ça s'est mal passé
        return False