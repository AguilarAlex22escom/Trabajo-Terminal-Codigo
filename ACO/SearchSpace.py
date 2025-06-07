import random as rd
from Ant import *
from Optimization import Optimization

class SearchSpace:
    def __init__(self, k, dimensions, q, p, n, xmin, xmax, fitness_name):
        self.k = k # Solutions file's size.
        self.s = [] # Solutions file.
        self.dimensions = dimensions # Number of dimensions.
        self.q = q # Convergence percentage
        self.p = p # Evaporation percentage.
        self.n = n # Number of ants.
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

    def init_ants(self):
        self.ants = []
        for i in range(self.n):
            ith_ant = Ant(i, self.p, self.dimensions, [self.xmin, self.xmax])
            ith_ant.init_position()
            ith_ant.evaluate(self.__set_fitness_func())
            self.ants.append(ith_ant)

        self.update_archive()
        return self.ants

    def update_ants(self, weights):
        if weights is None:
            weights = self._compute_weights()
            
        elite_solutions = self.s  # Archive de soluciones élite
        
        for ant in self.ants:
            ant.update_position(elite_solutions, self.k)
            fitness = ant.evaluate(self.__set_fitness_func())
            
            # Actualizar mejor solución global
            if fitness < self.gbest_fitness:
                self.gbest_fitness = fitness
                self.gbest = list(ant.pbest)
                
        self.update_archive()
        return self.ants

    def update_archive(self):
        archive_ants = []
        for i, solution in enumerate(self.s):
            temp_ant = Ant(-i-1, self.p, self.dimensions, [self.xmin, self.xmax])
            temp_ant.pbest = solution
            temp_ant.pbest_fitness = self.__set_fitness_func()(solution)
            archive_ants.append(temp_ant)
            
        # Combinar hormigas actuales y soluciones del archivo
        all_candidates = self.ants + archive_ants
        
        # Ordenar por fitness y mantener las k mejores
        all_candidates.sort(key=lambda a: a.pbest_fitness)
        self.s = [ant.pbest for ant in all_candidates[:self.k]]
        
        # Actualizar mejor solución global si es necesario
        if all_candidates[0].pbest_fitness < self.gbest_fitness:
            self.gbest_fitness = all_candidates[0].pbest_fitness
            self.gbest = list(all_candidates[0].pbest)

    def _compute_weights(self):
        weights = [1 / (self.q * self.k * math.sqrt(2 * math.pi)) * math.exp(self.q * (i**2) / (self.k**2))
                    for i in range(self.k)]
        total = sum(weights)
        return [w / total for w in weights]

    def select_elite_positions(self, weights):
        return rd.choices(self.s, weights=weights, k=self.dimensions)  # Muestrear 'dim' veces

    def search_global_minimum(self, max_iterations):
        self.init_ants()
            
        for _ in range(max_iterations):
            weights = self._compute_weights()
            self.update_ants(weights)
                
            # Print progress.
            '''
            if (iteration + 1) % 10 == 0:
                print(f"Iteración {iteration + 1}: Mejor fitness = {self.gbest_fitness}")            
            '''

            if self.gbest_fitness <= 1e-4:
                return self.gbest, self.gbest_fitness

        return self.gbest, self.gbest_fitness

