
import pandas as pd

class FileImporter:

    def load_json_database():
        database = pd.read_json("Resources/data/small_dataset.json")
        return database