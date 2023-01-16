from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(data: list):
        simple_Report = SimpleReport.generate(data)
        company_products = {}

        for product in data:
            if product["nome_da_empresa"] in company_products:
                company_products[product["nome_da_empresa"]] += 1
            else:
                company_products[product["nome_da_empresa"]] = 1

        companies = ""
        for company, quantity in company_products.items():
            companies += f"- {company}: {quantity}\n"

        return (
            f"{simple_Report}"
            f"Produtos estocados por empresa:\n {companies}"
        )
