# Roblox Asset Workflow — Guide français

Skill Agent Skills pour créer et perfectionner des assets Roblox avec Blender, Blender MCP (facultatif) et des agents IA compatibles. **Créativité libre, fidélité aux références, qualité de l'export réel.**

## Installation

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

Installation globale pour Claude Code, Codex et Gemini CLI :

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Il faut Node.js et un agent compatible. Blender et ses MCP s'installent séparément.

## Exigences

- Modèles originaux ou fidèles à tes références ; jamais de modification silencieuse d'une partie validée.
- Pièces interchangeables, pivots cohérents, UV/masques pour skins et couleurs personnalisées.
- **20 000 triangles au maximum par mesh individuel importé** ; l'optimisation globale exige aussi des mesures de performance.
- Profils `HQ` éditable, `GAME` exportable et `MOBILE` facultatif.
- Inspection rapprochée du **vrai niveau GAME**, pas seulement de la version HQ ; test magenta interne facultatif contre les micro-jours sur véhicules fermés.
- Préférence pour un matériau par pièce personnalisable. Vérification des UV `[0,1]` destinées aux livrées. Ne pas compter sur les noms de pièces générés automatiquement à l'import.
- Sauvegardes versionnées et aucun changement automatique des hitboxes ou scripts existants.

## Audits

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
blender -b your_asset.blend --python scripts/audit_blender.py -- --collection Vehicle_GAME --output asset-audit.json
python scripts/audit_glb.py path/to/Vehicle_GAME.glb --output glb-audit.json
```

L'audit Blender exclut les objets masqués par défaut (option `--include-hidden` pour les inclure) et propose `--collection` pour ignorer le décor studio. L'audit `.glb` fonctionne sans Blender. Tous deux sont des contrôles préliminaires : il faut encore vérifier l'import réel dans Roblox Studio, les matériaux, les pivots et les performances sur appareil cible.

Consulte [`references/roblox-export.md`](references/roblox-export.md), [`docs/PUBLISHING.md`](docs/PUBLISHING.md) et [`CHANGELOG.md`](CHANGELOG.md).
