# Graphe

Bibliothèque Python simple pour la gestion et le parcours de graphes :
- graphes orientés / non orientés
- graphes pondérés / non pondérés
- parcours en largeur (BFS) et en profondeur (DFS)

Le projet a un but pédagogique : proposer des structures de données et des algorithmes de base pour manipuler des graphes.

## Fonctionnalités
- Représentation de graphes (listes d'adjacence)
- Ajout / suppression de sommets et d'arêtes
- Support des graphes orientés et non orientés
- Support des poids sur les arêtes (graphes pondérés)
- Parcours en largeur (BFS) et parcours en profondeur (DFS)
- Utilitaires (pile/queue si présents dans le projet)

## Installation
Cloner le dépôt et installer dans un environnement virtuel :

```bash
git clone https://github.com/youssef-lecodeur/graphe.git
cd graphe
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate sur Windows
pip install -r requirements.txt  # si un fichier requirements.txt est ajouté
pip install -e .
```

Si le dépôt n'est pas packagé, vous pouvez simplement importer les modules depuis la racine du projet.

## Usage (exemples)
Les noms de classes et méthodes peuvent varier selon les fichiers fournis. Voici des exemples d'usage type que la bibliothèque vise à supporter :

Créer un graphe non orienté non pondéré et faire un BFS :

```python
from graphe import Graph  # exemple d'import, adapter selon le package réel

g = Graph(directed=False)           # graphe non orienté
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")                # ajoute une arête A-B

# BFS à partir de "A"
order = g.bfs("A")
print("Ordre BFS :", order)
```

Graphe orienté et DFS (itératif) :

```python
g = Graph(directed=True)
g.add_edge("1", "2")
g.add_edge("1", "3")
g.add_edge("3", "4")

visited = g.dfs("1")  # parcours en profondeur
print("Visités par DFS :", visited)
```

Graphe pondéré et algorithme de plus court chemin (exemple Dijkstra) :

```python
g = Graph(directed=False, weighted=True)
g.add_edge("A", "B", weight=5)
g.add_edge("B", "C", weight=2)
distances = g.dijkstra("A")
print(distances)  # distances minimales depuis A
```

Remarque : si les noms de classes/méthodes diffèrent dans le dépôt, adaptez les appels (par ex. `Graphe_OP2`, `Graphe_ONP2`, `lesgraphes.py`).

## API recommandée (suggestions)
Idées d'API claires et uniformes pour chaque implémentation :
- Constructeur : Graph(directed: bool = False, weighted: bool = False)
- add_vertex(v)
- add_edge(u, v, weight: float | int = 1)
- remove_vertex(v)
- remove_edge(u, v)
- neighbors(v) -> list
- bfs(start) -> list (ordre de visite)
- dfs(start) -> list (ordre de visite)
- dijkstra(start) -> dict (distances) — si pondéré

## Tests
Il est fortement recommandé d'ajouter une suite de tests (pytest). Exemple pour lancer les tests :

```bash
python -m pytest
```

Cas de test à couvrir :
- Graphe vide
- Graphe connecté et non connecté
- Self-loops et arêtes dupliquées
- Graphe pondéré avec poids positifs (Dijkstra)
- Comportement sur sommets/arêtes inconnus (erreurs / exceptions)

## Style & qualité
- Formattage : black
- Linting : ruff / flake8
- Typage : mypy (ajouter des annotations de type pour l'API publique)
- CI recommandée : GitHub Actions pour exécuter tests + lint + mypy

## Contribution
Contributions bienvenues. Idées pour les améliorations :
- Ajout de tests unitaires et d'un pipeline CI
- Conversion en package Python (pyproject.toml)
- Documentation détaillée (Sphinx / MkDocs)
- Visualisations d'exemples (notebooks)

Merci d'ouvrir une issue ou une pull request pour toute amélioration.

## Licence
Aucune licence fournie dans l'état actuel du dépôt. Ajouter un fichier `LICENSE` (par ex. MIT) si vous souhaitez autoriser la réutilisation.
