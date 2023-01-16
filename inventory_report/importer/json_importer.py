from inventory_report.importer.importer import Importer

import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if ".json" not in path:
            raise ValueError("Arquivo não suportado")
        with open(path, 'r') as file:
            return json.load(file)
