import random
from enum import Enum
from dataclasses import dataclass


class Opcao(Enum):
    PEDRA = 1
    TESOURA = 2
    PAPEL = 3


class Resultado(Enum):
    VITORIA = "vitoria"
    DERROTA = "derrota"
    EMPATE = "empate"


@dataclass
class Placar:
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0

    def atualizar(self, resultado: Resultado):
        if resultado == Resultado.VITORIA:
            self.vitorias += 1
        elif resultado == Resultado.DERROTA:
            self.derrotas += 1
        else:
            self.empates += 1

    def __str__(self):
        return f"\nVitórias: {self.vitorias} | Derrotas: {self.derrotas} | Empates: {self.empates}"

    def mostrar_final(self):
        print("\n=== PLACAR FINAL ===")
        print(self)


def escolher_opcao() -> Opcao:
    while True:
        try:
            escolha = int(input("Escolha (1, 2, 3): "))
            if escolha in [o.value for o in Opcao]:
                return Opcao(escolha)
            print("Digite apenas 1, 2 ou 3\n")
        except ValueError:
            print("Digite apenas números\n")


def jogar_rodada() -> Resultado:
    print("\n=== Jokenpô ===\n\n1 - Pedra\n2 - Tesoura\n3 - Papel\n")

    jogador = escolher_opcao()
    computador = random.choice(list(Opcao))

    print(f"\nVocê: {jogador.name} \nComputador: {computador.name}")

    VITORIAS = [
        (Opcao.PEDRA, Opcao.TESOURA),
        (Opcao.TESOURA, Opcao.PAPEL),
        (Opcao.PAPEL, Opcao.PEDRA),
    ]

    if (jogador, computador) in VITORIAS:
        print("\nVocê GANHOU!!!")
        return Resultado.VITORIA
    if jogador == computador:
        print("\nEMPATE!!!")
        return Resultado.EMPATE
    print("\nVocê PERDEU!!!")
    return Resultado.DERROTA


def quer_continuar() -> bool:
    while True:
        jogar = input("\nJogar novamente? (s/n): ").lower()
        if jogar in ["s", "n"]:
            return jogar == "s"
        print("Digite apenas 's' para sim ou 'n' para não.")


def main():
    placar = Placar()
    while True:
        placar.atualizar(jogar_rodada())
        print(placar)
        if not quer_continuar():
            placar.mostrar_final()
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJogo interrompido!")
