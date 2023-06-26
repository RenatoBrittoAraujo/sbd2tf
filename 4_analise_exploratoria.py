from src.create_db import *
import sqlalchemy as db
import pandas as pd


# explora o dataset e gera um log rico em informações da topologia do sistema
def explore(conn, engine):
    clss: list[object] = [DailySales, OneK, Retailers, Products, Methods]

    dataframe_sets = {x: None for x in [c.__name__ for c in clss]}
    print(dataframe_sets)

    for cls in clss:
        elems: list[sqlalchemy.engine.row.Row] = get_db_all(cls, conn)
        print("====================")

        # tabela com numero de tuplas
        print(f"{cls.__name__}: {len(elems)}")

        table_name = cls.__tablename__
        inspector = db.inspect(engine)
        columns: list[db.engine.interfaces.ReflectedColumn] = inspector.get_columns(
            table_name
        )
        dataframe_sets[cls.__name__] = pd.DataFrame()

        for col in columns:
            print("--------------")

            def getv(x):
                return elems[x]._asdict()[col["name"]]

            # coluna da tabela com tipo

            print(f"{col['name']}: {col['type']}")

            # 3 primeiras tuplas, como exemplo

            print(f"Sample: {[getv(x) for x in range(3)]}")

            vals = [getv(i) for i in range(len(elems))]
            df = pd.DataFrame(vals)
            dataframe_sets[cls.__name__][col["name"]] = df

            if type(getv(0)) is str:
                df = pd.DataFrame(vals)

                # numero de strings

                print(f"There are {len(df[0])} strings")

                # numero de strings unicas

                print(f"There are {len(df[0].unique())} unique strings")

                # histograma das strings

                print(f"Histogram: {df[0].value_counts()}")

            if type(getv(0)) is datetime:
                df = pd.DataFrame([x._asdict() for x in elems])
                df[col["name"]] = pd.to_numeric(df[col["name"]])

                mean = df[col["name"]].mean()
                mean = pd.to_datetime([mean])

                # média das datas, em formato datetime

                print(f"Mean: {mean[0]}")
                continue

            if type(getv(0)) is not int and type(getv(0)) is not float:
                # tabela é ignorada porque seu tipo é desconhecido

                print(f"row named {cls.__name__}.{col['name']} Ignored, unknown type")

                continue

            avg = sum(vals) / len(elems)

            # média dos elementos da tabela

            print(f"Average: {avg}")

    return dataframe_sets


# explora correlações entre cada uma das tuplas e tabelas
# onde a correlação é maior que um threshold.
# nem todas as correlações são relevantes
def correlations(dataframe_sets, threshold=0.7):
    print("\n\n\n======== Finding correlations....")

    for key in dataframe_sets:
        print(f"-------------")
        print(f"Correlations for {key}")

        df = dataframe_sets[key].copy()

        # hash em qualquer coluna de strings
        for column in df:
            if type(df[column][0]) == str:
                df[column] = df[column].apply(hash)

        correlation_matrix = df.corr()
        found = 0

        cols = correlation_matrix.columns
        i = 0
        for col1 in cols:
            i += 1
            for col2 in cols[i:]:
                if col1 != col2 and abs(correlation_matrix.loc[col1, col2]) > threshold:
                    found += 1
                    print(
                        "Columns:",
                        col1,
                        "and",
                        col2,
                        "have a correlation of",
                        correlation_matrix.loc[col1, col2],
                    )

        print(f"Found {found} correlations")


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

    # quais são as lojas que mais lucram?
    # quais são as lojas estão com baixa performance?
    # em qual país mais se lucra relativo aos gastos?
    # em qual país menos se lucra relativo aos gastos?


if __name__ == "__main__":
    # incia db
    conn, engine = init_db()

    # exploração preliminar
    dfs = explore(conn, engine)

    # procura correlações
    # threshold de correlação mínima de 0.1
    correlations(dfs, 0.25)
