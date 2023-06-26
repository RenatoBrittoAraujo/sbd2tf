from src.predict import *
from src.explore import *


def plot_de_vendas_por_data(dfs):
    ndf = gerar_tabela_de_lucro(dfs)

    df = ndf[ndf["date"] > ndf["date"].min() + pd.Timedelta(days=365)]

    # Create a line plot from the DataFrame
    plt.plot(df["date"].to_numpy(), df["lucro_bruto"].to_numpy(), label="lucro bruto")
    plt.plot(df["date"].to_numpy(), df["custo"].to_numpy(), label="gastos")
    plt.plot(
        df["date"].to_numpy(), df["lucro_liquido"].to_numpy(), label="lucro liquido"
    )

    # Set plot title and axis labels
    plt.title("Vendas por tempo")
    plt.legend()
    plt.xlabel("Data")
    plt.ylabel("Vendas")

    # Display the plot
    plt.show()


def plot_de_quantidade_vendida_de_produto(dfs):
    dpd = dfs["Products"]
    q = dpd["quantidade_vendida"].fillna(0).to_numpy()
    q.sort(axis=0)
    q = q[::-1]
    print(q)
    plt.hist(q, label="Quantidade vendida", bins=20)

    # Set plot title and axis labels
    plt.title("Histograma de vendas para cada produto")
    plt.legend()
    plt.xlabel("Quantidade vendida do produto")
    plt.ylabel("Quantidade de produtos na categoria")

    # Display the plot
    plt.show()


if __name__ == "__main__":
    conn, engine = init_db()
    dfs = explore(conn, engine)
    dfs = analise_especifica(dfs)

    plot_de_vendas_por_data(dfs)

    plot_de_quantidade_vendida_de_produto(dfs)
