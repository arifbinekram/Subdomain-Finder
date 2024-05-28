#!/usr/bin/python3

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# Prompt user for target URL
target_url = input("Enter the target URL (e.g., example.com): ").strip()

# Check if the target URL is not empty
if not target_url:
    print("Error: Target URL cannot be empty.")
    exit(1)

# Open the wordlist file and check each subdomain
with open("subdomains_20000.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        if not word:  # Skip empty lines
            continue
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print(f"[+] Discovered subdomain ----> {test_url}")
