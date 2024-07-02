# Advanced Python Calculator

## Overview

This project is an advanced Python-based calculator that I developed for my Software Engineering Graduate Course. It highlights important software development practices like writing clean, maintainable code, using design patterns, logging, configuring with environment variables, handling data with Pandas, and providing a command-line interface (REPL) for real-time user interaction.

## Features

- Basic arithmetic operations (Add, Subtract, Multiply, Divide)
- Calculation history management with Pandas
- Plugin system for adding new features
- Comprehensive logging
- Command-line interface (REPL)

# Setup

1. **Clone the repository:**


## Create and activate a virtual environment:

Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Copy code
pip install -r requirements.txt
Usage
Run the REPL:

Copy code
python src/repl.py


## Available commands:

add <a> <b>: 
Adds a and b.

subtract <a> <b>: 
Subtracts b from a.

multiply <a> <b>: 
Multiplies a and b.

divide <a> <b>: 
Divides a by b.

save <filename>: 
Saves the calculation history to filename.

load <filename>: 
Loads the calculation history from filename.

plugins: Lists available plugins.

exit: Exits the calculator.

## Design Patterns

Facade Pattern
The CalculatorFacade class provides a simplified interface for performing operations using the Calculator class.

Code: 
CalculatorFacade in src/calculator.py

This pattern makes it easier to interact with the calculator by providing a unified interface for the arithmetic operations.

Command Pattern
The REPL class handles various commands and organizes them effectively.

Code: 
REPL in src/repl.py

This pattern organizes the commands within the REPL, making it easier to manage and execute commands.

Plugin System
The PluginManager class dynamically loads new commands or features without modifying the core application.

Code: 
PluginManager in src/plugin_manager.py

This system allows new functionalities to be added through plugins without changing the core application.

Environment Variables
Environment variables are used to configure logging levels dynamically.

Code: 
logging configuration in src/calculator.py

The logging level can be set using the LOGGING_LEVEL environment variable, allowing for dynamic control over the verbosity of log messages.

Logging
Logging is implemented to record detailed application operations, data manipulations, errors, and informational messages.

Code: 
logging configuration in src/calculator.py

Logging is set up using Python's logging module, with messages categorized by severity (INFO, WARNING, ERROR).

Exception Handling
The application uses try/catch blocks to handle exceptions, demonstrating both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches.

LBYL Example:

Code: 
divide method in src/calculator.py

The code checks for potential issues before attempting an operation (like checking for zero before division).

EAFP Example:

Code: 
load_history method in src/calculator.py

The code tries operations directly and catches exceptions if they happen (like handling file I/O errors).

Continuous Integration
GitHub Actions is used for continuous integration, making sure that all tests pass on every push and pull request.

CI Configuration: .github/workflows/python-app.yml
Tests
Tests are written using pytest and can be run with:

Copy code
pytest

Video Demonstration
A video demonstration of using the calculator, highlighting its key features and functionalities, can be found here.
