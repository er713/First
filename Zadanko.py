from itertools import product, cycle
from random import randrange


def main():
    r = int(input())  # zmienny parametr bazowy
    N = 2 ** r  # ilość cząsteczek
    R = 2 * r + 1  # maksymalna wartość położenia
    P = r + (1 - r % 2)  # maksymalna wartość pędu
    t = 0  # czas
    deltat = 1/2 / P  # krok czasu
    states = tuple(product(range(-R, R + 1), range(-R, R + 1), range(-P, P + 1), range(-P, P + 1)))
    #print(states.index((-11, -11, 5, 5)))
    step = (2 * P + 1) ** 2
    print(step)
    border = (2 * R + 1) * step
    print(border)
    atoms = []
    atomsleft = N
    for i in cycle(range(0, border, step)):
        atoms.append(randrange(i, i + step))
        atomsleft -= 1
        if atomsleft == 0:
            break
    for i in range(N):
        print(states[atoms[i]])



if __name__ == "__main__":
    main()