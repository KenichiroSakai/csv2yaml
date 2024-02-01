import yaml
import json

with open('dat.json') as file:
    # JSONから辞書
    obj = json.load(file)
    # 辞書からYAML
    ym = yaml.dump(obj, Dumper=yaml.CDumper)
    print(ym)