# AGENT.md

You are to build a GUI wrapper application around the existing SWE-Bench CLI tool

## 1. Context & Objective

* **Goal**: Create a GUI application that integrates with the existing SWE-Bench CLI.
* **Task**: full end-to-end workflow from launching the GUI to visualizing results.

## 2. User & UX Requirements

* **Identify Personas**:
  - DevOps Engineers
  - QA Analysts
  - Developers
  - Team Leads
  - SWE-Bench Maintainers

* **Persona Details**:
  - **DevOps Engineers**:
    - *Primary Tasks*: Configure and automate test pipelines; integrate SWE-Bench into CI/CD workflows.
    - *Pain Points*: Manual CLI configurations; environment setup complexity; lack of pipeline visibility.
    - *GUI Solutions*: Guided configuration wizards; environment presets; pipeline status dashboard.
  - **QA Analysts**:
    - *Primary Tasks*: Execute test suites; analyze test coverage and results; generate reports.
    - *Pain Points*: Parsing verbose CLI output; manual report generation; filtering results.
    - *GUI Solutions*: Interactive result filters; real-time execution graphs; one-click report exports.
  - **Developers**:
    - *Primary Tasks*: Perform local test runs; debug performance regressions; profile metrics.
    - *Pain Points*: Complex CLI options; difficulty visualizing metrics; repetitive commands.
    - *GUI Solutions*: Preset configurations; inline metric visualizations; quick-run shortcuts.
  - **Team Leads**:
    - *Primary Tasks*: Oversee test health; track project metrics; share results with stakeholders.
    - *Pain Points*: Aggregating results across runs; generating summaries; lack of centralized dashboard.
    - *GUI Solutions*: High-level dashboards; exportable summary reports; role-based access views.
  - **SWE-Bench Maintainers**:
    - *Primary Tasks*: Maintain and update SWE-Bench; analyze user adoption; provide support.
    - *Pain Points*: User misconfigurations; troubleshooting environment issues; limited usage insights.
    - *GUI Solutions*: Built-in validation and tips; environment diagnostics; anonymized usage telemetry.

## 3. Wireframes & Navigation Flow

* **Screen List**:
  - Dashboard
  - Test Configuration
  - Execution Monitor
  - Results Viewer
  - Settings

* **Navigation Flow & Wireframes**:
  ```txt
  Dashboard
     ├── Test Configuration
     │     └── Execution Monitor
     │           └── Results Viewer
     └── Settings
  ```
  - **Dashboard**: Entry point showing project summaries and recent runs.
  - **Test Configuration**: Form-like interface to select suites, parameters, and presets.
  - **Execution Monitor**: Live log streaming, progress bars, run metadata.
  - **Results Viewer**: Interactive charts, metric tables, export controls.
  - **Settings**: Global preferences for CLI path, environment, theme, and storage.
  - **Navigation Paths**: Start at Dashboard, branch to Test Configuration or Settings; from Test Configuration launch runs in Execution Monitor, then view results in Results Viewer; Results Viewer can return to Dashboard or Test Configuration.

## 4. Technology Stack & Frameworks

* **Compare Options**:
  - **Electron (with React/Vue)**:
    - *Pros*: Cross-platform desktop support; rich ecosystem; easy Node.js CLI integration.
    - *Cons*: Larger bundle size; higher memory usage.
  - **Qt (C++/QML)**:
    - *Pros*: Native performance; smaller footprint; mature cross-platform support.
    - *Cons*: C++ learning curve; more complex build; limited JS ecosystem.
  - **Web-based (React/Vue without Electron)**:
    - *Pros*: Lightweight; deployable to browsers; continuous updates.
    - *Cons*: Requires server or local HTTP; limited native OS integration.
* **Recommendation**: Electron + React — balances CLI integration ease, cross-platform desktop support, and UI ecosystem familiarity.

## 5. Integration with SWE-Bench CLI

* **Invocation Method**: Use Node.js `child_process.spawn` to launch the SWE-Bench CLI as a subprocess.
* **Argument Handling**: Collect GUI form inputs, validate against a schema, assemble CLI arguments array, and pass to spawn.
* **Environment Setup**: Merge system environment with user-defined variables; allow presets and overrides in Settings.
* **Output Capture**: Stream `stdout`/`stderr` line-by-line into the Execution Monitor; tag lines as info, warning, or error.
* **Parsing**: Detect JSON-formatted output (e.g., via `--output json` flag); use `JSON.parse` for structured metrics or fallback to regex parsing for legacy text.

## 6. Data Modeling & Storage

* **Entities & Attributes**:
  - **TestSuite**: id, name, description, default parameters, tags.
  - **RunMetadata**: runId, timestamp, suiteId, parameters, status, duration.
  - **Metric**: runId, metricName, value, unit, timestamp.
  - **UserSettings**: cliPath, envVars, theme, recentProjects, defaultPresets.
* **Storage Engine**: JSON files stored in a user-configurable workspace directory.
* **Schema**:
  ```txt
  UserSettings
      ↳ TestSuite (1..*)
           ↳ RunMetadata (1..*)
                ↳ Metric (0..*)
  ```

## 7. Results Visualization

* **Visualization Types**:
  - Line charts for metrics over time.
  - Bar graphs for comparing runs.
  - Scatter plots for correlation analysis.
  - Timeline views for run events.
  - Data tables for raw metric inspection.
  - Dashboard cards for summary KPIs.
* **Library Suggestions**: Recharts (React), D3.js for custom visualizations, Chart.js for quick embeddable charts.
* **Update Strategy**: Real-time chart updates during Execution Monitor for streaming metrics; snapshot rendering in Results Viewer after run completion.

## 8. Configuration & Preferences

* **Test Configuration UI**: Dropdown selectors for TestSuite, parameter inputs (text/number/range), threshold sliders, and preset management (save/load).
* **Global Settings UI**: Inputs for CLI executable path, environment variable editor, theme switcher (light/dark), and workspace directory picker.
* **Persistence**: Save user settings and presets to the UserSettings JSON; auto-load on application launch.

## 9. Packaging & Distribution

* **Platforms**: Windows, macOS, Linux.
* **Packaging Tools**: Electron Builder for cross-platform installers (NSIS for Windows, DMG for macOS, AppImage for Linux).
* **Auto-Update**: Electron-Updater integrated with GitHub Releases.
* **Bundling**: Include platform-specific SWE-Bench binaries in the installer; fallback to external CLI if not bundled.

## 10. Testing & Quality Assurance

* **Test Levels**:
  - Unit tests for UI components (Jest + React Testing Library).
  - Integration tests for CLI invocation (Mocha/Chai with mocked `child_process`).
  - End-to-end tests (Playwright/Cypress) simulating user workflows.
  - Smoke tests for basic launch and CLI bundling.
* **CI Integration**: GitHub Actions pipeline running lint, unit tests, integration tests, and end-to-end tests in a matrix on Windows, macOS, and Linux.

## 11. Deployment & User Feedback

* **Beta Process**: Distribute nightly/beta builds via GitHub Releases with version tags.
* **Feedback Channels**: In-app feedback form sending optional logs; GitHub issue template for bugs/enhancements.
* **Error Reporting**: Capture unhandled errors with Sentry (opt-in user consent).
* **Analytics**: Opt-in telemetry (e.g., screen usage events, run counts) collected anonymously respecting privacy.
* **Metrics**: Track adoption (active installs), stability (crash/error rate), engagement (features used), and satisfaction (in-app ratings).

---

> *Use this AGENT.md as the single source of truth for automating of the SWE-Bench GUI application.*
