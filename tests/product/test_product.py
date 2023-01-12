from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, "leite", "gloria", "06-12-2022", "06-01-2023", "0123", "seco"
    )
    assert product.id == 1
    assert product.nome_do_produto == "leite"
    assert product.nome_da_empresa == "gloria"
    assert product.data_de_fabricacao == "06-12-2022"
    assert product.data_de_validade == "06-01-2023"
    assert product.numero_de_serie == "0123"
    assert product.instrucoes_de_armazenamento == "seco"
