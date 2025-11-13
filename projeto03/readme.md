## 🧩 **Desafio Técnico — Análise de Vendas Multilojas**

### 🎯 **Objetivo**

Avaliar sua capacidade de manipular dados com **Python**, **Pandas**, **NumPy** e **datetime**, realizando **tratamentos, junções e análises consolidadas** a partir de múltiplos DataFrames.

### 📁 **Contexto**

Uma rede de lojas possui três bases de dados:

1. **`vendas.csv`** — contém o histórico de vendas de todas as lojas.
2. **`lojas.csv`** — traz informações sobre cada loja.
3. **`produtos.csv`** — traz a lista de produtos vendidos.

Você deverá integrar essas bases e gerar insights consolidados sobre o desempenho das lojas e produtos.

### 📄 **Arquivos**

#### `vendas.csv`

| id_venda | id_loja | id_produto | quantidade | valor_unitario | data_venda       |
| -------- | ------- | ---------- | ---------- | -------------- | ---------------- |
| 1        | 101     | P01        | 3          | 20.0           | 2024-10-10 14:25 |
| 2        | 102     | P02        | 1          | 100.0          | 2024-10-10 15:12 |
| 3        | 101     | P03        | 2          | 45.0           | 2024-10-11 09:45 |
| ...      | ...     | ...        | ...        | ...            | ...              |

#### `lojas.csv`

| id_loja | nome_loja   | cidade         | data_abertura |
| ------- | ----------- | -------------- | ------------- |
| 101     | Loja Centro | São Paulo      | 2019-05-10    |
| 102     | Loja Norte  | Rio de Janeiro | 2020-03-22    |
| 103     | Loja Sul    | Belo Horizonte | 2021-07-18    |

#### `produtos.csv`

| id_produto | nome_produto | categoria   | preco_custo |
| ---------- | ------------ | ----------- | ----------- |
| P01        | Camiseta     | Vestuário   | 12.0        |
| P02        | Notebook     | Eletrônicos | 70.0        |
| P03        | Caneca       | Utensílios  | 20.0        |

---

### 🧠 **Tarefas**

1. **Leitura e pré-processamento**

   * Ler os arquivos `.csv` usando **Pandas**.
   * Converter as colunas de **datas** (`data_venda`, `data_abertura`) para o tipo `datetime`.
   * Criar uma nova coluna em `vendas` chamada `valor_total` = `quantidade * valor_unitario`.

2. **Integração de dados**

   * Fazer o **merge** entre `vendas`, `lojas` e `produtos`, resultando em um único DataFrame consolidado.
   * Garantir que o DataFrame resultante contenha:
     `nome_loja`, `cidade`, `nome_produto`, `categoria`, `quantidade`, `valor_total`, `data_venda`.

3. **Análise temporal**

   * Calcular o **faturamento mensal por loja**.
   * Calcular o **faturamento total por categoria de produto**.
   * Usar **datetime** para extrair o mês e ano de `data_venda`.

4. **Manipulação com NumPy**

   * Criar uma nova coluna `margem_lucro` = `valor_unitario - preco_custo`, usando **NumPy**.
   * Criar uma coluna `desempenho` classificando cada venda:

     * `"alto"` se `margem_lucro > 30% do valor_unitario`
     * `"baixo"` caso contrário.

5. **Filtros e insights**

   * Mostrar as **5 lojas com maior faturamento total**.
   * Mostrar os **3 produtos mais vendidos por quantidade**.
   * Calcular o **tempo de operação (em dias)** de cada loja com base em `data_abertura`.