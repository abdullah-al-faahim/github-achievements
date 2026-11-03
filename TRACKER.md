# 📋 Achievement tracker

Copy this into your own notes, issue or profile README and tick boxes as you go.
Check your current badges at `https://github.com/<your-username>?tab=achievements`.

## Active

### <img src="assets/badges/starstruck.svg" width="22"> Starstruck
- [ ] Default: 16 stars on one repo
- [ ] 🥉 Bronze: 128 stars
- [ ] 🥈 Silver: 512 stars
- [ ] 🥇 Gold: 4,096 stars

### <img src="assets/badges/pull-shark.svg" width="22"> Pull Shark
- [ ] Default: 2 merged PRs
- [ ] 🥉 Bronze: 16 merged PRs
- [ ] 🥈 Silver: 128 merged PRs
- [ ] 🥇 Gold: 1,024 merged PRs

### <img src="assets/badges/pair-extraordinaire.svg" width="22"> Pair Extraordinaire
- [ ] Default: 1 merged PR with a coauthored commit
- [ ] 🥉 Bronze: 10
- [ ] 🥈 Silver: 24
- [ ] 🥇 Gold: 48

### <img src="assets/badges/galaxy-brain.svg" width="22"> Galaxy Brain
- [ ] Default: 2 accepted answers
- [ ] 🥉 Bronze: 8
- [ ] 🥈 Silver: 16
- [ ] 🥇 Gold: 32

### Single-tier
- [ ] <img src="assets/badges/quickdraw.svg" width="22"> Quickdraw: close an issue/PR within 5 minutes
- [ ] <img src="assets/badges/yolo.svg" width="22"> YOLO: merge a PR without a review
- [ ] <img src="assets/badges/public-sponsor.svg" width="22"> Public Sponsor: sponsor someone publicly

## Highlights
- [ ] PRO
- [ ] Developer Program Member
- [ ] Security Bug Bounty Hunter
- [ ] Security Advisory Credit
- [ ] GitHub Campus Expert
- [ ] GitHub Star

**Total possible today:** 7 achievements · 19 achievement levels (4 × 4 tiered + 3 single) · 6 earnable highlights

## Check your progress from the terminal

```bash
# merged PRs you've authored (Pull Shark)
gh search prs --author @me --merged --limit 1000 --json url --jq length

# your most-starred repo (Starstruck)
gh repo list --limit 200 --json name,stargazerCount --jq 'max_by(.stargazerCount) | "\(.name): \(.stargazerCount) ★"'
```

[← Back to README](README.md)
