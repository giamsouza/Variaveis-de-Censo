Sobre o projeto
Neste projeto, eu estou como analista de dados para ajudar minha comunidade local limpando e organizando dados censitários simulados. O objetivo é preparar os dados para futuras análises de Business Intelligence e modelagem preditiva.

Descrição do conjunto de dados
O dataset contém informações sobre entrevistados em uma pequena comunidade nos EUA, com as seguintes variáveis:

Coluna	Descrição
primeiro_nome	Primeiro nome do entrevistado
sobrenome	Sobrenome do entrevistado
ano_de_nascimento	Ano de nascimento do entrevistado
votou	Indica se o entrevistado participou do ciclo de votação atual (Sim/Não)
num_filhos	Número de filhos que o entrevistado tem
ano_de_renda	Renda média anual do entrevistado
imposto_mais_alto	Grau de concordância com a afirmação: "os ricos deveriam pagar impostos mais altos"
estado_civil	Estado civil atual do entrevistado

Principais tarefas realizadas
Visualização das primeiras linhas do dataset para entender a estrutura dos dados (.head()).

Verificação dos tipos de dados de cada coluna (.dtypes).

Correção de dados inconsistentes, como substituição de valores ausentes no ano_de_nascimento.

Conversão do tipo de dado de ano_de_nascimento de string para inteiro.

Cálculo do ano médio de nascimento dos entrevistados.

Ordenação da variável categórica imposto_mais_alto com uma escala de concordância definida.

Cálculo da mediana do sentimento em relação ao imposto mais alto.

Codificação one-hot da variável estado_civil para preparar os dados para modelos de aprendizado de máquina.

Criação de variáveis adicionais, como codificação de rótulos para o estado civil e agrupamento por faixa etária (age_group).

Como rodar o projeto
Clone este repositório.

Certifique-se de ter o Python 3.x instalado.

Instale as dependências necessárias (ex: pandas, numpy):

```bash

pip install -r requirements.txt
Execute os scripts Python para limpeza, análise e transformação dos dados.

