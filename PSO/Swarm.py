import random as rn
from Particle import *


class Swarm:
    def __init__(self, n): # n = Number of particles.
        self.n = n
        self.particles = []
        self.gbest = []

    def generate_particle_swarm(self, w, c1, c2, xmin, xmax, dim, fitness_func):
        # dim = x to Particle
        positions = []
        for _ in range(self.n):
            '''
            This is an example only for test the algorithm.
            When we find information about dimensions, these values will be changed.
            '''
            position = [rn.uniform(xmin, xmax) for _ in range(dim)]
            positions.append(position)

        self.particles = [Particle(w, c1, c2, position, [xmin, xmax], i) for position, i in zip(positions, range(self.n))]
        # return self.particles
        for particle in self.particles:
            particle.evaluate(fitness_func)
        # self.update_particles(fitness_func)

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
