import json
from collections import OrderedDict

def create_config():
    try:
        file_data = OrderedDict()
        file_data['Token'] = ''
        file_data['command_prefix'] = ';'
        file_data['description'] = ''
        file_data['Auther'] = ''
        with open('config.json', 'w', encoding='utf-8') as CreateConfig:
           json.dump(file_data, CreateConfig, ensure_ascii=False, indent='\t')
    except Exception as ex:
        print("[X]: ERROR\n")
        print(f"{str(ex)}")
        exit()


with open('config.json', 'r', encoding='utf-8') as _config:
    config = json.load(_config)