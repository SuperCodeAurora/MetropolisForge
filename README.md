# 🏗️ MetropolisForge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Forging-orange.svg)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)

> **"Stop ticking boxes. Start building an empire."**

```text
   __  __      _                       _ _      ______
  |  \/  |    | |                     | (_)    |  ____|
  | \  / | ___| |_ _ __ ___  _ __ ___ | |_ ___ | |__ ___  _ __ __ _  ___
  | |\/| |/ _ \ __| '__/ _ \| '_ \ _ \| | / __||  __/ _ \| '__/ _` |/ _ \
  | |  | |  __/ |_| | | (_) | |_) | (_) | | \__ \| | | (_) | | | (_| |  __/
  |_|  |_|\___|\__|_|  \___/| .__/ \___/|_|_|___/|_|  \___/|_|  \__, |\___|
                            | |                                  __/ |
                            |_|                                 |___/
```

**MetropolisForge** is a TUI (Terminal User Interface) productivity engine that transforms your codebase maintenance into an isometric city-building simulation.

Every task you complete is a brick. Every bug you fix reinforces the walls. Every refactor upgrades the power grid.

---

## ⚡ The Concept

Traditional Todo lists are flat and uninspiring. They do not represent the **structure** or **magnitude** of your engineering efforts.

**MetropolisForge** maps your development workflow to urban zoning logic:

| Code Domain | City Zone | Visual Metaphor |
| :--- | :--- | :--- |
| **Backend / Systems** | **The Foundry** | Heavy Industry, Reactors, Smokestacks |
| **Frontend / UI** | **The Neon District** | Glass Skyscrapers, Holo-Ads, Cyberpunk Spires |
| **Documentation** | **The Archives** | Green Parks, Libraries, Data Vaults |
| **Tests / Security** | **The Bastion** | Shield Generators, Turrets, Reinforced Walls |

If you neglect your tests, **The Bastion** crumbles. If you ignore refactoring, **The Foundry** overheats.

---

## 📸 Visualization

```text
 ┌─────────────────────────────────────────────────────────────┐
 │  🏗️  METROPOLIS FORGE v0.1.0                              │
 ├─────────────────────────────────────┬───────────────────────┤
 │  [The Foundry: Backend API]         │  [City Stats]         │
 │                                     │                       │
 │        __                           │  POPULATION: 1,024    │
 │       /  \      [Core Reactor]      │  ENTROPY:    Low      │
 │     _/____\_    Level 5             │  POWER:      Stable   │
 │    / \    / \                       │                       │
 │   /___\  /___\                      ├───────────────────────┤
 │    |  |  |  |                       │  [Overseer's Log]     │
 │   _|_ |__| _|_                      │                       │
 │                                     │  "New auth module     │
 │  [Subway: Unit Tests]               │   deployed. Grid      │
 │  ====================               │   stability +15%."    │
 └─────────────────────────────────────┴───────────────────────┘
```

---

## 🛠️ Installation

**MetropolisForge** is built on the modern Python stack (`Textual` + `Rich`).

```bash
# Clone the repository
git clone [https://github.com/SuperCodeAurora/MetropolisForge.git](https://github.com/yourusername/MetropolisForge.git)
cd MetropolisForge

# Install in editable mode
pip install -e .

# Initialize the Forge
forge init
```

---

## 🎮 Usage

### 1. The Forge (Add Tasks)
Don't just "add a task." **Forge a structure.**

```bash
# Syntax: forge build "<Task Description>" --effort <1-5>

# Example: Building a backend feature
forge build "Refactor the database connection pool" --effort 4
> [SYSTEM] Constructing 'Molten Core Reactor (Mk.4)' in The Foundry...

# Example: Writing documentation
forge build "Update API endpoints documentation" --effort 2
> [SYSTEM] Planting 'Data Tree' in The Archives...
```

### 2. The View (Visualize)
Launch the TUI dashboard to see your city grow in real-time.

```bash
forge view
```

### 3. The Overseer (AI Analysis)
Run the AI architect to analyze your progress.

```bash
forge analyze
> "Overseer Report: Your city has too many Skyscrapers (Features) and not enough Bastions (Tests). Structure is unstable. Recommend immediate reinforcement."
```

---

## 🏗️ Architecture

This project follows a strict **Industrial Grade** directory structure to ensure scalability.

```text
src/metropolis_forge/
├── architect/   # AI Persona & Logic Engine
├── city/        # ASCII Renderer & Zoning Rules
├── forge/       # Task Management & Gamification Math
└── database/    # Async SQLite Persistence Layer
```

---

## 🤝 Contributing

**We accept PRs.**
* **Engineers:** Optimize the `renderer.py` for smoother frame rates.
* **Architects:** Add new building types in `zones.py`.
* **Designers:** Improve the CSS in `assets/metropolis.css`.

Please read `CONTRIBUTING.md` before submitting patches to the grid.

---

## 📄 License

**MIT License**.
Free to build, free to expand.
