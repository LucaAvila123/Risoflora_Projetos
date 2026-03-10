# Descrição do Problema
O conjunto de dados ITENS_PROVA_2018 tem os dados da prova do ENEM de 2018
O DICIONARIO descreve cada uma das colunas que fala das questões
São elas
# CO_POSICAO: Posição do Item na Prova
# SG_AREA: Área de Conhecimento do Item
# CO_ITEM: Código do Item
# TX_GABARITO: Gabarito do Item
# CO_HABILIDADE: Habilidade do Item
# IN_ITEM_ABAN: Indicador de item abandonado
# TX_MOTIVO_ABAN: Motivo para o abandono do item
# NU_PARAM_A: Parâmetro de discriminação: é o poder de discriminação do item para diferenciar os participantes que dominam dos participantes que não dominam a habilidade avaliada.
# NU_PARAM_B: Parâmetro de dificuldade: associado à dificuldade do item, sendo que quanto maior seu valor, mais difícil é o item.
# NU_PARAM_C: Parâmetro de acerto ao acaso: é a probabilidade de um participante acertar o item não dominando a habilidade exigida.
# TX_COR: Cor da Prova
# CO_PROVA: Identificador da Prova
# TP_LINGUA: Língua Estrangeira 
# IN_ITEM_ADAPTADO: Item pertencente à prova adaptada

A partir desses dados de colunas podemos aplicar alguns princípios de Ciência de Dados para construir um classificador
O Propósito desse classificador é mapear, a partir dos três parâmetros dados, em qual grau de dificuldade real uma questão faria parte
A partir disso, o classificador receberia uma questão e poderia servir para afirmar se uma questão é fácil, média ou difícil
Com isso, criaríamos um simulado do ENEM que consiga medir as pontuações dos participantes com questões autorais

As duas bases de dados serão utilizadas pelo classificador
O Desafio principal dessa plataforma de simulados será justamente:
- Montar a base de dados
- Treinar o classificador de maneira coerente com a base de dados
- Construir novos simulados e que a categorização das questões sirva de maneira satisfatória para um propósito pedagógico para a prova do ENEM (e outros vestibulares)