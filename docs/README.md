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
