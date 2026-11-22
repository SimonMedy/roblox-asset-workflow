# Roblox Asset Workflow — Guide français

Skill Agent Skills pour créer des **assets Roblox aboutis** : modèles Blender, pièces interchangeables, UV/skins, cosmétiques à raretés, VFX natifs et préparation SFX. Créativité libre, qualité réelle et références chargées à la demande. **Ce n'est pas encore un skill de développement de jeu complet.**

## Installation

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

Installation globale pour Claude Code, Codex et Gemini CLI :

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Node.js et un agent compatible sont nécessaires. Blender, Blender MCP et Roblox Studio MCP sont des outils séparés.

## Ce qui change en v3.2.0

- **Raretés et direction artistique :** items communs soignés, mythiques mémorables, identité et lisibilité à distance de match. Prototyper un seul item héros avant la collection.
- **Skins émissifs :** `EmissiveMaskContent` doit être préconfiguré avec les autorisations appropriées (`PluginSecurity`) ; `EmissiveStrength` et `EmissiveTint` peuvent réagir au gameplay sur un motif fixe. Ils ne font pas défiler les UV.
- **VFX :** auras, boosts, flipbooks, `ParticleEmitter`, `Beam`, `Trail` et meshes 3D. Transparence propre, animation stable, surcharge visuelle évitée et profilage avec plusieurs joueurs / sur mobile.
- **Audio :** SFX originaux/licenciés, attaque, boucle, relâchement, variation maîtrisée et intégration Roblox.
- **Qualité Pass/Fail :** refuser les défauts visuels réellement observés ; signaler `UNVERIFIED` pour tout import, test multijoueur ou mobile non réalisé.

## Principes préservés

- Modèles originaux ou fidèles aux références, sans détruire les régions approuvées.
- Pièces interchangeables, pivots, UV/masques et coloris personnalisables.
- **20 000 triangles maximum par mesh standard importé** ; les avatars peuvent imposer d'autres règles. Ce plafond ne garantit pas les performances.
- `HQ` éditable, `GAME` réellement exporté et inspecté, `MOBILE` facultatif selon la cible.
- Sauvegardes versionnées, pas de modification silencieuse des hitboxes ou de la physique.

## Références et outils

Lire `SKILL.md`, puis uniquement les fiches nécessaires dans `references/` :
[skins](references/skins.md) · [raretés](references/rarity-and-art-direction.md) · [VFX](references/vfx-roblox.md) · [audio](references/audio-sfx.md) · [export/QA](references/roblox-export.md).

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
blender -b your_asset.blend --python scripts/audit_blender.py -- --collection Vehicle_GAME --output asset-audit.json
python scripts/audit_glb.py path/to/Vehicle_GAME.glb --strict --output reports/glb-audit.json
```

Les audits sont des précontrôles : seule la vérification dans Roblox Studio et sur les appareils/joueurs ciblés établit le fonctionnement final. Voir [publier](docs/PUBLISHING.md) et [historique](CHANGELOG.md).
