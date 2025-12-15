class Graphe_NONP:
    def __init__(self):
        self.dic = dict()

    def ajout_sommet(self, s):
        assert s not in self.dic, "Le sommet existe déjà."
        self.dic[s] = []

    def ajout_arete(self, a, b):  # arete entre a et b
        if a not in self.dic.keys():
            self.ajout_sommet(a)
        if b not in self.dic.keys():
            self.ajout_sommet(b)
        assert not self.est_voisin(a, b), "a et b sont déjà reliés."
        self.dic[a].append(b)
        self.dic[b].append(a)
   
    def est_voisin(self, a, b):
        return b in self.dic[a]
       
    def __repr__(self):
        return str(self.dic)