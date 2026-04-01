# UI Testing Playground

A practical **UI Test Automation** demo project built with Python, designed to practice testing on the popular training website:

**[UI Test Automation Playground](http://uitestingplayground.com/)**

This repository demonstrates how to automate various challenging UI elements and interactions commonly found in real-world web applications.

## ✨ Purpose

- Learn and practice UI automation techniques
- Demonstrate solutions for tricky UI scenarios (Dynamic IDs, AJAX, Hidden Layers, etc.)
- Serve as a clean reference project for learning and technical interviews

## 🛠️ Tech Stack

- **Language**: Python 3
- **Testing Framework**: Playwright, pytest
- **Test Site**: [http://uitestingplayground.com](http://uitestingplayground.com/)

## 📋 Implemented Test Case
All tests are located in tests/test_ui_playground.py and cover various UI challenges from the playground site:

- Dynamic ID
- Class Attribute
- Hidden Layers
- And more…

## 🚀 Getting Started

### A. Installation

1. Install uv
```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux / MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone Repository
```bash
git clone https://github.com/GCwenmoon/ui-testing-playground.git

cd ui-testing-playground
```

3. Build virtual environment
```bash
uv sync --group dev
```

4. Install Playwright Browser
```bash
uv run playwright install
```


### B. Run the tests

Run all tests
```bash
uv run pytest
```

Run all tests with threading
```bash
uv run pytest -n auto
```