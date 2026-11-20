# Publish and maintain Roblox Asset Workflow on GitHub

Repository: https://github.com/SimonMedy/roblox-asset-workflow

## Repository workflow

- Use the persistent `develop` branch for all changes, never commit directly on `main`.
- Create a pull request from `develop` to `main`, let GitHub Actions validate it, and merge after successful checks.
- Reuse `develop` for future maintenance; keep it up to date with `main`. The branch is not deleted after merging.
- Keep `SKILL.md` concise and domain guidance in `references/`.
- Update `CHANGELOG.md` for meaningful changes; tag releases on the validated merged commit.

## Install

```bash
npx skills add SimonMedy/roblox-asset-workflow
```

For global installs in selected agents:

```bash
npx skills add SimonMedy/roblox-asset-workflow -g -a claude-code -a codex -a gemini-cli
```

The optional Blender audit is not a substitute for checking imported assets in Roblox Studio and profiling on target devices. Check current platform specs before changing platform-specific limits.

## Security and licensing

- Do not publish private `.blend` projects, game assets without rights, paid textures, account keys or proprietary exports.
- Skills can run scripts: review source before installation and only execute trusted code.
- MIT covers these skill sources, not third-party models or outputs you do not own.
