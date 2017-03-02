import json


with open('backup_config.json') as f:
    conf = json.load(f)

conf['newkey'] = 5.0005

with open('backup_config.json', 'w') as f:
    json.dump(conf, f)
