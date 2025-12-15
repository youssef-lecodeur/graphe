class Graphe_OP:
    def __init__(self):
        self.dic = dict()

    def ajout_sommet(self, s):
        if s in self.dic:
            return
        self.dic[s] = {}

    def ajout_arete(self, depart, arrivee, poids=0):
        if depart not in self.dic:
            self.ajout_sommet(depart)
        if arrivee not in self.dic:
            self.ajout_sommet(arrivee)

        self.dic[depart][arrivee] = poids
        
    def set_poids(self, depart, arrivee, poids):
        if self.est_arete_existante(depart, arrivee):
            self.dic[depart][arrivee] = poids
        else:
            raise ValueError(f"L'arête orientée de {depart} à {arrivee} n'existe pas.")
        
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
            arcs = [f"({v}, p={p})" for v, p in voisins.items()]
            graphe_str += ", ".join(arcs) + "\n"
        return graphe_str

G2 = Graphe_OP()
G2.ajout_sommet('A')
G2.ajout_sommet('B')
G2.ajout_sommet('C')
G2.ajout_sommet('D')

G2.ajout_arete('A', 'B', 2)
G2.ajout_arete('A', 'C', 7)
G2.ajout_arete('B', 'D', 3)
G2.ajout_arete('C', 'D', 1)
G2.ajout_arete('D', 'A', 5)
G2.ajout_arete('B', 'E', 9)

print(G2)

try:
    G2.set_poids('A', 'C', 10)
    print(G2)
except ValueError as e:
    print(e)

try:
    G2.set_poids('C', 'A', 99)
except ValueError as e:
    print(e)