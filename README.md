# Mechanination

Mechanination is a lightweight biomechanical sprite animation toolkit and research playground. The project includes a Python-based renderer (`primeanim_v4a.py`) that composes a rigged character from image parts, applies biomechanical constraints/presets, interpolates keyframes, and outputs spritesheets. The repository also contains research notes and a separate "Trixel Composer" research area.

## Quick summary
- Language: Python (main renderer)
- Entry point: `primeanim_v4a.py`
- Core concept: rig JSON + animation JSON → composited spritesheet (PNG)
- Primary asset layout: `assets/character_v2/rig/...` (rig and anim JSONs), `assets/.../parts/*.png`

## Features
- CLI renderer that:
  - Loads a rig JSON describing parts and pivots
  - Loads an animation JSON with `duration` and `keyframes`
  - Interpolates poses across frames
  - Applies biomechanical constraints via a unified preset registry
  - Renders layered sprites into a single spritesheet
- Preset-driven biomechanical constraints (preset registry exposed as `BIOMECH_PRESETS`)
- Several example CLI runs and outputs (documented in the repo text files)

## Repository layout (important files / folders)
- `primeanim_v4a.py` — main Python renderer / CLI
- `biomechanical_constraints_fixed.py` — expected import providing `BiomechanicalConstraintsFixed`, `get_preset`, and `BIOMECH_PRESETS`
- `assets/` — example assets, rigs, parts and exported spritesheets (e.g. `assets/character_v2/rig/`)
- `trixel_composer/` — research and notes for a separate Trixel Composer project
- `we got this far.txt` — developer notes, usage examples and rendered-output logs

## Requirements
- Python 3.8+
- Pillow (PIL)

Install the runtime dependency:
```
pip install -r requirements.txt
```

## Usage (examples)
The renderer follows a CLI. The key flags supported by `primeanim_v4a.py`:

- `--rig` (required) — path to rig JSON
- `--anim` (required) — path to animation JSON
- `--frames` — number of frames to render (default 12)
- `--cols` — spritesheet columns (default 4)
- `--size` — pixel size for each frame (default 512)
- `--preset` — locomotion/biomech preset (choices from `BIOMECH_PRESETS`, default `human_balanced`)
- `--out` (required) — output spritesheet path
- `--debug` — enable debug outputs (invariant truth lines, etc.)

Example:
```
python3 primeanim_v4a.py \
  --rig examples/example_rig.json \
  --anim examples/example_anim.json \
  --frames 12 \
  --cols 4 \
  --size 256 \
  --preset human_balanced \
  --out examples/output/example_spritesheet.png
```

## Examples
An `examples/` folder is included with a minimal rig and animation plus a small helper script to generate placeholder part images. See `examples/README.md` for details.

## Troubleshooting
- If you see `⚠️ Error: biomechanical_constraints_fixed.py not found.`, make sure `biomechanical_constraints_fixed.py` is present in the repository root (or adjust the import path). The renderer requires that module to apply presets and constraints.
- If images fail to load, confirm paths in the rig JSON point to existing PNG files in `assets/.../parts/` or `examples/parts/`.
- If animation output looks wrong, try `--debug` to output invariant/truth lines used by the constraint system.

## Development notes & roadmap
- Add a `requirements.txt` and CI checks (done)
- Add a formal JSON Schema for rig and animation files
- Add automated tests for interpolation and constraint application
- Add more examples and integrate a Godot importer

## Contributing
Contributions, bug reports and ideas are welcome. Open an issue, fork, and create a pull request.

## License
No license file was found in the repository snapshot. Add a `LICENSE` (e.g., MIT) to make this project open source.