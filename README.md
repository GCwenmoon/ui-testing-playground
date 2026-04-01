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



text## 🚀 Getting Started

### 1. Install dependencies

```bash
# build virtual enviornment
python -m venv venv

# activate venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 安裝所需套件
pip install -r requirements.txt

### 2. Clone the repository

```bash
git clone https://github.com/GCwenmoon/ui-testing-playground.git
cd ui-testing-playground
2. Run the tests
Bash# Run all tests
python -m pytest tests/ -v

# Run with detailed output
python -m pytest tests/test_ui_playground.py -v
📋 Implemented Test Cases
All tests are located in tests/test_ui_playground.py and cover various UI challenges from the playground site:

Dynamic ID
Class Attribute
Hidden Layers
And more…