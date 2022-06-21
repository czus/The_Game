# The Game - Banco Imobiliário

Este é um jogo estilo banco imobiliário com algumas regras:

* O tabuleiro é composto de 20 casas.
* 4 jogadores, com personalidades especificas e comportamentos especificos;
* Cada partida é composta de 1000 rodadas, encerrando por timeout caso o número máximo seja atingido.
* São realizadas 300 simulações de partida.
* No final, são contabilizadas as partidas encerradas por timeout, e ordenada a porcentagem de vitórias para cada personalidade.


Principais bibliotecas utilizadas:
* random - utilizada para obter valores aleatórios para o custo das posições.
* collections.Counter - Utilizado para realizar as contabilizações de valores de vitória.

Estrutura do projeto:
```
.
├── README.md
├── game.py
```

* game.py - The game.

## Execução 

1. Realize o clone do repositório.
2. Rode o código game.py.

## Output
```
Das 300 partidas, 209 encerraram em timeout.
##################################################################################################################################
Das 300 partidas jogadas, as partidas vencidas pelo jogador cauteloso totalizam: 62. Representando 20.67%
Das 300 partidas jogadas, as partidas vencidas pelo jogador impulsivo totalizam: 17. Representando 5.67%
Das 300 partidas jogadas, as partidas vencidas pelo jogador aleatorio totalizam: 7. Representando 2.33%
Das 300 partidas jogadas, as partidas vencidas pelo jogador exigente totalizam: 5. Representando 1.67%
##################################################################################################################################
De todas as partidas onde houve um vencedor, as partidas vencidas pelo jogador cauteloso totalizam: 62. Representando 68.13%
De todas as partidas onde houve um vencedor, as partidas vencidas pelo jogador impulsivo totalizam: 17. Representando 18.68%
De todas as partidas onde houve um vencedor, as partidas vencidas pelo jogador aleatorio totalizam: 7. Representando 7.69%
De todas as partidas onde houve um vencedor, as partidas vencidas pelo jogador exigente totalizam: 5. Representando 5.49%
O comportamento com mais vitórias é: cauteloso
A média de partidas não encerradas em timeout é de 281.0 rodadas
```
