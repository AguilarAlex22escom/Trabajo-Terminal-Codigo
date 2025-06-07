
import os
import time
import statistics
from SearchSpace import *

class Tester:
    # algorithm_file = r"C:\Users\Alexander\Documents\documentos_importantes\TrocasTuneadas\Programas\ACO\__main__.py"
    results_directory = r"C:\Users\Alexander\Documents\documentos_importantes\TrocasTuneadas\Programas\PSO"

    def __create_results_file(self):
        os.makedirs(self.results_directory, exist_ok=True)
        results_file = os.path.join(self.results_directory, "results_pso.txt")
        return results_file

    def save_results(self):
        start_time = time.time()
        best_solutions = []
        best_fitness = []
        # Parametters
        num_ejecuciones = int(input("¿Cuántas veces deseas ejecutar el script?: "))
        fitness_name = input("Nombre de la función de prueba (sphere, rastrigrin, rosenbrock, griewank): ").lower()
        itr = int(input("Número de iteraciones (itr): "))
        n = int(input("Número de partículas (n): "))
        dim = int(input("Dimensiones (dim): "))
        w = float(input("Valor de w: "))
        c1 = float(input("Valor de c1: "))
        c2 = float(input("Valor de c2: "))
        xmin = int(input("Límite mínimo: "))
        xmax = int(input("Límite máximo: "))
        results_file  = self.__create_results_file()
        with open(results_file, 'w') as file:
            for i in range(num_ejecuciones):
                print(f'Ejecutando la iteración {i + 1}...')

                pso = SearchSpace(w=w, c1=c1, c2=c2, itr=itr, n=n, dim=dim, xmin=xmin, xmax=xmax, fitness_name=fitness_name)
                gbest, gbest_fitness = pso.search_global_minimun()

                best_solutions.append(gbest)
                best_fitness.append(gbest_fitness)

                file.write(f'Mejor solución: {[round(x, 6) for x in gbest]}\n')
                file.write(f'Mejor fitness: {round(gbest_fitness, 6)}\n')
                file.write('---------------------------------\n')
                end_time = time.time()
                print(f'Iteración {i + 1} completada\n')
                print(f"Tiempo de ejecución: {round(end_time - start_time, 4)} segundos\n")
            stats = self.get_statistics(best_solutions=best_solutions, fitness=best_fitness)
            print(f'Resultados guardados')
            print(f"Estadísticas:\n{stats}")


    def get_statistics(self, best_solutions, fitness):
        # Getting statistics for fitness
        average_fitness = statistics.mean(fitness) # Average
        median_fitness = statistics.median(fitness) # Median
        std_dev_fitness = statistics.stdev(fitness) # Standard deviation

        statistics_fitness = {"average": average_fitness, "median": median_fitness, "standard_deviation": std_dev_fitness }
        return statistics_fitness

if __name__ == '__main__':
    testing = Tester()
    testing.save_results()

