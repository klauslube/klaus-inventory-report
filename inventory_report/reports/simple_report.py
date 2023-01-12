from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data: list):
        oldest_manufacturing_date = str(date.max)
        neareast_expiration_date = str(date.max)

        company_with_most_products = Counter(
            [product["nome_da_empresa"] for product in data]
        ).most_common(1)[0][0]

        for product in data:
            if product["data_de_fabricacao"] < oldest_manufacturing_date:
                oldest_manufacturing_date = product["data_de_fabricacao"]

            if product["data_de_validade"] < neareast_expiration_date:
                neareast_expiration_date = product["data_de_validade"]    
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {neareast_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
