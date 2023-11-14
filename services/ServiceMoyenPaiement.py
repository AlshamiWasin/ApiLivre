from entites.Moyenpaiement import Moyenpaiement  
import db

connection = db.db

class ServiceMoyenPaiement:
    def getAllMoyenPaiements():
        return Moyenpaiement.query.all()
    

    ''' GET
    Récupérer un moyenpaiement par son ID
    '''
    def getMoyenPaiementById(id_moyen_paiement):
        moyenpaiement = Moyenpaiement.query.get(id_moyen_paiement)
        return moyenpaiement


    ''' POST
    Créer un nouveau moyen de paiement dans la BDD
    '''
    def createMoyenPaiement(type, nom, numero, date, code):
        # on se sert d'un objet moyen de paiement pour y remplir les informations
        new_moyenpaiement = Moyenpaiement(type_paiement = type, 
                            nom_proprietaire_paiement = nom,                                          
                            numero_moyen_paiement = numero, 
                            date_expiration_paiement = date , 
                            code_secu_paiement = code )
        # ouvrir la connexion et ajouter un moyen de paiement à la BDD
        connection.session.add(new_moyenpaiement)
        # sauvegarder et fermer la connexion avec la BDD
        connection.session.commit()
        return new_moyenpaiement
    
    def updateMoyenPaiement(id_moyen_paiement, new_type, new_nom, new_numero , new_date, new_code): 
        moyenpaiement = Moyenpaiement.query.get(id_moyen_paiement)
        if moyenpaiement:
            moyenpaiement.type_paiement = new_type
            moyenpaiement.nom_proprietaire_paiement = new_nom
            moyenpaiement.numero_moyen_paiement = new_numero
            moyenpaiement.date_expiration_paiement = new_date
            moyenpaiement.code_secu_paiement = new_code
            connection.session.commit()
            return moyenpaiement
        return None
    
    def deleteMoyenPaiement(id_moyen_paiement):
        moyenpaiement = Moyenpaiement.query.get(id_moyen_paiement)
        if moyenpaiement:
            connection.session.delete(moyenpaiement)
            connection.session.commit()
            return True
        return False