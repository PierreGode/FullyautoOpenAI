# AGENT.md

You are to build a GUI wrapper application around the existing SWE-Bench CLI tool

## 1. Context & Objective

* **Goal**: Create a GUI application that integrates with the existing SWE-Bench CLI.
* **Task**: full end-to-end workflow from launching the GUI to visualizing results.

## 2. User & UX Requirements

* **Identify Personas**: DevOps engineers, QA analysts, developers, team leads, and SWE-Bench maintainers.
* **For Each Persona**:

  * Define primary tasks they will perform.
  * List pain points with the CLI.
  * Describe how the GUI features will address those pain points.

## 3. Wireframes & Navigation Flow

* **Screen List**: Dashboard, Test Configuration, Execution Monitor, Results Viewer, Settings.
* **For Each Screen**:

  * Specify key UI components and controls.
  * Explain data displayed.
  * Define navigation paths between screens.
* **Deliverable**: A textual wireframe or ASCII diagram showing screen hierarchy and transitions.

## 4. Technology Stack & Frameworks

* **Compare Options**:

  * Electron vs. Qt for desktop.
  * React/Vue web-based approaches (with or without Electron shell).
* **For Each Option**:

  * List pros and cons, especially CLI integration complexity.
  * Recommend a preferred stack with justification.

## 5. Integration with SWE-Bench CLI

* **Invocation Method**: spawn the SWE-Bench process (e.g., Node child\_process or QProcess).
* **Argument Handling**: Explain building, validating, and passing CLI arguments from the GUI.
* **Environment Setup**: Detail handling of environment variables.
* **Output Capture**: stream stdout/stderr to the UI and tag lines.
* **Parsing**: parsing of structured output (JSON) or fallback to regex parsing.

## 6. Data Modeling & Storage

* **Entities**: TestSuite, RunMetadata, Metric, UserSettings.
* **Attributes**: List fields for each entity.
* **Storage Engine**: JSON files
* **Schema**: Provide a simple ER diagram or table of relational structure.

## 7. Results Visualization

* **Visualization Types**: Line charts, bar graphs, scatter plots, timelines, data tables, dashboard cards.
* **Library Suggestions**: Chart.js, D3.js, Recharts, vis.js.
* **Update Strategy**: use real-time streaming or post-run rendering.

## 8. Configuration & Preferences

* **Test Configuration UI**: Detail selectors for test suites, parameters, thresholds, and presets.
* **Global Settings UI**: Include CLI path, env vars, theme, storage location.
* **Persistence**: decide how settings are saved and loaded.

## 9. Packaging & Distribution

* **Platforms**: Windows
* **Packaging Tools**: Electron-builder (NSIS, DMG, AppImage), AppImage, DEB/RPM. ?
* **Auto-Update**: Electron Updater or Sparkle.
* **Bundling**: SWE-Bench executable per OS.

## 10. Testing & Quality Assurance

* **Test Levels**:

  * Unit tests for UI components (Jest, React Testing Library, Vitest).
  * Integration tests for CLI invocation (Mocha/Chai, pytest-qt).
  * End-to-end tests simulating user workflows (Playwright, Cypress).
  * Smoke tests for basic launch and CLI bundling.
* **CI Integration**: Describe running tests on PRs and nightly builds.

## 11. Deployment & User Feedback

* **Beta Process**: Outline distribution method for beta testers.
* **Feedback Channels**: In-app feedback forms or issue templates.
* **Error Reporting**: Integrate Sentry or similar for crash dumps.
* **Analytics**: Propose opt-in event tracking for runs, screens, and errors.
* **Metrics**: Define adoption, stability, engagement, and satisfaction metrics.

---

> *Use this AGENT.md as the single source of truth for automating of the SWE-Bench GUI application.*
