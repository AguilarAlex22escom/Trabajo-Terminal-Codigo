import random as rd
import math
from Ant import *
from Optimization import Optimization

class SearchSpace:
    def __init__(self, K_max, dimensions, q, n, xmin, xmax, fitness_name, xi=0.6061, K_start=1):
        self.K_max = K_max # Solutions file's size.
        self.K_current = K_start
        self.s = [] # Solutions file.
        self.s_fitness = [] # Fitness' solutions file.
        self.dimensions = dimensions # Number of dimensions.
        self.q = q # Convergence percentage
        self.n = n # Number of ants.
        self.xi = xi
        self.ants = []
        self.xmin = xmin # Minimun limit.
        self.xmax = xmax # Maximun limit.
        self.fitness_name = fitness_name
        self.gbest = None
        self.gbest_fitness = float('inf')

    def __set_fitness_func(self):
        fitness_func = None
        if self.fitness_name == "sphere":
            fitness_func = Optimization.sphere_func
        elif self.fitness_name == "rastrigin":
            fitness_func = Optimization.rastrigrin_func
        elif self.fitness_name == "rosenbrock":
            fitness_func = Optimization.rosenbrock_func
        elif self.fitness_name == "griewank":
            fitness_func = Optimization.griewank_func
        return fitness_func


    def __build_initial_archive(self):
        solutions = []
        for ant in self.ants:
            solutions.append((ant.get_best_position(), ant.get_best_fitness()))

        solutions.sort(key=lambda x: x[1])
        self.s = []
        self.s_fitness = []

        for i in range(min(self.K_current, len(solutions))):
            self.s.append(solutions[i][0])
            self.s_fitness.append(solutions[i][1])
    
    def init_ants(self):
        self.ants = []
        for i in range(self.n):
            ith_ant = Ant(i, self.dimensions, [self.xmin, self.xmax], self.xi)
            ith_ant.init_position()
            ith_fitness = ith_ant.evaluate(self.__set_fitness_func())
            self.ants.append(ith_ant)

        self.__build_initial_archive()
        return self.ants

    def __compute_weights(self):
        if self.K_current == 0:
            return []
        
        weights = []
        for i in range(self.K_current):
            euler = math.exp(-0.5 * (((i + 1) / (self.q * self.K_current)) ** 2))
            w = (1 / (self.q * self.K_current * math.sqrt(2 * math.pi))) * euler
            weights.append(w)
        total = sum(weights)

        if total > 0:
            weights = [w / total for w in weights]
        else:
            weights = [1 / self.K_current] * self.K_current

        return weights

    def __select_elite_solutions(self, weights):
        return rd.choices(self.s, weights=weights, k=1)[0]  # Muestrear 'dim' veces
    
    def update_ants(self):
        if not self.s:
            return self.ants

        weights = self.__compute_weights()

        for ant in self.ants:
            selected_solution = self.__select_elite_solutions(weights)
            ant.update_position(selected_solution, self.s, self.K_current)
            fitness = ant.evaluate(self.__set_fitness_func())
            
            # Actualizar mejor solución global
            if fitness < self.gbest_fitness:
                self.gbest_fitness = fitness
                self.gbest = list(ant.pbest)
                
        self.__update_archive()
        return self.ants

    def __update_archive(self):
        archive_ants = []
        for i, solution in enumerate(self.s):
            archive_ants.append((solution, self.s_fitness[i]))
            
        # Combinar hormigas actuales y soluciones del archivo
        for ant in self.ants:
            archive_ants.append((ant.get_best_position(), ant.get_best_fitness()))
        
        # Ordenar por fitness.
        archive_ants.sort(key=lambda x: x[1])
        if self.K_current < self.K_max:
            self.K_current = min(self.K_max, self.K_current + 1)
        
        self.s = []
        self.s_fitness = []

        for i in range(min(self.K_current, len(archive_ants))):
            self.s.append(archive_ants[i][0])
            self.s_fitness.append(archive_ants[i][1])

        # Actualizar mejor solución global.
        if self.s_fitness and self.s_fitness[0] < self.gbest_fitness:
            self.gbest_fitness = self.s_fitness[0]
            self.gbest = list(self.s[0])


    def search_global_minimum(self, iterations, tolerance=1e-6, verbose=False):
        self.init_ants()
            
        convergence_itr = iterations

        for itr in range(iterations):
            self.update_ants()
                
            # Print progress.
            if verbose and (itr + 1) % 10 == 0:
                print(f"Iteración {itr + 1}: "
                      # f"Mejor fitness = {self.gbest_fitness:.6e}, "
                      f"Mejor fitness = {self.gbest_fitness}, "
                      f"Tamaño archivo = {self.K_current}")

        return self.gbest, self.gbest_fitness, convergence_itr
        