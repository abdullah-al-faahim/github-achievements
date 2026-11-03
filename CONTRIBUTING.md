# Contributing

Thanks for helping keep this guide accurate! 🙌

## Reporting a change

Open an issue that includes:
- The achievement or highlight name
- What changed (new badge, new threshold, different trigger)
- **Evidence**: a profile link, a screenshot, or a GitHub changelog/docs link

## Editing the guide

1. Fork the repo and create a branch.
2. Update thresholds or names in [`data/achievements.json`](data/achievements.json).
3. Regenerate the banner and check every badge URL still resolves:
   ```bash
   python scripts/generate_badges.py
   ```
4. Update the matching page in [`achievements/`](achievements) and the tables in [`README.md`](README.md).
5. Open a pull request. Co-authoring with a friend gets you a little closer to Pair Extraordinaire 😉

## Style

- Keep steps short and practical.
- Mark anything unverified as **unconfirmed**.
- Link GitHub's official badge images from `github.githubassets.com`. Don't commit copies of them to the repo.
