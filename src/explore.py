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


if __name__ == "__main__":
    # incia db
    conn, engine = init_db()

    # exploração preliminar
    dfs = explore(conn, engine)

    # procura correlações
    # threshold de correlação mínima de 0.1
    correlations(dfs, 0.25)
