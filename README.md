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



## 🚀 Getting Started

### A. Install dependencies

1. Build virtual enviornment
```bash
python -m venv venv
```

2. Activate venv
```bash
# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

3. Upgrade pip to latest if needed
```bash
python.exe -m pip install --upgrade pip
```

4. install requirements
```bash
pip install -r requirements.txt
```

### B. Clone the repository and Run the script

```bash
git clone https://github.com/GCwenmoon/ui-testing-playground.git
cd ui-testing-playground
```

Run the test
```bash
python -m pytest tests/test_ui_playground.py -v
```


## 📋 Implemented Test Case
All tests are located in tests/test_ui_playground.py and cover various UI challenges from the playground site:

- Dynamic ID
- Class Attribute
- Hidden Layers
- And more…