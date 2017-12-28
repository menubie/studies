# Distribuições

## Variável Aleatória

A Variável Aleatória é uma função que, dado um Evento (altura das pessoas) que ocorre em certo Espaço Amostral (conjunto de pessoas) irá mapear para cada elemento (pessoa) diferentes Valores Numéricos (1.92m, 1.71m, etc...).

Em outras palavras, sabendo que:
	
* A altura das pessoas pode ser representada por X, 
* O conjunto de pessoas é representado por Ω (ômega maiúsculo) 
* E uma pessoa específica é representada por ω (ômega minúsculo)

Uma Variável Aleatória pode ser entendida por: X(ω) → R.

A Variável Aleatória pode ser:
1. Discreta
	* Os valores numéricos que são assumidos são enumeráveis;
	* Onde X é a quantidade de propriedades por bairro em São Paulo.
1. Contínua
	* Os valores numéricos que são assumidos não são enumeráveis;
	* Onde x é o valor de financiamento das propriedades de São Paulo.
1. Mista	

## Função Densidade

Também conhecida como **Função Densidade de Probabilidade** (FDP) ou **Probability Density Functions** (PDF).

Dado uma Variável Aleatória Contínua:

É possível calcular a probabilidade de ω - que pertence a Ω - estar dentro do intervalo: P(1,30 <= X < 1,40). A função que vai descrever essa **probabilidade** é a Função Densidade de Probabilidade (FDP) - densidade também é conhecida como frequência relativa. A probabilidade da Variável Aleatória cair em uma faixa particular é dada pela integral da densidade dessa variável sobre tal faixa, delimitado pelo intervalo de interesse. Calculamos a integral pois queremos saber a área que esse intervalo abrange. Se pegarmos o intervalo inteiro, a probabilidade deverá ser igual a 1.

Importante entender o motivo de pensarmos em probabilidades de faixas e não de valores exatos ao lidarmos com FDPs. Por ser uma função que descreve a densidade de ****Variáveis Aleatórias Contínuas****, dado um intervalo de 0 a 1, teríamos valores infinitamente pequenos se fossemos atribuir probabilidades para cada um dos valores contidos nestes intervalos: Deveríamos ter uma probabilidade associada a 0.5 bem cpomo para 0.333333339 e 0.333333338... Por isso, é muito mais realista calcular a **Probabilidade da Variável Aleatória Contínua estar entre 0.35 e 0.55**.

A principal diferença entre uma FDP e um Histograma é que o último se encarrega de descrever a amostra através das frequências absolutas. Já a FDP irá pensar em descrever a amostra de maneira probabilística: Dada um intervalo, qual a probabilidade de uma Variável Aleatória estar nesta faixa? 
	
Conseguimos obter a FDP derivando uma Função Distribuição Acumulada.

## Função Distribuição

Também conhecida como **Função Distribuição Acumulada** (FDA)

## Função de Probabilidade

Também conhecida como **Função Massa de Probabilidade** (FMP) ou **Probability Mass Function** (PMF).

Conceito muito similar ao da Função Densidade de Probabilidade, com a diferença de que a FDP trata apenas as **Variáveis Aleatórias Contínuas**. Para sabermos a probabilidade de um intervalo na PDF, é necessário integrar a área do gráfico que contém o intervalo. Para a PMF isso não seria necessário.

## Exercícios

Para exercícios práticos, clique **[aqui](./distribuitions_exercises.ipynb)**.

## Referências

* https://en.wikipedia.org/wiki/Random_variable
* https://en.wikipedia.org/wiki/Exponential_distribution
* https://en.wikipedia.org/wiki/Probability_mass_function
* http://hamelg.blogspot.com.br/2015/11/python-for-data-analysis-part-22.html
