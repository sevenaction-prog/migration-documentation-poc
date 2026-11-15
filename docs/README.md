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
