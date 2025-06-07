import random


class Particle:
    def __init__(self, w, c1, c2, x, limits, id):
        self.id = id
        # x = position
        self.pbest = list(x)
        self.pbest_fitness = float('inf')
        self.v = [0.00 for _ in range(len(x))]
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.x = x
        self.limits = limits

    def update_velocity(self, gbest):
        r1 = random.random()
        r2 = random.random()
        for i in range(len(self.v)):
            cognitive = self.c1 * r1 * (self.pbest[i] - self.x[i])
            social = self.c2 * r2 * (gbest[i] - self.x[i])
            # v(t + 1)
            self.v[i] = (self.w * self.v[i]) + cognitive + social

    def update_position(self):
        # x(t + 1)
        for i in range(len(self.x)):
            self.x[i] += self.v[i]

            if self.x[i] < self.limits[0]:
                self.x[i] = self.limits[0]
            elif self.x[i] > self.limits[1]:
                self.x[i] = self.limits[1]


    def evaluate(self, fitness):
        current_fitness = fitness(self.x) # pbest_fitness

        if current_fitness < self.pbest_fitness:
            self.pbest = list(self.x)
            self.pbest_fitness = current_fitness

        return current_fitness
