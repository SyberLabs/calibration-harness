# Calibration history

This branch holds the paperweight calibration harness's baseline history
(packages/calibrate on master). CI appends to it when a pull request that
changes the prompt is merged; nothing here is ever merged into master.

- `history.jsonl` and `runs/`: real accepted runs, one line and one folder each.
- `synthetic/history.jsonl` and `synthetic/runs/`: SYNTHETIC runs from the Lua
  shim and the synthetic set. They demonstrate the replay job until a real
  baseline exists, and a real baseline lookup never reads them.
