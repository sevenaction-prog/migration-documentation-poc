# Workshop documentaire — BA Junior / Companion

**Guide et checklist de découverte AS-IS, données synthétiques.** Inspiré des fonctions observées dans les deux prototypes BAForge Junior, sans publication des applications.

## 1. Préparer la session
Définir périmètre, service, date, rôle des participants, objectif, exclusions et questions. Un département peut avoir plusieurs workshops. Les échanges interéquipes doivent être explicitement identifiés.

## 2. Conduire un entretien guidé
- **Pourquoi ?** Activité métier et événement déclencheur.
- **Quoi ?** Classe documentaire, exemplaire autorisé, valeur probante.
- **Où ?** Système, disque partagé, repository, dossier et arborescence.
- **Qui ?** Créateur, lecteur, modificateur, approbateur, responsable de conservation.
- **Quand ?** Début du cycle, révision, fin, exceptions et archivage.
- **Comment ?** Workflow réel, entrées, actions, décisions et sorties.
- **Interfaces ?** Processus émetteur, processus récepteur, événement et preuve.
- **Inconnues ?** Questions ouvertes, hypothèses et propriétaire de validation.

## 3. Modèles de fiches
1. Scope — nom, objectif, inclus/exclus, owner, parties prenantes, dépendances, source, confiance.
2. Repository — drive, chemin fictif, usage, owner, utilisateurs, classes, volume, droits, anomalies.
3. Document — famille, finalité, processus, formats, auteur, approbateur, version, confidentialité, rétention.
4. Processus — déclencheur, séquence, acteurs, exceptions, documents, décisions, outputs.
5. Acteur — rôle, responsabilités, justification des droits.
6. Action — question ou risque, statut, propriétaire, date cible, impact, preuve.

## 4. Séparer l'observation et le jugement
Utiliser NON ABORDÉ / DÉCLARÉ / PARTIEL / À CONFIRMER / VALIDÉ. Une réponse métier déclarée ne devient pas automatiquement un fait vérifié. Conserver la référence de preuve et la date de décision.

## 5. Workflow AS-IS
Pour chaque étape : numéro, activité, rôle responsable, acteur, entrée, document associé, emplacement, décision et sortie. Décrire les chemins alternatifs. Ne pas inventer de workflow M365.

## 6. Interfaces entre processus
Consigner émetteur, récepteur, objet transmis, canal actuellement utilisé, fréquence, contrôle de réception et anomalie. Une interface de travail n'implique pas forcément une API.

## 7. Clôture et qualité
Vérifier les champs requis, références rompues, owner absent, preuves manquantes, statut de confiance incohérent et décisions sans validation. Restituer une liste de points ouverts et proposer la prochaine étape.

## 8. Exports et confidentialité
Les prototypes examinés exportent notamment CSV, JSON de sauvegarde et compte rendu imprimable/Word-compatible ; un des prototypes exporte aussi un XML lisible dans Excel. Ces formats ne signifient pas qu'un fichier DOCX/XLSX natif est produit par l'application. Les prototypes stockent localement les données navigateur : pas de sauvegarde centralisée, pas d'authentification d'entreprise. Interdire les données RH nominatives, secrets et pièces réelles sur une version publique.

## 9. Livrables
Compte rendu de workshop, inventaire des repositories, registre de classes, matrice des acteurs, workflow AS-IS, registre d'interfaces, registre décisions/actions et état de maturité pour transmission au BA senior.

## Acceptation
Chaque élément critique comporte au moins une source, un owner, un statut et le prochain arbitrage. Le design cible reste à valider avec métier, architecture et sécurité.