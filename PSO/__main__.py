import sys
from SearchSpace import *


def main():
    fitness_name = sys.argv[1].lower()
    itr = int(sys.argv[2])
    n = int(sys.argv[3])
    dim = int(sys.argv[4])
    w = float(sys.argv[5])
    c1 = float(sys.argv[6])
    c2 = float(sys.argv[7])

    pso = SearchSpace(w, c1, c2, itr, n, dim, fitness_name)

    gbest, gbest_fitness = pso.search_global_minimun()
    print("Mejor posición global: ", [round(x, 6) for x in gbest])
    print("Mejor fitness global: ", round(gbest_fitness, 6))


if __name__ == '__main__':
    main()
