import json

class WordInfo():
    """Gets definitions and summary statistics from dictionary.json"""

    @staticmethod
    def get_definition(arg):
        with open('dictionary.json') as f:
            data = json.load(f)
            return data[arg]
