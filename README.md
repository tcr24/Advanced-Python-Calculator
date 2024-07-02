# Advanced Python Calculator

## Overview

This project is an advanced Python-based calculator application designed for a Software Engineering Graduate Course. It showcases professional software development practices including clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Features

- Arithmetic operations (Add, Subtract, Multiply, Divide)
- Calculation history management with Pandas
- Plugin system for extended functionalities
- Comprehensive logging
- Command-line interface (REPL)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Advanced-Python-Calculator.git
   cd Advanced-Python-Calculator
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install pandas pytest pylint
Usage
Run the REPL:

bash
Copy code
python src/repl.py
Available commands:

add <a> <b>: Adds a and b.
subtract <a> <b>: Subtracts b from a.
multiply <a> <b>: Multiplies a and b.
divide <a> <b>: Divides a by b.
save <filename>: Saves the calculation history to filename.
load <filename>: Loads the calculation history from filename.
plugins: Lists available plugins.
exit: Exits the calculator.
Design Patterns
Facade Pattern
The CalculatorFacade class provides a simplified interface for performing operations using the Calculator class.

Code: CalculatorFacade in src/calculator.py
Description: This pattern simplifies the interaction with the calculator by providing a unified interface for the arithmetic operations.
Command Pattern
The REPL class handles various commands and organizes them effectively.

Code: REPL in src/repl.py
Description: This pattern organizes the commands within the REPL, enabling clean and maintainable command execution.
Plugin System
The PluginManager class dynamically loads new commands or features without modifying the core application.

Code: PluginManager in src/plugin_manager.py
Description: This system enables the addition of new functionality through plugins without modifying the core application.
Environment Variables
Environment variables are used to configure logging levels dynamically.

Code: logging configuration in src/calculator.py
Description: The logging level can be set via the LOGGING_LEVEL environment variable, allowing dynamic control over the verbosity of log messages.
Logging
Comprehensive logging is implemented to record detailed application operations, data manipulations, errors, and informational messages.

Code: logging configuration in src/calculator.py
Description: Logging is set up using Python's logging module, with messages differentiated by severity (INFO, WARNING, ERROR).


##Exception Handling
The application uses try/catch blocks to handle exceptions, demonstrating both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches.

LBYL Example:

Code: divide method in src/calculator.py
Description: The code checks for potential issues before attempting an operation (e.g., checking for zero before division).
EAFP Example:

Code: load_history method in src/calculator.py
Description: The code attempts operations directly and catches exceptions if they occur (e.g., handling file I/O errors).


##Continuous Integration
GitHub Actions is used for continuous integration, ensuring that all tests pass on every push and pull request.

CI Configuration: .github/workflows/python-app.yml


##Tests

Tests are written using pytest and can be run with:
pytest

##Video Demo
