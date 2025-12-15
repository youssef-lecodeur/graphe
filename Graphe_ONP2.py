class Graphe_ONP:
    def __init__(self):
        self.dic = dict()

    def ajout_sommet(self, s):
        if s in self.dic:
            return
        self.dic[s] = {}

    def ajout_arete(self, depart, arrivee):
        if depart not in self.dic:
            self.ajout_sommet(depart)
        if arrivee not in self.dic:
            self.ajout_sommet(arrivee)

        self.dic[depart][arrivee] = True
        
    def est_arete_existante(self, depart, arrivee):
        if depart in self.dic:
            return arrivee in self.dic[depart]
        return False
        
    def get_voisins(self, s):
        if s in self.dic:
            return self.dic[s].keys()
        return set()

    def __repr__(self):
        graphe_str = ""
        for sommet, voisins in self.dic.items():
            graphe_str += f"{sommet} -> "
            arcs = [str(v) for v in voisins.keys()]
            graphe_str += ", ".join(arcs) + "\n"
        return graphe_str

G3 = Graphe_ONP()
G3.ajout_sommet(1)
G3.ajout_sommet(2)
G3.ajout_sommet(3)
G3.ajout_sommet(4)

G3.ajout_arete(1, 2)
G3.ajout_arete(2, 3)
G3.ajout_arete(3, 4)
G3.ajout_arete(4, 1)
G3.ajout_arete(1, 4)

print(G3)

print(G3.est_arete_existante(1, 4))
print(G3.est_arete_existante(4, 3))
print(G3.get_voisins(1))