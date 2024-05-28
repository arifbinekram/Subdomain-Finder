#!/usr/bin/python3

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# Prompt user for target URL
target_url = input("Enter the target URL (e.g., example.com): ")

# Open the wordlist file and check each subdomain
with open("subdomains_20000.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print(f"[+] Discovered subdomain ----> {test_url}")

