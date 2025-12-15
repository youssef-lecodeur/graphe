class Graphe_NOP:
    def __init__(self):
        self.dic = dict()

    def ajout_sommet(self, s):
        assert s not in self.dic, f"Le sommet {s} existe déjà."
        self.dic[s] = {}

    def ajout_arete(self, a, b, poids=0):
        if a not in self.dic:
            self.ajout_sommet(a)
        if b not in self.dic:
            self.ajout_sommet(b)

        self.dic[a][b] = poids
        self.dic[b][a] = poids
        
    def set_poids(self, a, b, poids):
        if self.est_voisin(a, b):
            self.dic[a][b] = poids
            self.dic[b][a] = poids
        else:
            raise ValueError(f"L'arête entre {a} et {b} n'existe pas.")
        
    def est_voisin(self, a, b):
        if a in self.dic:
            return b in self.dic[a]
        return False
        
    def __repr__(self):
        return str(self.dic)
    
G1=Graphe_NOP()
G1.ajout_sommet('A')
G1.ajout_sommet('B')
G1.ajout_arete('A','B',2)
G1.ajout_sommet('C')
G1.ajout_arete('A','C',7)
print(G1)