import re


raw = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for parsed_raw in f:
        print(re.findall(raw, parsed_raw))
