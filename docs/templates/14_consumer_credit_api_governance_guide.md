# Cahier d'analyse métier — crédit à la consommation, référentiels et API

## Positionnement
Canevas fictif de Business Analysis et Product Ownership pour une organisation de financement à la consommation. Il ne constitue pas un contrat API officiel, une politique de crédit ou un document bancaire approuvé. Tous les identifiants et exemples sont inventés.

## 1. Ambition
Structurer l'intégration de référentiels Produit et Véhicule dans un parcours de financement connecté à plusieurs canaux de distribution. Réduire les ressaisies et les incohérences en clarifiant la source de vérité, les règles de contrôle et la chaîne d'acceptation.

## 2. Périmètre métier type
- Consultation des familles de produits et de leurs états de disponibilité.
- Consultation de catégories et caractéristiques de véhicules.
- Association d'une référence produit à un dossier de simulation ou financement.
- Mise à disposition des références par des API REST documentées.
- Conservation contrôlée des documents et versions de référence.
- Articulation Business, Distribution, Compliance, Operations et IT.

## 3. Parcours AS-IS / TO-BE
AS-IS fictif : référentiels différents selon les canaux, échanges manuels, demandes de clarification, ressaisie et preuves éparpillées. TO-BE proposé : un référentiel maître, des services de consultation versionnés, des erreurs explicites et des dossiers traçables.

## 4. Rôles et gouvernance
- Product Owner : valeur, backlog, ordre de livraison et arbitrages.
- Product Data Owner : définitions, statuts et qualité des références de produits.
- Vehicle Data Owner : catégories, identifiants de référence et règles de mise à jour.
- Compliance : exigences de vérification et approbation des étapes sensibles.
- Distribution : besoins des canaux et usage opérationnel des APIs.
- Delivery IT : design, intégration, erreurs, télémétrie et mise en production.
- UAT Owners : preuve d'acceptation des cas nominaux et négatifs.

## 5. Référentiel Produit
Champs pédagogiques : ProductId, ProductFamily, AvailabilityStatus, ValidFrom, ValidTo, Version, Owner. Aucun taux, limite financière ou condition d'éligibilité réelle n'est fourni. Les règles de décision produit doivent être définies et validées par les équipes habilitées.

## 6. Référentiel Véhicule
Champs pédagogiques : VehicleRefId, Category, BrandCodeExample, ModelCodeExample, EnergyCategory, ValidFrom, Version. L'exemple ne prétend pas reproduire un inventaire constructeur ou un référentiel réellement utilisé.

## 7. Contrats API et flux
Décrire les endpoints de consultation, les consommations par application, les formats de réponse, les règles de pagination, les codes d'erreur, les stratégies de cache et la version de référence. Les URL de l'exemple sont fictives et n'indiquent aucun système réel.

## 8. Parcours crédit et conformité
Les contrôles d'identité, KYC et AML sont représentés par des **portes génériques de validation**. Leur contenu exact, séquence et responsabilité doivent être approuvés par les fonctions concernées. Un contrôle de conformité ne doit jamais être remplacé par une simple automatisation documentaire.

## 9. Optimisation Lean Six Sigma
Pour chaque étape : mesurer la ressaisie, les retours en arrière, le temps de traitement, les erreurs de référentiel et les attentes inter-équipes. Formaliser problème, cause, solution, hypothèse de gain, preuve et indicateur avant/après.

## 10. Exigences fonctionnelles types
- BRQ-01 : un consommateur peut retrouver une référence valide et sa version.
- BRQ-02 : une référence retirée ne peut être proposée comme active.
- BRQ-03 : les erreurs API sont explicites et traçables sans exposer de données personnelles.
- BRQ-04 : l'utilisateur retrouve l'état d'une demande et ses pièces autorisées.
- BRQ-05 : un contrôle nécessitant validation humaine ne peut être marqué « passé » par inférence.

## 11. DMS et gouvernance documentaire
Distinguer documents approuvés, pièces associées à un dossier, modèles, versions précédentes et éléments techniques. Définir famille, type, référence, propriétaire, statut, classification et durée de conservation. Les habilitations et les durées sont à approuver, non présumées.

## 12. Backlog, user stories et recette
Une user story réunit objectif, dépendances, données de référence, règles métier, critère d'acceptation, test positif/négatif et décision de Product Owner. Relier chaque story à une exigence et à un scénario UAT. Les items bloqués restent visibles avec owner et dépendance.

## 13. Priorisation et livraison
Prioriser les contrôles réglementaires, dépendances inter-applicatives, qualité des données et besoins de distribution. Prévoir une validation par sprint ou incrément, des jeux de tests fictifs, un plan de retour arrière et un passage RUN contrôlé.

## 14. Questions ouvertes et limites
Confirmer les contrats API et leurs propriétaires, le catalogue des produits et véhicules réellement autorisé, les règles de conformité, le modèle d'accès documentaire, la rétention, les métriques de performance et la stratégie de synchronisation. Aucun de ces éléments n'est affirmé au nom d'une entreprise.