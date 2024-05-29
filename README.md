# Subdomain Finder

Welcome to the Subdomain Finder project! This repository contains scripts to find subdomains for a given domain. This can be useful for penetration testing, security research, and other network-related tasks.

## Features

- **Automated Subdomain Discovery**: Efficiently finds subdomains of a given domain using various methods.
- **Easy to Use**: Simple command-line interface for quick integration into your workflow.
- **Customizable**: Easily extendable to add more subdomain discovery techniques.

## Prerequisites

- Python 3.x
- `requests` library

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using the following command:
```sh
git clone https://github.com/arifbinekram/Subdomain-Finder.git
cd Subdomain-Finder
```

### 2. Install Dependencies

Install the required Python packages using pip:
```sh
pip install -r requirements.txt
```

### 3. Run the Script

To use the subdomain finder script, follow these steps:

1. Ensure you have a wordlist file named `subdomains_20000.txt` in the same directory as the script. This file should contain potential subdomains, one per line.
2. Run the script:
   ```sh
   python subfinder.py
   ```

3. You will be prompted to enter the target URL. Enter the domain you want to find subdomains for (e.g., `example.com`).

### Example Usage

```sh
python subfinder.py
```

You will see a prompt:
```
Enter the target URL (e.g., example.com):
```
Type in your target domain (e.g., `example.com`) and press Enter. The script will start checking for subdomains and output any discovered subdomains to the console:
```
[+] Discovered subdomain ----> sub.example.com
```

## Repository Structure

- `subfinder.py`: The main script to find subdomains.
- `requirements.txt`: A list of Python dependencies required for the project.
- `README.md`: This README file.

## Script Details

The `subfinder.py` script works as follows:

1. It prompts the user to input the target URL.
2. It reads the `subdomains_20000.txt` file line by line, appending each subdomain to the target URL.
3. It sends HTTP requests to each subdomain and prints out the subdomains that respond successfully.

## Contributing

Contributions are welcome! If you have any improvements or bug fixes, feel free to open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.


## Disclaimer

This project is intended for educational and ethical testing purposes only. Use this tool responsibly and ensure you have permission to test the target domain. Unauthorized use is illegal and unethical.

---

Thank you for using the Subdomain Finder! If you have any questions or feedback, feel free to reach out by opening an issue in the repository.
