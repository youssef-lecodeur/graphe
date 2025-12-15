from Graphe_NONP2 import *
from Graphe_NOP2 import *
from Graphe_ONP2 import *
from Graphe_OP2 import *
from File import *
from Pile import *
class Parcours:
    def __init__(self):
        self.
    
    def parcours_largeur(self, valeur_depart):
        if valeur_depart not in self.sommets:
            return "Départ non trouvé"
        
        sommet_depart = self.sommets[valeur_depart]
        
        file_a_visiter = File()  
        file_a_visiter.enfiler(sommet_depart)
        visites = {sommet_depart}
        resultat = []
        
        while not file_a_visiter.est_vide():
            sommet_courant = file_a_visiter.defiler()
            resultat.append(sommet_courant.valeur)
            
            for voisin in sommet_courant.obtenir_voisins():
                if voisin not in visites:
                    visites.add(voisin)
                    file_a_visiter.enfiler(voisin)
                    
        return resultat

    def parcours_profondeur(self, valeur_depart):
        if valeur_depart not in self.sommets:
            return "Départ non trouvé"
        
        sommet_depart = self.sommets[valeur_depart]
        
        pileav = Pile()  
        pileav.empiler(sommet_depart)
        visites = set()
        resultat = []
        
        while not pileav.est_vide():
            sommet_courant = pileav.depiler()
            
            if sommet_courant not in visites:
                visites.add(sommet_courant)
                resultat.append(sommet_courant.valeur)
                
                for voisin in sommet_courant.obtenir_voisins():
                    if voisin not in visites:
                        pileav.empiler(voisin)
                        
        return resultat