# vector-primitives

`Vector2/3/4`, `Matrix4`, `AxisAngle`, `Polygon2/3` geometry helpers.

KotOR-specific `SurfaceMaterial` / `Face` walkmesh types are **not** included.

Optional: install `pyglm` or `glm` for GLM-backed bases.

## Name note

GitHub repo remains `python-vectors`. The **PyPI distribution name** is `vector-primitives` because [`python-vectors`](https://pypi.org/project/python-vectors/) is already taken (unrelated 2D/3D point library by Foster Reichert).

Import as `vector_primitives`.

## Install

```bash
pip install -e .
# or eventually: pip install vector-primitives
pip install pyglm  # optional
```

## Origin

Sliced from PyKotor `utility/common/geometry.py`.

## License

LGPL-3.0-or-later
