# Document Atlas — POC de bibliothèque documentaire

POC web public **100 % fictif / anonymisé** pour organiser les modèles de migration documentaire et d'architecture SharePoint / M365.

## Accès
Après déploiement GitHub Pages : https://sevenaction-prog.github.io/migration-documentation-poc/

## Contenu
- `index.html` : interface responsive (filtres par périmètre, format, phase; recherche; aperçus)
- `catalog.json` : référentiel de neuf modèles et sept périmètres génériques
- `templates/` : modèles Office générés par le workflow GitHub Actions, ainsi que les versions CSV / Markdown
- `assets/` : aperçus SVG génériques
- `.github/workflows/pages.yml` : génération des modèles anonymisés + publication du site

**Important :** ne jamais ajouter de données de clients, employés, fournisseurs, chemins réels ou informations confidentielles à ce dépôt public. Tous les fichiers exemples sont synthétiques.

## Activer GitHub Pages
Dans **Settings > Pages**, choisir **GitHub Actions** comme source de déploiement si l'option n'est pas encore active. Le workflow `Deploy Document Atlas` publie ensuite l'interface et les fichiers Office.

## Bibliothèques sectorielles (nouveau)

**Intégration financière institutionnelle** : le guide BA/FA, le mapping des champs, le catalogue des règles et de traçabilité et le registre de handover constituent quatre modèles métier, tous synthétiques.

**Crédit à la consommation et référentiels** : le guide BA/PO, le mapping Produit/Véhicule/API, le backlog Agile et la matrice de gestion documentaire forment quatre modèles métier, tous synthétiques.

Les scénarios sont construits à partir de pratiques professionnelles décrites dans des sources privées consultées lors de la préparation; **aucun CV, document client, compte, règle tarifaire ou dossier réel n'est mis en ligne**. Ils ne sont pas des copies anonymisées de livrables historiques. Les politiques métier, seuils, contrats API, contrôles et règles de conservation restent à obtenir auprès du client concerné.

## Kits projet supplémentaires (BAForge et HeckeGate)

Les six sources remises pour analyse ont été regroupées en trois domaines de capitalisation sans publier le code ni les documents d'origine :

- **AI / Automation BA (BAForge AI)** — guide de delivery en 14 phases (18), registre de qualification/ROI (19), jeu d'évaluation/HITL (20), spécification Prompt/RAG/Eval (21).
- **Documentary Discovery (BAForge Junior et Workshop Companion)** — fiches repository/document (22), workflows/interfaces/décisions (23), guide d'atelier (24).
- **Payment Control Assurance (HeckeGate / PaymentGate)** — matrice des contrôles (25), UAT & evidence chain (26), spécification fonctionnelle (27), registre de validation des allégations (28).

Tous les nouveaux livrables sont générés depuis des sources textuelles **fictives** et ne contiennent ni code source, ni journaux de paiement réels, ni données client. Les affirmations de performance, démonstration mathématique, certifications et conformité doivent être vérifiées par tests indépendants avant toute communication commerciale ou réglementaire. Les documents Word et Excel sont produits par le workflow `scripts/build_office.py` et publiés dans `docs/templates/`.

## Nouveaux kits métier — SCE, DMS, Mission Ops, PMO, Enterprise QA et Android

Les modèles `29` à `48` sont reconstruits en exemples **fictifs** à partir des axes fonctionnels observés dans les huit sources fournies. Il ne s'agit pas de duplications du code ni des jeux de données privés :

- **SCE / Structural Assurance** — guide de preuve des relations (29), modèle des objets (30), invariants/tests (31), constats/remédiations (32).
- **DMS Control Tower** — playbook des dix workshops (33), matrice workshops (34), classification/migration (35), accès/rétention/pilotage (36).
- **Mission Operations** — guide de facturation générique (37), timesheets et contrôles (38), rapprochement des encaissements (39).
- **PMOForge** — guide 14 phases (40), catalogues d'ateliers (41), portefeuille/RAID/bénéfices (42), KPI/maturité/gates (43).
- **Enterprise Fraud Assurance** — architecture de contrôles (44), catalogue des détecteurs (45), registre de validation des performances/allégations (46).
- **Android/TWA** — guide de publication (47), checklist permissions/installation (48). **Le code de l'application web hébergée n'était pas inclus dans l'archive Android : fonctionnalités métier non confirmées.**

### Confidentialité et assurance

Tous les chemins, personnes, organismes, montants, processus, ID, règles et exemples dans les nouveaux modèles sont fictifs. Les numéros contractuels, données bancaires et adresses du prototype de facturation ont été exclus. Les études de performance et affirmations réglementaires du projet Hecke ne sont pas considérées comme indépendamment confirmées.

Le site héberge uniquement les modèles Word/Excel et les sources Markdown/CSV qui servent à les générer via GitHub Actions. Aucune archive projet ni code d'application d'origine n'est publié.
