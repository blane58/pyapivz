#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "zaphod beeblebrox", "species": ["betelgeusian", "martian", "venecian"]}, {"name": "authoer dent", "species": "human"},{"name": "ford prefict", "species": None}]

#    with open("zfile.yml", "w") as zfile:
#        yaml.dump(hitchhikers, zfile)
    mystr = yaml.dump(hitchhikers)

    print(mystr)

main()

