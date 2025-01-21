import json
from datetime import datetime

def load_data():
  try:
    with open('data.json', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return {'expenses': [], 'budgets': {}}
  
def save_data(data):
  with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

