import random as rnd
from Swarm import Swarm
from Optimization import Optimization


class SearchSpace:
    # itr = Number of iterations.
    # n = Number of particles.
    def __init__(self, itr, n, dim, xmin, xmax, fitness_name):
        self.itr = itr
        self.n = n
        self.fitness_name = fitness_name.lower()
        self.xmin = xmin
        self.xmax = xmax
        self.dim = dim
        self.gbest = []
        self.gbest_fitness = 0.0

    def search_global_minimum(self):
        swarm = Swarm(self.n)
        # particles = swarm.generate_particle_swarm(self.w, self.c1, self.c2, self.dim, self.limits)
        global_minimum = 1e-6

        if self.fitness_name == "sphere":
            fitness_func = Optimization.sphere_func

        elif self.fitness_name == "rastrigin":
            fitness_func = Optimization.rastrigrin_func

        elif self.fitness_name == "rosenbrock":
            fitness_func = Optimization.rosenbrock_func

        elif self.fitness_name == "griewank":
            fitness_func = Optimization.griewank_func

        else:
            raise ValueError(f"La función {self.fitness_name} no es valida...\n")

        swarm.initialize_particle_swarm(self.xmin, self.xmax, self.dim, fitness_func)

        print("------------------------------------------------------------")
        for t in range(self.itr):
            
            self.gbest, self.gbest_fitness, _ = swarm.update_gbest()
            swarm.update_particles(fitness_func)
            swarm.update_parameters(itr=self.itr, t=t + 1)

            '''
            print("Número de iteración: " + str(i + 1))
            print(f"Partícula con la mejor posición: {best_particle.id}")
            print(f"Posición de la partícula {best_particle.id}: {[round(x, 3) for x in self.gbest]}")
            print(f"Evaluación de la posición {best_particle.id}: {round(self.gbest_fitness, 5)}")
            print("------------------------------------------------------------")
            # time.sleep(1)
            '''

            if self.gbest_fitness <= global_minimum:
                return self.gbest, self.gbest_fitness

        return self.gbest, self.gbest_fitness