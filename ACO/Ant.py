import random as rd
import math

class Ant:
    def __init__(self, id, dim, limits, xi): # xi maybe 0.8257 too.
        self.id = id
        self.dim = dim
        self.limits = limits  # [min, max]
        self.xi = xi
        self.trail = []
        self.pbest = []
        self.pbest_fitness = float('inf')

    def init_position(self):
        self.trail = [rd.uniform(self.limits[0], self.limits[1]) for _ in range(self.dim)]
        self.pbest = list(self.trail)

    def evaluate(self, fitness_func):
        current_fitness = fitness_func(self.trail)
        if current_fitness < self.pbest_fitness:
            self.pbest = list(self.trail)
            self.pbest_fitness = current_fitness
            
        return current_fitness

    def update_position(self, selected_solution, archive_solutions, k):
        new_position = []
        # adaptive_xi = self.xi * (1 + (max_iterations - iteration) / max_iterations)
        for dim in range(self.dim):
        # Obtener valores de esta dimensión en todas las soluciones élite
            mu = selected_solution[dim]
            dim_values = [sol[dim] for sol in archive_solutions]
            sigma = self.xi * sum(abs(x - mu) for x in dim_values) / max(1, k - 1)
        
            if sigma < 1e-10:
                sigma = (self.limits[1] - self.limits[0]) * 0.01
            
            if sigma < 1e-20:
                sigma = (self.limits[1] - self.limits[0]) * 0.01

            new_dim = rd.gauss(mu, sigma)
        
            new_dim = max(self.limits[0], min(self.limits[1], new_dim))
            new_position.append(new_dim)

        self.trail = new_position

    def get_position(self):
        return list(self.trail)
    
    def get_best_position(self):
        return list(self.pbest)
    
    def get_best_fitness(self):
        return self.pbest_fitness