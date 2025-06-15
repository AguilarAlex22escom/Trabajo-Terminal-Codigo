import math

class Optimization:

    @staticmethod
    def sphere_func(position):
        sphere = float(sum(dimension ** 2 for dimension in position))
        return sphere

    @staticmethod
    def rastrigrin_func(position):
        n = len(position)
        rastrigrin = 10 * n + sum((dimension ** 2 - 10 * math.cos(2 * math.pi * dimension)) for dimension in position)
        # rastrigrin = 10 + sum((dimension ** 2 - 10 * math.cos(2 * math.pi * dimension)) for dimension in position)
        return float(rastrigrin)

    @staticmethod
    def rosenbrock_func(position):
        rosenbrock = 0.0
        for dimension in range(len(position) - 1):
            first_part = (position[dimension + 1] - (position[dimension] ** 2)) ** 2
            second_part = (position[dimension] - 1) ** 2
            i = 100 * first_part + second_part
            rosenbrock += i
        return float(rosenbrock)

    @staticmethod
    def griewank_func(position):
        sum_i = sum(dimension ** 2 for dimension in position) / 4000
        product_i = 1.0

        for dimension in range(len(position)):
            product_i *= math.cos(position[dimension] / math.sqrt(dimension + 1))

        griewank = sum_i - product_i + 1
        return float(griewank)
