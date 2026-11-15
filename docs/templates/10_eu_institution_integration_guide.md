# Analyse fonctionnelle et gouvernance documentaire — intégration financière institutionnelle

## Positionnement du modèle
Ce document est un **canevas fictif et réutilisable** pour la modernisation d'un système financier institutionnel. Il ne représente ni un livrable original ni une spécification approuvée par une organisation réelle. Tous les objets, responsabilités, identifiants et exemples ont été reconstruits à titre pédagogique.

## 1. Objectif et valeur métier
Préserver les comportements métier utiles tout en remplaçant une consultation financière directe par des services intermédiés. La valeur attendue est la continuité opérationnelle, une origine de données maîtrisée, des décisions explicites et des résultats vérifiables de bout en bout.

## 2. Contexte fonctionnel fictif
Un système métier gère des dossiers et références financières. En AS-IS, les données de tiers, engagements, comptes et lignes budgétaires sont consultées dans un ancien référentiel. En TO-BE, un service d'intégration sécurisée distribue les mêmes informations depuis une source financière de référence.

## 3. Délimitation et responsabilités
- Business Owner : objectif, priorité, règles de gestion et arbitrage des exceptions.
- Process Owner : validation des états, transitions et cas métiers.
- Data Owner : dictionnaire, qualité, statut de source de vérité et conservation.
- BA / Functional Analyst : workflows, mapping, règles, exigences et traçabilité.
- Architecte / équipe API : contrat technique, résilience et intégration.
- Security / Compliance : contrôles d'accès, données personnelles et journalisation.
- QA / Key Users : critères d'acceptation, UAT et preuve de validation.
- Run Team : supervision, connaissance, escalade et passation.

## 4. Baseline et analyse AS-IS
Inventorier les écrans, actions utilisateur, données, systèmes de référence, synchronisations, traitements manuels et exceptions. Conserver une matrice de preuve : observation, source, hypothèse, propriétaire, date de validation. Ne jamais présenter une inférence comme une décision approuvée.

## 5. Analyse TO-BE orientée processus
- Création de dossier : rechercher une référence, confirmer l'identité et vérifier les informations nécessaires.
- Modification : recalculer les attributs sensibles lorsqu'une donnée source est actualisée.
- Soumission et validation : appliquer les contrôles bloquants et tracer l'auteur de la décision.
- Annulation : enregistrer le motif, la date et la conséquence métier.
- Recherche et reporting : restituer la source effective et l'horodatage de synchronisation.

## 6. Cartographie des données et règles de transformation
Chaque champ doit porter : identifiant fictif, objet métier, source, cible, format, règle de transformation, nullabilité, source de vérité, statut, preuve, owner et scénario de test. Les valeurs « à déterminer » doivent rester visibles et empêcher un faux accord.

## 7. Contrôles fonctionnels et qualité
Prévoir des règles de présence obligatoire, cohérence des références, validité de la réponse du service, unicité et statut de référence. Un échec bloquant interrompt la transition concernée ; un avertissement ne doit pas être confondu avec un blocage. Les exemples de seuils restent configurables et ne prétendent à aucune règle réelle.

## 8. Contrat d'interface et sécurité
Documenter les événements d'appel, codes de réponse, règles de retry, horodatage, idempotence, journalisation minimale et séparation des responsabilités. Les URL, charges utiles et noms d'API restent fictifs. Aucun jeton ou secret ne doit figurer dans un livrable.

## 9. Gestion documentaire du package projet
- 00 Gouvernance : référentiel de décisions, inventaire des versions et propriétaires.
- 01 Business : besoins, processus AS-IS et arbitrages.
- 02 Fonctionnel : spécifications, user stories, cas d'usage.
- 03 Données / API : dictionnaire, mapping, transformation et exceptions.
- 04 Règles : catalogue, priorité, preuves de validation.
- 05 Recette : traceabilité, UAT, anomalies, rapprochements.
- 06 Passation : connaissance, runbook, points ouverts, ownership.
- 99 Historique : versions remplacées sous règles de conservation approuvées.

## 10. Traçabilité complète
Une décision valide doit être reliée à un besoin, une exigence, une règle, un cas d'usage, une interface et un ou plusieurs tests. Une référence n'est « confirmée » que si une source ou un décideur explicitement nommé l'appuie.

## 11. Stratégie de test et critères d'acceptation
Tester happy path, données manquantes, références expirées, conflit de statut, erreur de service, délai dépassé, idempotence, droits insuffisants et réconciliation des données. Formaliser les résultats attendus, les données de test synthétiques et les responsables de validation.

## 12. Handover et préparation RUN
Préparer un inventaire des livrables, les versions de référence, le dictionnaire des données, le registre de décisions, les écarts non résolus, les contacts par rôle, les règles d'escalade, les scénarios de test et une checklist d'acceptation du successeur.

## 13. Points de décision avant mise en œuvre
- Confirmer le système de référence pour chaque objet.
- Confirmer les droits et la classification par famille.
- Valider les cas métiers et règles bloquantes.
- Lever les écarts de mapping et les champs indéterminés.
- Approuver les exigences non fonctionnelles.
- Signer les jeux de tests et critères de bascule.

## 14. Contrôles de faisabilité et limites
Le document ne contient ni architecture réelle, ni contrats API réels, ni processus organisationnels validés. Tout usage en contexte professionnel nécessite un inventaire, un atelier, la validation des propriétaires et une revue de sécurité.