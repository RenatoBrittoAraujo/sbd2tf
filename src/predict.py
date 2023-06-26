from src.explore import *
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# recebe os datasets em pandas
# específico para o dataset estudado
def analise_especifica(dfs: dict[str, pd.DataFrame]):
    print("\n\n============== RESPONDER PERGUNTAS")

    # quantas vendas são feitas?

    vendas_totais = len(dfs["DailySales"])
    print(
        "numero de vendas é",
        vendas_totais,
        "do dia",
        dfs["DailySales"]["date"].min().date(),
        "até",
        dfs["DailySales"]["date"].max().date(),
    )

    # quantos produtos foram vendidos?

    produtos_vendidos = dfs["DailySales"]["quantity"].sum()
    print(
        "numero de produtos vendidos é",
        produtos_vendidos,
    )

    # qual é o lucro bruto total dos produtos vendidos?
    # qual é o gasto total com produtos?
    # qual é o lucro líquido da empresa com produtos?
    # qual o lucro total da empresa com produtos?
    # qual é o produto mais lucrativo?
    # qual é a margem de lucro percentual por produto?
    # qual é o produto menos lucrativo?
    # quais são as marcas mais lucrativas?

    lucros_bruto = 0
    gasto_produtos = 0

    for i, product in dfs["Products"].drop_duplicates(subset="product").iterrows():
        quantidade = len(
            dfs["DailySales"][
                dfs["DailySales"]["product_number"].eq(product["product_number"])
            ]
        )
        dfs["Products"].at[i, "quantidade_vendida"] = quantidade

        lucro_unitario = product["unit_price"] - product["unit_cost"]
        dfs["Products"].at[i, "lucro_unitario"] = lucro_unitario

        margem_percentual = product["unit_price"] / product["unit_cost"] - 1.0
        dfs["Products"].at[i, "margem_percentual"] = margem_percentual

        custo = quantidade * product["unit_cost"]
        dfs["Products"].at[i, "custo"] = custo

        lucro_bruto = quantidade * product["unit_price"]
        dfs["Products"].at[i, "lucro_bruto"] = lucro_bruto

        lucro_liquido = lucro_bruto - custo
        dfs["Products"].at[i, "lucro_liquido"] = lucro_liquido

        gasto_produtos += custo
        lucros_bruto += lucro_bruto

        print("--------")
        print(
            "produto",
            product["product"],
            "vendido",
            round(quantidade, 2),
            "vezes lucrando",
            round(product["unit_price"], 2),
            "e custando",
            round(product["unit_cost"], 2),
            "sendo o lucro liquido de",
            round(lucro_unitario, 2),
            "por unidade, totalizando",
            round(lucro_bruto, 2),
            "com custo de",
            round(custo, 2),
            "que é um lucro liquido de",
            round(lucro_liquido, 2),
            "e margem percentual de",
            round(margem_percentual, 2),
        )

    mais_lucrativo = (
        dfs["Products"].sort_values(by="lucro_liquido", ascending=False).iloc[0]
    )

    print(
        "\n\nproduto que gerou mais lucro é:",
        mais_lucrativo["product"],
        "gerando $",
        round(mais_lucrativo["lucro_liquido"], 2),
    )

    menos_lucrativo = (
        dfs["Products"].sort_values(by="lucro_liquido", ascending=True).iloc[0]
    )

    print(
        "produto que gerou menos lucro é:",
        menos_lucrativo["product"],
        "gerando $",
        round(menos_lucrativo["lucro_liquido"], 2),
    )

    print(
        "média de margens de lucro percentual é",
        round(dfs["Products"]["margem_percentual"].mean() * 100, 5),
    )

    print(
        "média de margens de lucro é",
        round(dfs["Products"]["lucro_unitario"].mean(), 2),
    )

    print(
        "lucros brutos é $",
        round(lucros_bruto, 2),
    )

    print(
        "custos é $",
        round(gasto_produtos, 2),
    )

    print(
        "lucro líquido é $",
        round(lucros_bruto - gasto_produtos, 1),
    )

    return dfs


# rede neural generalizada para qualquer X, Y
def create_neural_network(x, y, shape_x, shape_y, test_size=0.2):
    # predict overall daily sales liquid profit for a given date
    # x: past sales data
    # y: liquid profit

    size = shape_x[0]
    size_train = int(size * (1.0 - test_size))

    x_train, x_test = x[:size_train], x[size_train:]
    y_train, y_test = y[:size_train], y[size_train:]

    print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
    print("ok now try make it")

    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=shape_x[1:]),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(y.max()),
        ]
    )

    predictions = model(x_train).numpy()

    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

    min_iter = 0
    iterc = 0
    min_acc = 0.8
    history = None

    while (
        history is None
        or history.history["accuracy"][-1:][0] < min_acc
        or iterc < min_iter
    ):
        history = model.fit(x_train, y_train, epochs=5)
        print("last acc:", history.history["accuracy"][-1:][0])
        iterc += 1

    model.evaluate(x_test, y_test, verbose=2)

    return model, model.predict


def gerar_tabela_de_lucro(dfs):
    # montando dataset de teste
    dds: pd.DataFrame = dfs["DailySales"]
    dpd: pd.DataFrame = dfs["Products"]

    dds_by_date: pd.DataFrame = dfs["DailySales"].drop_duplicates(subset="date")
    dds_by_date = dds_by_date.sort_values(by="date")

    ndf = pd.DataFrame()
    ndf["date"] = dds_by_date["date"]

    for i, col in ndf.iterrows():
        sales_info = dds[dds["date"].eq(col["date"])]
        lucro_brutos = 0
        custos = 0
        liquidos = 0
        for _, sale_info in sales_info.iterrows():
            pid = sale_info["product_number"]
            product_info = dpd[dpd["product_number"].eq(pid)]
            quantity = sale_info["quantity"]
            price = float(product_info["unit_price"].iloc[0])
            custo = float(product_info["unit_cost"].iloc[0])
            lucro_brutos += price * quantity
            custos += custo * quantity
            liquidos += price * quantity - custo * quantity

        ndf.at[i, "lucro_bruto"] = lucro_brutos
        ndf.at[i, "custo"] = custos
        ndf.at[i, "lucro_liquido"] = liquidos

    return ndf


# retorna rede neural treinada e função de predição para lucros dado sua data
def criar_rede_neural_lucro_por_dia(ndf):
    vdf = ndf
    vdf["date"] = vdf["date"].astype("int64")
    vdf["date"] = vdf["date"].apply(lambda x: x / 100000000000)
    vdf["date"] = vdf["date"].astype("int32")
    vdf["lucro_bruto"] = vdf["lucro_bruto"].astype("int32")
    vdf["custo"] = vdf["custo"].astype("int32")
    vdf["lucro_liquido"] = vdf["lucro_liquido"].astype("int32")

    x = vdf["date"].to_numpy()
    y = vdf["lucro_liquido"].to_numpy()
    x.shape = (x.shape[0], 1)
    y.shape = (y.shape[0], 1)

    return create_neural_network(x, y, x.shape, y.shape)


if __name__ == "__main__":
    conn, engine = init_db()
    dfs = explore(conn, engine)

    # responder perguntas analíticas
    dfs = analise_especifica(dfs)

    # cria uma tabela secundária de gastos e lucros
    ndf = gerar_tabela_de_lucro(dfs)
    print("\n\nnova tabela (primeiros 10 elementos):", ndf[0:10])

    # plot de lucros por tempo
    plot(ndf)

    # rede neural. demora algum tempo para ser criado, usa muita memória!
    # nn, predict = criar_rede_neural_lucro_por_dia(ndf)

    # a rede não é particularmente útil, visto que ela apenas
    # usa uma data como input, mas é fácil de treinar e usar
