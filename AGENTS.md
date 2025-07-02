 Context & Objective
Prompt:

“I have an existing command-line benchmarking tool called SWE-Bench. Help me design an application with a graphical user interface that lets users select tests, run benchmarks, and view results interactively. Outline the overall workflow.”

2. User & UX Requirements
Prompt:

“List the key user personas (e.g. DevOps engineer, QA analyst) and their main use cases for the SWE-Bench GUI. For each persona, describe their primary tasks, pain points, and how the GUI can solve them.”

3. Wireframes & Navigation Flow
Prompt:

“Sketch out the screen hierarchy and navigation flow for the GUI: home/dashboard, test configuration, execution monitor, results viewer, and settings. Describe what each screen shows and how users move between them.”

4. Technology Stack & Frameworks
Prompt:

“Recommend a tech stack for building the SWE-Bench GUI. Compare desktop options (e.g. Electron, Qt) versus web-based (React, Vue) approaches, citing pros and cons for integration with the existing CLI tool.”

5. Integration with SWE-Bench CLI
Prompt:

“Explain how the GUI can invoke the existing SWE-Bench binary or library under the hood. Cover argument passing, environment setup, capturing stdout/stderr, and parsing output into structured data.”

6. Data Modeling & Storage
Prompt:

“Design a simple data model for storing benchmark runs and results. Include entities like TestSuite, RunMetadata, Metric, and UserSettings. Suggest a lightweight storage solution (e.g. SQLite, JSON files) and explain why.”

7. Results Visualization
Prompt:

“Propose a set of visualizations—charts, tables, timelines—to display benchmark metrics (e.g. execution time, memory usage). Recommend libraries (e.g. Chart.js, D3) and describe how the GUI updates these in real time or on demand.”

8. Configuration & Preferences
Prompt:

“Outline how users will configure test parameters and global settings. Include things like selecting target code paths, setting iterations, threshold alerts, and storing presets for later reuse.”

9. Packaging & Distribution
Prompt:

“Suggest a packaging strategy for distributing the GUI app to users on Windows, macOS, and Linux. Cover bundling the SWE-Bench executable, automatic updates, and installer creation.”

10. Testing & Quality Assurance
Prompt:

“Define a testing plan for the GUI wrapper: unit tests for frontend components, integration tests that run actual benchmarks, and end-to-end tests simulating a user workflow. Recommend frameworks or tools.”

11. Deployment & User Feedback
Prompt:

“Plan a beta release process: how to gather user feedback, log crash reports, and iterate on UI/UX improvements. Suggest metrics to track adoption and satisfaction.”
