# Real Python: Command-Line Interfaces with argparse

This project contains my implementations and outputs from the tutorial **"Build Command-Line Interfaces With Python's argparse"**, published by [Real Python](https://realpython.com/).

## 📚 About This Project

The tutorial walks through how to build **command-line interfaces (CLIs)** using Python's `argparse` module. This project serves as a hands-on reference while following the tutorial, helping me to solidify my understanding of `argparse` by implementing various examples.

I highly recommend going through the tutorial if you're looking to improve your Python CLI development skills!

📖 **Read the full tutorial here:**  
🔗 [Real Python: Build Command-Line Interfaces With Python’s argparse](https://realpython.com/command-line-interfaces-python-argparse/#customizing-your-command-line-argument-parser)

## 🛠 Features & Learning Outcomes

Throughout this project, I have implemented different CLI examples covering:

- Basic usage of `argparse` for handling command-line arguments
- Defining required and optional arguments
- Handling different argument types (strings, integers, choices, etc.)
- Using **flags and boolean arguments**
- Implementing **default values and help messages**
- Structuring CLI applications for readability and maintainability

## 🚀 Running the CLI Applications

To run any of the CLI applications from this project:

1. Clone this repository:

   ```bash
   git clone https://github.com/loughness/CLI-Applications.git
   cd cli-applications/hello_cli
   ```

2. Ensure you have Python installed (version 3.x recommended).

3. Run any script from the command line, for example:

   ```bash
   python3 script_name.py --help
   ```

   This will display the help message for the CLI.

## 📌 Example Usage

Here’s an example command for a script that takes an argument:

```bash
python3 calc.py add 5 10
```

Output:

```
15
```

## 🔧 Dependencies

This project primarily relies on Python’s built-in `argparse` module, so no external dependencies are required.

## 📝 Notes & Reflections

- Following this tutorial gave me a deeper understanding of how to design **user-friendly CLI applications**.
- I learned how to **structure and document CLI applications effectively**.
- This repository may continue to evolve as I explore **more advanced CLI features**.

---

Cheers! 🤙🏻
