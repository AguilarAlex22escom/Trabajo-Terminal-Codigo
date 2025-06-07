from Swarm import Swarm
from Optimization import Optimization


class SearchSpace:
    # itr = Number of iterations.
    # n = Number of particles.
    def __init__(self, w, c1, c2, itr, n, dim, xmin, xmax, fitness_name):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.itr = itr
        self.n = n
        self.fitness_name = fitness_name
        self.xmin = xmin
        self.xmax = xmax
        self.dim = dim
        self.gbest = []
        self.gbest_fitness = 0.0

    def search_global_minimum(self):
        swarm = Swarm(self.n)
        # particles = swarm.generate_particle_swarm(self.w, self.c1, self.c2, self.dim, self.limits)
        global_minimun = 0.0

        if self.fitness_name == "sphere":
            fitness_func = Optimization.sphere_func
            '''
            min = -100
            max = 100            
            '''
        elif self.fitness_name == "rastrigrin":
            fitness_func = Optimization.rastrigrin_func
            '''
            min = -5.12
            max = 5.12
            '''
        elif self.fitness_name == "rosenbrock":
            fitness_func = Optimization.rosenbrock_func
            '''
            min = -30
            max = 30
            '''
        elif self.fitness_name == "griewank":
            fitness_func = Optimization.griewank_func
            '''
            min = -100
            max = 100
            '''
        swarm.generate_particle_swarm(self.w, self.c1, self.c2, self.xmin, self.xmax, self.dim, fitness_func)

        print("------------------------------------------------------------")
        for i in range(self.itr):
            self.gbest, self.gbest_fitness, best_particle = swarm.update_gbest()
            swarm.update_particles(fitness_func)
            '''
            print("Número de iteración: " + str(i + 1))
            print(f"Partícula con la mejor posición: {best_particle.id}")
            print(f"Posición de la partícula {best_particle.id}: {[round(x, 3) for x in self.gbest]}")
            print(f"Evaluación de la posición {best_particle.id}: {round(self.gbest_fitness, 5)}")
            print("------------------------------------------------------------")
            # time.sleep(1)
            '''

            if self.gbest_fitness <= global_minimun:
                return self.gbest, self.gbest_fitness

        return self.gbest, self.gbest_fitness