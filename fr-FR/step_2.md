## Commencer

--- task ---

Ouvre le [projet de démarrage Motifs puissants](https://editor.raspberrypi.org/fr-FR/projects/powerful-patterns-starter){:target="_blank"}.

--- /task ---

### Configurer ton projet

--- task ---

Choisis une taille et une couleur d'arrière-plan.

--- code ---
---
language: python
line_numbers: true line_number_start: 6
line_highlights: 7-8
---
def setup():
    size(400, 400)  # Choisis une taille
    background(255, 255, 255)  # Essaie différents nombres pour changer la couleur

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton projet pour voir les modifications.

La quantité maximale de rouge, de vert ou de bleu est de `255`. Assure-toi que toutes tes valeurs de couleur `d'arrière-plan` sont comprises entre `0` et `255`.

--- /task ---


