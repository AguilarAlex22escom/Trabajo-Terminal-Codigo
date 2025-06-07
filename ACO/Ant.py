import random as rd
import math

class Ant:
    def __init__(self, id, p, dim, limits):
        self.id = id
        self.p = p  # porcentaje de evaporación
        self.dim = dim
        self.limits = limits  # [min, max]
        self.trail = []
        self.pbest = []
        self.pbest_fitness = float('inf')

    def init_position(self):
        self.trail = [rd.uniform(self.limits[0], self.limits[1]) for _ in range(self.dim)]
        self.pbest = list(self.trail)

    def evaluate(self, fitness):
        current_fitness = fitness(self.trail)
        if current_fitness < self.pbest_fitness:
            self.pbest = list(self.trail)
            self.pbest_fitness = current_fitness
        return current_fitness

    def update_position(self, elite_solutions, k):
        new_position = []
        for dim in range(self.dim):
        # Obtener valores de esta dimensión en todas las soluciones élite
            dim_values = [sol[dim] for sol in elite_solutions]
            mu = sum(dim_values) / len(dim_values)
            sigma = math.sqrt(sum((x - mu)**2 for x in dim_values) / len(dim_values))
            
            if sigma < 1e-10:
                sigma = 0.01
            
            new_dim = rd.gauss(mu, sigma)
            new_dim = max(self.limits[0], min(self.limits[1], new_dim))
            new_position.append(new_dim)
        self.trail = new_position

    '''
    def __get_average_deviation(self, elite_solutions):
        deviations = []
        for dim in range(self.dim):
            dim_values = [sol[dim] for sol in elite_solutions]
            mean = sum(dim_values) / len(dim_values)
            sigma = sum(abs(x - mean) for x in dim_values) / len(dim_values)
            deviations.append(sigma * self.p)
        return deviations

    def __gaussian_sample(self, average, standard_deviation):
        u1 = rd.random()
        u2 = rd.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        return z0 * standard_deviation + average

    def __g_formula(self, x, mu, sigma):
        if sigma == 0:
            return mu
        exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
        coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
        g = coefficient * math.exp(exponent)
        return rd.gauss(mu, sigma)
    
    '''
