from entites.Commande import Commande
import db

connection = db.db

class ServiceCommande:

    ''' GET
    Récupérer tous les commandes
    '''
    def getAllCommande():
        return Commande.query.all()
    

    def createCommand(id_client, id_ouvrage, id_moyen_paiement, date_commande, montant):
        new_command = Commande(
            id_client=id_client,
            id_ouvrage=id_ouvrage,
            id_moyen_paiement=id_moyen_paiement,
            date_commande=date_commande,
            montant=montant
        )
        connection.session.add(new_command)
        connection.session.commit()
        return new_command
    


    def getCommandById(command_id):
        return Commande.query.get(command_id)
    


    def updateCommand(command_id, data):
        command = Commande.query.get(command_id)
        if command:
            for key, value in data.items():
                setattr(command, key, value)
            connection.session.commit()
            return command
        else:
            return None
        

    def deleteCommand(command_id):
        command = Commande.query.get(command_id)
        if command:
            connection.session.delete(command)
            connection.session.commit()
            return True
        else:
            return False

    @staticmethod
    def getAllCommands():
        commands = Commande.query.all()
        return [command.serialize() for command in commands]