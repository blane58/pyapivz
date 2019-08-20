#!/usr/bin/python3

import requests
from pprint import pprint

def main():
    r = requests.get("https://www.anapioficeandfire.com/api")
    r.status_code
    pprint(r.json())

main()
