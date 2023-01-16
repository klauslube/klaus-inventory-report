from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str):
        if "csv" in path:
            return Inventory.open_csv(path, report_type)
        elif "json" in path:
            return Inventory.open_json(path, report_type)
        elif "xml" in path:
            return Inventory.open_xml(path, report_type)
        else:
            raise ValueError("arquivo não é suportado")

    @classmethod
    def open_csv(path, type):
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport.generate(reader)
            elif type == "completo":
                return CompleteReport.generate(reader)
            else:
                raise ValueError("arquivo não é suportado")

    @classmethod
    def open_json(path, type):
        with open(path, "r") as file:
            reader = json.load(file)
            if type == "simples":
                return SimpleReport.generate(reader)
            elif type == "completo":
                return CompleteReport.generate(reader)
            else:
                raise ValueError("arquivo não é suportado")

    @classmethod
    def open_xml(path, type):
        with open(path, "r") as file:
            reader = xmltodict.parse(file.read())['dataset']['record']
            if type == "simples":
                return SimpleReport.generate(reader)
            elif type == "completo":
                return CompleteReport.generate(reader)
            else:
                raise ValueError("arquivo não é suportado")
