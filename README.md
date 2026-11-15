# Field Notes website

Static site generated from the `_publications` collection. Publication entries
use YAML front matter with `title`, `venue`, `year`, `authors`, `paperurl`,
`citation` and an optional `codeurl`.

The `projects/` folder contains the per-project release workspaces referenced by
the publication entries. The release activity page is rendered from
`_data/sync_messages.json`, which is regenerated from the raw assistant capture
in `_data/sync_raw.jsonl`.
