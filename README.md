<h1 align="center"> Projeto de Web analytics com Python e MongoDB </h1>

# Descrição do Projeto
Projeto de Web Analitycs com extração de dados não estruturados via api do cliente. 
Nesse projeto extraí dados via api e fiz modelagens dos mesmos de acordo com as solicitações do front-end, ou seja, extraía dados, manipulavá- os e devolvia de acordo com o que cada tela da aplicação web demandava.

A primeira modelagam que fiz foi a de unificar os dados de usuários e suas coordenadas, sendo que esses dados estavam em collections diferentes e foi preciso analisar vários jsons de forma minunciosa para obter esse resultado.

# Objetivo principal :dart:
Extrair dados via api, Modelá-los e permanecê-los no MongoDB

# Status do Projeto: :running:	
Concluído :muscle::trophy:

# Principal Desafio

Fazer as modelagens de dados Históricos. Existe uma colletion chamada point_id que é alimentada a cada um minuto e o Cientista de dados pediu que eu dividisse os dados de acordo com o tempo, por exexmplo: 

dados das últimas 24h deveriam permanecer em uma collection , separados por hora - tive que calcular media dos valores por hora

dados a partir de 25h e 3 meses atrás deveriam permanecer em outra collection - cujas médias dos valores deveriam ser calculadas por dia. 

dados a partir de 3 meses da data de geração em uma outra - cujas médias dos valores deveriam ser calculadas por mês. 

Para facilitar o entendimento anexei a especificação funcional desta tarefa em: 
https://github.com/Denise-Pro/Projeto_Web_analytics-Python-MongoDB/blob/master/Especifica%C3%A7%C3%A3o%20_funcional_Dados%20hist%C3%B3ricos.pdf

A maior dificuldade foi na collection onde tinha que permanecer as médias entre 25h e 3 meses, calcular as médias foi fácil, porém apresentá-las da maneira como foi definida a regra de negócio foi um tremendo desafio.

# Desenvolvedores
[<img src="https://avatars2.githubusercontent.com/u/66394744?s=400&u=e5a0cd3c7d94c95ba5926502a2f80720ff814ff7&v=4" width=115 > <br> <sub> Denise Proença </sub>](https://github.com/Denise-Pro) 
