# System Cleaner

![Python version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/system-cleaner)

## Description

This project is a Python-based system cleaner tool that removes temporary files from your system. It allows users to clean their system's temporary files while providing detailed feedback about the files deleted and those that couldn't be removed due to being in use by other processes.

The tool is interactive, and it includes an intuitive terminal-based menu system.

## Features

- **Clean Temporary Files**: Removes unwanted temporary files from your system.
- **Detailed Logs**: Logs the files that were successfully cleaned and any files that couldn't be cleaned (e.g., because they were in use).
- **Excludes Critical Files**: Automatically excludes system directories and important files to ensure safety.

## Install required dependencies:

The tool requires the rich library for styling terminal output. Install it using pip:

```bash
pip install rich
```
## Disclaimer

**This script is very basic.** It is intended for educational purposes and might not cover all edge cases. It is advised to use it with caution and verify the files it deletes before running it in a production environment.
