# Roblox Asset Workflow — Guide français

Skill universel pour créer des **assets 3D destinés à Roblox** avec Blender et des agents IA : véhicules, environnements, props, UV, skins, pièces interchangeables et exports optimisés. Aucun jeu particulier n'est présupposé ; le style reste libre.

## Installation facile

```powershell
npx skills add SimonMedy/roblox-asset-workflow
```

Pour l'installer globalement dans Claude Code, Codex et Gemini CLI :

```powershell
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

Il faut **Node.js** pour `npx`. Une installation alternative propre à Gemini CLI :

```powershell
gemini skills install https://github.com/SimonMedy/roblox-asset-workflow
```

Ensuite, dis simplement à l'agent : « Utilise `roblox-asset-workflow` et modélise les références jointes dans Blender. » Le MCP Blender ou le MCP Roblox doivent être installés **séparément** ; le skill ne donne pas magiquement accès aux logiciels.

## Règles clés

- **Créativité libre** : pas de style imposé, pas de polygones supprimés arbitrairement.
- **Fidélité aux références** et conservation des parties déjà validées.
- **Séparation des pièces utiles** : roues indépendantes, pivots cohérents, accessoires démontables et zones recolorables.
- **Cosmétiques** : UV et masques pour color picker, skins de carrosserie, textures et animations lorsque la technologie le permet.
- **Limite Roblox** : **20 000 triangles maximum par mesh individuel**, non par voiture entière. Les avatars peuvent avoir des règles plus strictes.
- **Versions** : HQ `.blend` éditable ; GAME export Roblox ; MOBILE plus léger uniquement si utile.
- **Tests** : rendus multiangles, vérification du mesh exporté, puis Roblox Studio et appareil réel pour mesurer les performances.
- **Sauvegardes** : snapshot avant les opérations destructrices.

### Rappel important

Un skin animé complexe ne se fait pas simplement en important un shader Blender dans Roblox : les possibilités d'animation dépendent de l'API Roblox et des appareils ciblés. Le skill prépare la géométrie, les UV et les masques ; la programmation du garage et de ses animations relève du jeu.

## Publication

Lis [`docs/PUBLISHING.md`](docs/PUBLISHING.md). Il explique comment maintenir le dépôt et publier les versions depuis une branche de travail avec Pull Request.
