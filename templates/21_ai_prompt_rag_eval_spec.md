# Prompt / RAG / Evaluation — Spécification de solution IA

**Modèle fictif.** Les seuils, sources et contrôles sont proposés à titre d'exemple et non validés pour un client réel.

## 1. Fiche système
- ID : AI-DEMO-001 ; objectif : proposer la classification de documents non sensibles.
- Utilisateur : analyste autorisé ; approbateur : superviseur.
- Hors périmètre : décisions automatisées irréversibles et contenus sensibles.
- Owner, environnement, version et date : À COMPLÉTER.

## 2. Prompt Specification
| Composant | Question de conception | Preuve attendue |
| --- | --- | --- |
| Role | Quel rôle et quelle langue ? | Prompt versionné |
| Task | Quel input produit quel output ? | Exemples de référence |
| Context | Quelles données sont autorisées ? | Registre de sources |
| Schema | Quel JSON ou tableau doit être produit ? | Validation de schéma |
| Guardrails | Quels cas refuser / escalader ? | Tests négatifs |
| Version | Qui a changé quoi et pourquoi ? | Historique et delta d'évaluation |

## 3. RAG et gouvernance du corpus
Séparer sources autoritatives, brouillons, archives et exclusions. Définir owner, droits, date de référence, fréquence d'indexation, priorité des sources et réponse en cas de contradiction.

## 4. Évaluation
Construire un golden set avec questions représentatives, cas limites, attaques, sources contradictoires et demandes hors périmètre. Mesurer exactitude, exhaustivité, conformité de format, citations, confidentialité et refus approprié. Ne pas calculer une réussite globale à partir d'un petit jeu sans avertissement.

## 5. Human-in-the-loop
Le système propose ; le rôle autorisé décide. Escalader lorsqu'une source manque, que deux sources divergent ou qu'un résultat peut affecter une personne. Définir une action de repli sûre.

## 6. Exigences
- Chaque réponse inclut version de prompt et références utilisées si des sources ont été consultées.
- Aucune affirmation sans source ne doit être présentée comme validée.
- Tout changement de modèle, prompt ou corpus déclenche les tests de régression définis.
- Les journaux ne doivent pas conserver des données sensibles non nécessaires.
- Les seuils de latence, erreur et coût sont définis avec les propriétaires avant recette.

## 7. Sécurité et risques
Documenter secret management, rétention, data residency, prompt injection, droits des utilisateurs, revue des dépendances et incidents. Faire valider toute interprétation réglementaire par Legal et DPO.

## 8. Go / no-go
Confirmer qualité de corpus, jeu d'essai validé, métriques mesurées, contrôles HITL démontrés, approbateurs identifiés et procédure d'incident. Rejeter la mise en service si les contraintes critiques ne sont pas démontrées.

## Statuts
OBSERVÉ (preuve directe), DÉCLARÉ (interview), PROPOSÉ (analyse), À VALIDER (arbitrage) ; jamais de validation implicite.