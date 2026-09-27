# AI/ML Project Templates

These are **templates**, not runnable code — the pipeline files lay out
the steps as numbered comments so you can fill in the actual logic for
your own project. `config/config_template.yaml` and
`logging_template.py` are the two exceptions with real, working code,
since they're reusable across almost any project as-is.

## Folder structure

```
ai_ml_project_templates/
├── config/
│   └── config_template.yaml     # paths, logging settings, dataset locations
├── docs/
│   └── README.md                # this file
├── data/
│   ├── raw/                     # original, untouched input files
│   ├── processed/                # cleaned/encoded files, ready for modeling
│   └── output/                   # final predictions
├── logs/                         # log files land here (timestamped, gitignored)
├── training/
│   ├── preprocessing_template.py # raw -> clean, model-ready data
│   └── training_template.py      # train, compare, and save models
├── inference/
│   └── inference_template.py     # load a saved model, score new data
└── logging_template.py           # shared logger, used by every script above
```

## Suggested flow

```
config/config_template.yaml
        │
        ▼
training/preprocessing_template.py   →  data/processed/ (training set)
        │
        ▼
training/training_template.py        →  model + metrics artifacts
        │
        ▼
training/preprocessing_template.py again (on new/incoming data)
        │
        ▼
inference/inference_template.py      →  data/output/predictions
```

`logging_template.py` sits at the project root because both
`training/` and `inference/` scripts need it — each template file has
a note at the top on how to import it (add the project root to
`sys.path`, or turn this into a proper installable package later on).

## Notes on what was fixed from the original draft

- `config_template.py` was actually YAML content — renamed to
  `config_template.yaml` so it opens/parses correctly.
- `logging_template.py`'s file handler used `os.mkdir()`, which throws
  an error if the log folder's parent doesn't already exist. Changed to
  `os.makedirs(..., exist_ok=True)`.
- Removed the leftover top-level code that loaded a config and wrote a
  log message the moment the file was imported — that's now shown only
  as a commented-out example at the bottom, so importing `_set_logger`
  elsewhere has no side effects.
- Added a note in `config_template.yaml` about `${core.xxx}`
  placeholders: plain YAML loaders (like PyYAML) don't resolve these
  automatically — you'll need to either hardcode the path or use a
  config library that supports interpolation (e.g. OmegaConf).
- Added a note about reusing the same fitted encoders between training
  and inference, since re-fitting an encoder on new data is a common
  source of subtle bugs (mismatched encodings between train and
  inference).
