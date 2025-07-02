# FullyautoOpenAI
Fully autonomous repository with OpenAI Codex

pipeline will build anything you defined in AGENTS.md and push to the repo

## SpecFlow LivingDoc Workflow

This workflow runs SpecFlow high-level tests and generates a LivingDoc HTML report published via GitHub Pages.

- **Tests directory:** `tests/HighLevelTests`
- **Features:** `tests/HighLevelTests/Features`
- **Step definitions:** `tests/HighLevelTests/Steps`
- **Report output:** `docs/livingdoc.html`

Make sure to configure the repository secret:
- **G_TOKEN:** GitHub token with permission to push to `gh-pages`.

You can also generate the LivingDoc HTML report locally by running:
```bash
bash scripts/generate_livingdoc.sh
```

-----------------------------------------------------------------------------------



in settings/secrets/actions set repository secrets G_TOKEN (github token) and OPENAI_API_KEY
