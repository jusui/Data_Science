# coding:utf-8
# extract_from_json.py

import json

def extract_from_json(title):
    with open("jawiki-country.json") as f:
        json_data = f.readline()
        while json_data:
            article_dict = json.loads(json_data)
            if article_dict["title"] == title:
                return article_dict["text"]

            else:
                json_data = f.readline()

    return ""
