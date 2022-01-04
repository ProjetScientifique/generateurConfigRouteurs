#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('routers')
env = Environment(loader=file_loader)

SDISID = int(input("Numéro du SDIS: "))

template = env.get_template('SDIS.txt')

SDIS_router = template.render(SDISID=SDISID)

with open(f'SDIS-R{SDISID+1}.txt', 'w') as f:
    f.write(SDIS_router)

template = env.get_template('BBN.txt')

BBN_router = template.render(SDISID=SDISID)

with open(f'BBN-R{SDISID+4}.txt', 'w') as f:
    f.write(BBN_router)