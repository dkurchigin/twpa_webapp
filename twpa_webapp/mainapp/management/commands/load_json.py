from django.core.management.base import BaseCommand
from dictapp.models import DictWithRules

import json
import os

JSON_PATH = 'mainapp/json'


def load_from_dir(dir_name):
    json_files = os.listdir(dir_name)
    for json_file in json_files:
        with open(os.path.join(dir_name, json_file), "r", encoding='utf-8') as read_file:
            loaded_json = json.load(read_file)
            dicts = loaded_json["phrases"]
            for key, value in dicts.items():
                pure_value = format_list_to_str(value)
                dicts[key] = pure_value
                #print(key, dicts[key])
                one_dict = DictWithRules(name=key, content=dicts[key], was_created_manual=False, created_from=json_file)
                one_dict.save()


def format_list_to_str(input_list):
    out_str = ""
    for rule in input_list:
        out_str = out_str + "\"{}\"".format(rule)
        if not input_list.index(rule) == (len(input_list) - 1):
            out_str = out_str + ",\n"
    return out_str


class Command(BaseCommand):
    def handle(self, *args, **options):

        print("Test")
        load_from_dir(JSON_PATH)
        # with open(self.json_file, "r", encoding='utf-8') as read_file:
        #     loaded_json = json.load(read_file)
