import random
import time
from collections import Counter

class Jogador:
    def __init__(self, name, personalidade):
        self.name = name
        self.pontos = 300
        self.personalidade = personalidade
        self.posicao_atual = 0
        self.jogando = True

    def _atualiza_posicao(self, dado):
        if (self.posicao_atual + dado) > 20:
            restante = ((self.posicao_atual + dado) - 20)
            self.posicao_atual = restante
            self.pontos+=100
        else:
            self.posicao_atual+=dado


    def _rola_dado(self):
        dado = random.randint(1,6)
        self._atualiza_posicao(dado)


    def joga(self,tabuleiro):
        self._rola_dado()
        if tabuleiro[self.posicao_atual-1].verificar_disponibilidade():
            tabuleiro[self.posicao_atual-1].checa_personalidade(self)
        else:
            tabuleiro[self.posicao_atual-1].alugar(self)


    def finaliza_jogador(self):
        self.jogando = False

class Propriedade:
    def __init__(self, posicao):
        self.posicao = posicao
        self.valor_compra = random.randint(20,100)
        self.valor_aluguel = random.randint(10, 60)

    def verificar_disponibilidade(self):
        if not hasattr(self, 'comprado'):
            return True
        return False

    def compra(self, proprietario):
        self.comprado = proprietario
        proprietario.pontos = (proprietario.pontos - self.valor_compra)

    def desocupa_propriedade(self):
        delattr(self, 'comprado')
    def checa_personalidade(self, proprietario):
        if 'impulsivo' in proprietario.personalidade:
            self.compra(proprietario)
        elif 'exigente' in proprietario.personalidade and self.valor_aluguel > 50:
            self.compra(proprietario)
        elif 'cauteloso' in proprietario.personalidade and ((proprietario.pontos - self.valor_compra) >= 80):
            self.compra(proprietario)
        elif 'aleatorio' in proprietario.personalidade and bool(random.getrandbits(1)):
            self.compra(proprietario)
        else:
            if self.verificar_disponibilidade():
                pass
            else:
                self.alugar(proprietario)

    def alugar(self, inquilino):
        if inquilino.pontos >= self.valor_aluguel and self.valor_aluguel > 0:
            inquilino.pontos = (inquilino.pontos - self.valor_aluguel)
            self.comprado.pontos += self.valor_aluguel

        else:
            inquilino.finaliza_jogador()




def game_start():
    lista_jogadores = []
    jogador1 = Jogador('Shepard', 'impulsivo')
    jogador2 = Jogador('Garry', 'exigente')
    jogador3 = Jogador('Dio', 'cauteloso')
    jogador4 = Jogador('ClapTrap', 'aleatorio')

    lista_jogadores.append(jogador1)
    lista_jogadores.append(jogador2)
    lista_jogadores.append(jogador3)
    lista_jogadores.append(jogador4)

    tabuleiro = []
    for casa in range(1,21):
        propriedade = Propriedade(casa)
        tabuleiro.append(propriedade)

    random.shuffle(lista_jogadores)

    vencedor = False

    i = 0


    while not vencedor:
        while i < 1000:
            lista_jogando = []
            for jogador in lista_jogadores:
                if jogador.jogando:
                    lista_jogando.append(jogador)

            if len(lista_jogando) == 1:
                print(f"Vencedor {lista_jogando[0].name} : Personalidade: {lista_jogando[0].personalidade}")
                lista_partidas.append(i)
                vencedor = True

                return lista_jogando[0]
            for jogador in lista_jogando:
                if not jogador.jogando:
                    for _ in tabuleiro:
                        if hasattr(_, 'comprado'):
                            nome_obj = str(jogador.__repr__())
                            nome_owner = str(_.comprado)
                            if _.comprado.__repr__() == jogador.__repr__():
                                _.desocupa_propriedade()
                if jogador.jogando:
                    jogador.joga(tabuleiro)
                i += 1

        vencedor = True
        return "timeout"



if __name__ == '__main__':
    print(f'The game')
    start_game = time.time()

    lista_vencedores = []
    timeout_contador = 0
    lista_partidas = []

    for partida in range(0,300):
        print(f"Partida {partida}")
        resultado = game_start()

        if hasattr(resultado,'personalidade'):
            lista_vencedores.append(resultado.personalidade)
        else:
            timeout_contador+=1


    c = Counter(lista_vencedores)

    print(f"Das 300 partidas, {timeout_contador} encerraram em timeout.")

    print("#" * 130)

    for i, count in c.most_common():
        print(f"Das 300 partidas jogadas, as partidas vencidas pelo jogador {i} totalizam: {count}. Representando {round(count / 300 * 100, 2)}%")

    print("#"*130)

    for i, count in c.most_common():
        print(f"De todas as partidas onde houve um vencedor, as partidas vencidas pelo jogador {i} totalizam: {count}. Representando {round(count / sum(c.values()) * 100, 2)}%")


    print(f"O comportamento com mais vitórias é: {max(set(lista_vencedores), key=lista_vencedores.count)}")

    print(f"A média de partidas não encerradas em timeout é de {round(sum(lista_partidas) / len(lista_partidas),0)} rodadas")