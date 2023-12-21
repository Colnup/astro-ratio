# Todo list - suivi du projet

## Défis basiques

- [ ] Créer une interface graphique
  - [ ] Capable de charger une image
  - [ ] Afficher l'image chargée
  - [ ] Charger une image de gradient
  - [ ] Afficher l'image après traitement

## Défis intermédiaires

- [ ] Implémenter au moins une méthode de détection du gradient
- [ ] Effectuer une comparaison sur l'efficacité du traitement entre C++ et Python

## Défis avancés

- [ ] Implémenter _plusieurs_ méthodes de détection du gradient
- [ ] Prévoir un traitement d'images par lot
- [ ] Comparer les résultats des différentes méthodes de détection du gradient (temps de calcul, qualité du résultat, mémoire utilisée, etc.)
- [ ] Tout autre ajout pertinent
  - [ ] Ajout d'une interface complète CLI

## Défis experts

- [ ] Proposez et implémentez une architecture logicielle permettant de représenter une ≪ suite ≫ de traitements d’images comme un graphe acyclique orienté de traitements atomiques. Dans ce modèle, récupérer les fichiers images d’un répertoire, lire une image, évaluer le gradient, supprimer le gradient sont des traitements atomiques.
- [ ] Proposez un langage simple permettant de définir une ≪ suite ≫ de traitement et implémentez un ≪ transpileur ≫ transformant un fichier dans votre langage en un code C++/python permettant d’effectuer les traitements.
  - [ ] Définir un format de fichier
    - [ ] YAML
    - [ ] JSON
    - [ ] XML

## Avant rendu final

- [ ] Cleanup readme
  - [ ] Liste des réalisations
  - [ ] Liens vers sources utilisées
- [ ] Cleanup code
- [ ] Suite de tests
- [ ] Documentation
