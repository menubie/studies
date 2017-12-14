# Distribuições

## Variável Aleatória

A Variável Aleatória é uma função que, dado um Evento (altura das pessoas), irá mapear para cada item de um Espaço Amostral (conjunto de pessoas) diferentes Valores Numéricos (1.92m, 1.71m, etc...).

Em outras palavras, sabendo que a altura das pessoas é representada por X, o conjunto de pessoas é representado por Ω (ômega maiúsculo) e uma pessoa específica é representada por ω (ômega minúsculo), uma variável aleatória pode ser entendida por: X(ω) → R.

A Variável Aleatória pode ser:
1. Discreta 
1. Contínua 
1. Mista	

## Função Densidade de Probabilidade (FDP) 

Também conhecida como _Probability Density Functions_ (PDF)

É possível calcular a probabilidade de ω - que pertence a Ω - estar dentro do intervalo: P(1,30 <= X < 1,40). A função que vai descrever essa **probabilidade** é a Função Densidade de Probabilidade (FDP) - densidade também é conhecida como frequência relativa. A probabilidade da Variável Aleatória cair em uma faixa particular é dada pela integral da densidade dessa variável sobre tal faixa, delimitado pelo intervalo de interesse. Calculamos a integral pois queremos saber a área que esse intervalo abrange. Se pegarmos o intervalo inteiro, a probabilidade deverá ser igual a 1.

Importante entender o motivo de pensarmos em probabilidades de faixas e não de valores exatos ao lidarmos com FDPs. Por ser uma função que descreve a densidade de Variáveis Aleatórias Contínuas, dado um intervalo de 0 a 1, teríamos valores infinitamente pequenos se fossemos atribuir probabilidades para cada um dos valores contidos nestes intervalos: desde 0.5 até 0.333333339. Por isso, é muito realista fazer algo como: Probabilidade da Variável Aleatória Contínua estar entre 0.35 e 0.55.

A principal diferença entre uma FDP e um Histograma é que o último se encarrega de descrever a amostra através das frequências absolutas. Já a FDP irá pensar em descrever a amostra de maneira probabilística: Dada um intervalo, qual a probabilidade de uma Variável Aleatória estar nesta faixa? 
	
Conseguimos obter a FDP derivando uma Função Distribuição Acumulada.

## Função Distribuição Acumulada

## Função Massa de Probabilidade

Também conhecida como _Probability Mass Function_ (PMF).

Conceito muito similar ao da Função Densidade de Probabilidade, com a diferença de que a FDP trata apenas as variáveis aleatórias contínuas. Para sabermos a probabilidade de um intervalo na PDF, é necessário integrar a área do gráfico que contém o intervalo. Para a PMF isso não seria necessário.

## Referências

* https://en.wikipedia.org/wiki/Random_variable
* https://en.wikipedia.org/wiki/Exponential_distribution
* https://en.wikipedia.org/wiki/Probability_mass_function

