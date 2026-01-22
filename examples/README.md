# Examples

This folder contains a minimal rig and animation to demonstrate the renderer. A helper script `generate_example_assets.py` will create a small `parts/` directory with placeholder PNGs.

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Generate example assets:

```
python3 examples/generate_example_assets.py
```

This script will create `examples/parts/` PNG files and write `examples/example_rig.json` and `examples/example_anim.json` (already present). After generating assets, run the renderer:

```
python3 primeanim_v4a.py --rig examples/example_rig.json --anim examples/example_anim.json --out examples/output/example_spritesheet.png --size 256
```

If you do not have `biomechanical_constraints_fixed.py` in the repo, the renderer will print an error and exit. You can still use the examples to validate rig/anim shapes and the asset generation flow.
