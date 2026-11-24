---
title: ComfyFactorio Documentation
aliases:
  - docs
  - index
tags:
  - factorio
  - scenario
  - mountain-fortress
  - documentation
---

# ComfyFactorio — Documentation

> [!note] Scope
> This documentation focuses on the **Mountain Fortress v3** scenario
> (`maps/mountain_fortress_v3/`) and the code it depends on. It describes **how
> things work** and **how to use/host** them.

This vault documents the [ComfyFactorio](../readme.md) repository — a community
collection of custom Factorio **scenarios** (not mods), built and maintained by
the Comfy community.

## Index

- [[architecture]] — repo layout, the runtime `require` system, the `utils/`
  framework, `modules/`, `maps/`, and templates.
- [[hosting]] — how to enable, host, and run Mountain Fortress v3; CI; commands.
- [[mountain_fortress/overview]] — what the scenario is, the core gameplay loop,
  and how a session is wired together.
- [[mountain_fortress/systems]] — per-file deep dive: terrain generation, state,
  economy, loot, markets, traps, wave defense, highscores, soft-reset.
- [[mountain_fortress/submodules]] — the `ic`, `icw`, `locomotive`, and
  `stateful` sub-packages.
- [[mountain_fortress/dependencies]] — the reusable `modules/` this scenario
  builds on and how it configures each one.

## Quick facts

- **Language:** Lua, running as a Factorio **scenario** (loaded via
  `control.lua`).
- **Entry point:** [[architecture#how-a-scenario-boots|control.lua]] — exactly
  one map is enabled via a single `require` line.
- **Mountain Fortress v3** lives in
  `maps/mountain_fortress_v3/` and requires the **MtnFortressAddons** mod.
- **The train is the base.** The locomotive's health is the win/loss condition.

## Related

- [[architecture]]
- [[hosting]]
- [[mountain_fortress/overview]]
