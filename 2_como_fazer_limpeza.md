# Como fazer a limpeza de um dataset

Limpar um conjunto de dados envolve a remoção de dados indesejados, tratamento de valores ausentes, correção de erros e preparação dos dados para análise ou modelagem. 

## Etapas 

Aqui temos algumas etapas, bem como uma explicação de como executar-la com a biblioteca Pandas em Python:

### Identificar e lidar com valores ausentes
Verifique se há valores ausentes em seu conjunto de dados usando o método `isnull()` ou `isna()`.
Decida como lidar com os valores ausentes. Você pode remover as linhas ou colunas com valores ausentes usando `dropna()`, preencher os valores ausentes com `fillna()`, ou usar métodos mais avançados, como imputação de dados.

### Tratar dados duplicados
Verifique se há linhas duplicadas no conjunto de dados usando o método `duplicated()`.
Remova as linhas duplicadas usando `drop_duplicates()`.

### Lidar com erros e valores inconsistentes
Identifique e corrija erros e valores inconsistentes em seu conjunto de dados.
Use métodos como `replace()` ou expressões regulares para corrigir erros de digitação ou padronizar os dados.

### Converter tipos de dados
Verifique os tipos de dados das colunas e converta-os, se necessário.
Use métodos como `astype()` para converter os tipos de dados das colunas.

### Remover colunas desnecessárias
Identifique as colunas que não são relevantes para sua análise ou modelo e remova-as usando `drop()`.

### Renomear colunas
Renomeie as colunas, se necessário, para tornar os nomes mais descritivos ou padronizados, usando o método `rename()`.

Essas são apenas algumas etapas gerais para limpar um dataset. A complexidade da limpeza de dados varia de acordo com o conjunto de dados específico e os requisitos da análise ou modelo.