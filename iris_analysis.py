# Importando as bibliotecas necessárias 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o dataset"
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Exibindo as primeiras linhas do conjunto de dados para entender a estrutura
print("Visualizando as primeiras linhas do dataset:")
print(df.head())

# Gráfico 1: Dispersão entre comprimento e largura das pétalas, separadas por espécie
plt.figure(figsize=(8, 6))
sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=df)
plt.title("Dispersão entre comprimento e largura das pétalas")
plt.xlabel("Comprimento da pétala")
plt.ylabel("Largura da pétala")
plt.grid(True)
plt.show()

# Gráfico 2: Boxplot para comparar o comprimento e a largura das sépalas entre as espécies
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x="species", y="sepal_length", data=df)
plt.title("Comprimento da sépala por espécie")

plt.subplot(1, 2, 2)
sns.boxplot(x="species", y="sepal_width", data=df)
plt.title("Largura da sépala por espécie")

plt.tight_layout()
plt.show()

# Gráfico 3: Matriz de correlação entre os atributos numéricos
plt.figure(figsize=(8, 6))
correlacao = df.drop("species", axis=1).corr()
sns.heatmap(correlacao, annot=True, cmap="Blues")
plt.title("Matriz de Correlação entre os atributos")
plt.show()
