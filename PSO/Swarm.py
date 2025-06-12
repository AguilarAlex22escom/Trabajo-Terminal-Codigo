import random as rnd
from Particle import *


class Swarm:
    def __init__(self, n): # n = Number of particles.
        self.n = n
        self.particles = []
        self.gbest = []
        self.w = 0.7
        self.c1 = 2.5
        self.c2 = 0.5

    def initialize_particle_swarm(self, xmin, xmax, dim, fitness_func):
        # dim = x to Particle
        positions = []

        for _ in range(self.n):
            '''
            This is an example only for test the algorithm.
            When we find information about dimensions, these values will be changed.
            '''
            position = [rnd.uniform(xmin, xmax) for _ in range(dim)]
            positions.append(position)

        self.particles = [Particle(w=self.w, c1=self.c1, c2=self.c2, x=position, limits=[xmin, xmax], id=i) for position, i in zip(positions, range(self.n))]
        # return self.particles
        for particle in self.particles:
            particle.evaluate(fitness_func)
        # self.update_particles(fitness_func)
        # return self.particles

    def update_parameters(self, itr, t): # itr = max iteration, t = current iteration
        wmax = 0.7
        wmin = 0.4

        c1 = [2.5, 0.5] # [c1i, c1f]
        c2 = [0.5, 2.5] # [c2i, c2f]


        # self.w = 0.5 + round(rnd.uniform(0.0, 1.0) / 2, 4)
        self.w = ((wmax - wmin) * ((itr - t) / itr)) + wmin
        self.c1 = ((c1[1] - c1[0]) * (t / itr)) + c1[0]
        self.c2 = ((c2[1] - c2[0]) * (t / itr)) + c2[0]

        for particle in self.particles:
            particle.w = self.w
            particle.c1 = self.c1
            particle.c2 = self.c2
        # print(f"En {t} -> w: {self.w}; c1: {self.c1}; c2: {self.c2}")

    def update_gbest(self):
        if not self.particles:
            return [], float('inf')

        swarm = self.particles
        best_particle = swarm[0]
        self.gbest = swarm[0].pbest
        gbest_fitness = swarm[0].pbest_fitness

        for particle in swarm:
            if particle.pbest_fitness < gbest_fitness:
                gbest_fitness = particle.pbest_fitness
                self.gbest = particle.pbest
                best_particle = particle

        return self.gbest, gbest_fitness, best_particle

    def update_particles(self, fitness_func):
        for particle in self.particles:
            particle.update_velocity(self.gbest)
            particle.update_position()
            particle.evaluate(fitness_func)
