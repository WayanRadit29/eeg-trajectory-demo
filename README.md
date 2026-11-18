# eeg-trajectory-demo

A desktop research demo for continuous 3D wrist trajectory decoding from recorded EEG. The planned demo replays trials from WAY-EEG-GAL and compares predicted wrist positions with recorded ground truth. The 3D scenes use a simulated robot arm and drone swarm to show the trajectory, with EEG traces and model outputs alongside them.

> Offline replay of recorded EEG from healthy subjects (WAY-EEG-GAL). Research demo only, not a medical or assistive device.

## Repository responsibilities

| Repository | Responsibility |
| --- | --- |
| `physio-ssl-trajectory` | Preprocesses data, trains and evaluates models, and will export demo bundles. |
| `eeg-trajectory-demo` | Reads exported bundles and will provide trial playback, inference, and visualization. |

A bundle will carry a manifest, preprocessed trial arrays, precomputed predictions for replay, and any exported model files. The desktop app will use the bundle as its data source. The manifest and trial schema are still proposals to be agreed with the research team.

## Phase 0 status

The Python package, placeholder command, pytest configuration, and smoke tests are available. Bundle loading, EEG playback, inference, and desktop visualization are planned. The scaffold runs independently of a research model or demo bundle.

### Planned architecture

| Package | Planned responsibility |
| --- | --- |
| `bundle` | Validate the manifest and load trials and models. |
| `playback` | Track trial position and issue one inference step per 20 EEG samples (0.2 s at 100 Hz). |
| `inference` | Read precomputed outputs in replay mode or run the exported model in order during playback. |
| `scene` | Display ground truth and predictions in simulated robot arm and drone swarm scenes. |
| `ui` | Connect transport controls, EEG and model state plots, and the 3D view. |

The planned desktop stack uses PySide6, PyVista with `pyvistaqt`, and `pyqtgraph`. Bundles use JSON and NumPy, live model execution during recorded playback uses CPU ONNX Runtime, and Windows packaging uses PyInstaller. GUI testing will use `pytest-qt`. Add these dependencies as the corresponding modules are implemented.

## Local setup and verification

Install Python 3.12 and `uv`, then run these commands from the repository root.

```sh
uv sync
uv run trajdemo
uv run pytest
```

`uv sync` creates the local `.venv` and installs the editable package and its test dependency. The `trajdemo` command prints the Phase 0 status and exits. Pytest verifies that the planned subpackages are importable and that the placeholder entry point runs.

`pyproject.toml` defines the package metadata, build configuration, command, and test settings. With the `src/` layout, `trajdemo` is imported through the installed package. Editable installation makes source edits available immediately.

## Next milestones

1. Agree on the minimum versioned manifest and trial schema with the research team, then create a tiny synthetic bundle for loader tests.
2. Implement bundle loading, playback, and replay of precomputed predictions.
3. Integrate stateful ONNX inference and check that its output matches replay.
4. Add desktop controls, EEG and model state plots, and the two 3D scenes.
5. Package the Windows app and verify it with an exported research bundle when available.

Keep raw datasets under `datasets/` and exported bundles under `demo_bundle/` or `demo_bundles/`, or store them outside the repository. `sample_bundle/` is reserved for small synthetic fixtures.
