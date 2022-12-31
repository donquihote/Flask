# tương tác cơ sở dữ liệu
import json, os
from saleapp import app

def read_json(path):
  with open(path, "r") as f:
      return json.load(f)

def load_categories():
    return read_json()