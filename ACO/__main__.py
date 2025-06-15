import sys
from SearchSpace import SearchSpace

def main():
    fitness_name = sys.argv[1].lower()
    iterations = int(sys.argv[2])  # Número de iteraciones
    k_max = int(sys.argv[3])       # Tamaño máximo del archivo de soluciones
    n = int(sys.argv[4])           # Número de hormigas
    dim = int(sys.argv[5])         # Dimensiones
    q = float(sys.argv[6])         # Porcentaje de convergencia (antes era 'p')
    xmin = float(sys.argv[7])      # Límite mínimo
    xmax = float(sys.argv[8])      # Límite máximo

    # Crear el espacio de búsqueda con los parámetros correctos
    search_space = SearchSpace(
        K_max=k_max, 
        dimensions=dim, 
        q=q, 
        n=n, 
        xmin=xmin, 
        xmax=xmax, 
        fitness_name=fitness_name,
        xi=0.6061  # Parámetro de desviación estándar
    )
    
    # Usar el método integrado de búsqueda que maneja todo el proceso
    best_solution, best_fitness, convergence_iteration = search_space.search_global_minimum(
        iterations=iterations, 
        verbose=True
    )
    
    print(f"\nBúsqueda completada en {convergence_iteration} iteraciones")
    print(f"Mejor fitness encontrado: {best_fitness:.6e}")
    print(f"Mejor solución: {best_solution}")
    print(f"Tamaño final del archivo: {search_space.K_current}")

if __name__ == '__main__':
    if len(sys.argv) < 9:
        print("Parámetros requeridos: <fitness_name> <iterations> <k_max> <n> <dim> <q> <xmin> <xmax>")
        print("  fitness_name: sphere, rastrigin, rosenbrock, griewank")
        print("  iterations: número de iteraciones")
        print("  k_max: tamaño máximo del archivo de soluciones")
        print("  n: número de hormigas")
        print("  dim: número de dimensiones")
        print("  q: porcentaje de convergencia (0.0 - 1.0)")
        print("  xmin: límite mínimo del espacio de búsqueda")
        print("  xmax: límite máximo del espacio de búsqueda")
        sys.exit(1)
    
    main()