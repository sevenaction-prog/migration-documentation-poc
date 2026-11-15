# Payment Control Assurance — Functional Specification

**Modèle pédagogique fictif inspiré des prototypes HeckeGate / HeckePaymentGate inspectés.** Aucune donnée de paiement réelle, aucune preuve de conformité ni garantie indépendante.

## 1. Objectif
Analyser les séquences de traitement facture/paiement, relever les anomalies structurelles et constituer des traces reproductibles. Séparer détection post hoc, shadow verification et éventuel contrôle préventif inline.

## 2. Modules métiers candidats
- Vérifier une facture et son cycle de commande / réception / rapprochement / approbation / paiement.
- Vérifier un paiement et ses événements d'authentification, autorisation, exécution, règlement et réconciliation.
- Importer une population d'exports CSV, XLSX, JSON, et messages métier structurés si un adaptateur est implémenté.
- Trier les exceptions, conserver un registre de contrôles et exporter des preuves.
- Consulter le mapping contrôle / obligation réglementaire, sous réserve de validation juridique.

## 3. AS-IS / TO-BE
AS-IS fictif : contrôles dispersés, rapprochements et preuves manuels. TO-BE hypothétique : import maîtrisé, normalisation, contrôle structurel, dossier d'exception, re-performance et validation humaine.

## 4. Contrôles
Contrôler inversion d'étapes, étapes manquantes, doublons, replay, synchronisation règlement/comptabilité, erreurs de statut, écarts d'autorisation et de capture. Le contrôle de bénéficiaire s'applique selon le type de paiement et les règles en vigueur, non universellement.

## 5. Règles de qualification
Catégories PASS / REVIEW / BLOCK-CANDIDATE / ERROR. Chaque exception porte identifiant, contexte, événements, règle, preuve et décision du reviewer. Un blocage « candidate » n'est pas un refus bancaire effectif.

## 6. Moteur algébrique
Une réduction sur un modèle 0-Hecke peut servir à canoniser une séquence. Il faut vérifier les hypothèses de mapping, tester la correspondance du code avec la propriété mathématique et auditer la chaîne entrée → algorithme → résultat. Une preuve mathématique de l'algèbre ne prouve ni la véracité du journal ni la correction exhaustive du logiciel.

## 7. Formats d'entrée
Décrire schéma, champs obligatoires, type de rail, dates, montants, IDs, provenance, mapping, erreurs d'import et stratégie de dédoublonnage. Enregistrer la version de l'adaptateur et la transformation appliquée.

## 8. Preuves
Le package de preuve contient entrée normalisée, version moteur, résultat, contrôles exécutés, motifs, horodatage, chaîne de hash et métadonnées de provenance. Les données descriptives non couvertes par le hash doivent être clairement séparées.

## 9. Conservation
Un hash SHA-256 n'établit pas à lui seul une intégrité probante d'origine ; un champ « WORM-ready » n'est pas un stockage WORM effectivement activé. Définir scellement externe, horodatage fiable, rétention, habilitations et re-performance.

## 10. Service shadow versus inline
Un service shadow agit sur des événements observés sans bloquer la transaction réelle. Une intégration inline exigerait une architecture, des règles de fallback, des tests de charge, une disponibilité et une gouvernance opérationnelle distinctes.

## 11. Conformité et limites
Les références PSD3/PSR, VoP, SCA ou DORA doivent être revalidées sur les textes officiels applicables et l'avis juridique. Une console de contrôle structurel n'est ni un service VoP, ni un moteur AML, ni un mécanisme SCA, ni un dispositif complet de détection de fraude.

## 12. UAT et qualité
Tester contrôle positif, inversion, absence, replay, double règlement, import invalide, format de date incohérent, type de paiement non applicable, explication et reproductibilité de chaque résultat. Inclure tests de sécurité et performance mesurée.

## 13. Registre des affirmations
Toute assertion « zéro faux positif », « couverture complète », « garantie mathématique », « prêt pour l'audit » ou « conformité juridique » doit être marquée À VÉRIFIER et associée à un protocole, un corpus, un résultat de test indépendant et un signataire.

## Critères d'acceptation
Chaque verdict s'explique, chaque règle identifie ses données d'entrée et son domaine d'applicabilité, chaque preuve est refaisable sur les mêmes éléments, et aucune revendication réglementaire ne devient CONFIRMÉ sans revue externe.