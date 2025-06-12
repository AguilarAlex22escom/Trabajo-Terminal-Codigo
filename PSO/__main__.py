import sys
from SearchSpace import *


def main():
    fitness_name = sys.argv[1]
    itr = int(sys.argv[2])
    n = int(sys.argv[3])
    dim = int(sys.argv[4])
    xmin = float(sys.argv[5])
    xmax = float(sys.argv[6])
    
    pso = SearchSpace(itr=itr, n=n, dim=dim, xmin=xmin, xmax=xmax, fitness_name=fitness_name)

    gbest, gbest_fitness = pso.search_global_minimum()
    print("Mejor posición global: ", [round(x, 6) for x in gbest])
    print("Mejor fitness global: ", round(gbest_fitness, 6))


if __name__ == '__main__':
    if len(sys.argv) < 6:
        raise ValueError("Parametros requeridos: <fitness name>, <iterations>,"
        "<number of particles>, <dimensions>, <minimum>, <maximum>")

    main()
