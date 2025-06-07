import sys
from SearchSpace import *

def main():
    fitness_name = sys.argv[1].lower()
    itr = int(sys.argv[2])  # Número de iteraciones
    k = int(sys.argv[3])
    n = int(sys.argv[4])    # Número de hormigas. Más grande que el tamaño de archivo.
    dim = int(sys.argv[5])  # Dimensiones
    p = float(sys.argv[6])  # Porcentaje de evaporación
    xmin = float(sys.argv[7])
    xmax = float(sys.argv[8])

    search_space = SearchSpace(k=k, dimensions=dim, p=p, n=n, xmin=xmin, xmax=xmax, fitness_name=fitness_name)
    search_space.init_ants()

    for i in range(itr):
        weights = search_space._compute_weights()
        search_space.update_ants(weights)
        best_fitness = min([ant.pbest_fitness for ant in search_space.ants])
        print(f"Iteración {i + 1}: Mejor fitness = {best_fitness:.6f}")

    best_ant = min(search_space.ants, key=lambda a: a.pbest_fitness)
    print("\nMejor solución encontrada:")
    print(f"Fitness: {best_ant.pbest_fitness}")
    print(f"Solución: {best_ant.pbest}")

if __name__ == '__main__':
    if len(sys.argv) < 9:
        print("It's required the parametters: <fitness name> <iteraciones> <k> <n> <dim> <p> <xmin> <xmax>")

    main()