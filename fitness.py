class Fitness:
    def __init__(self, route, city_map):
        """
        :param route: a single travelling route
        :param city_map: completed graph implemented with adjacency matrix
        """
        self.route = route
        self.city_map = city_map
        self.distance = 0
        self.fitness = 0.0

    def get_total_distance(self):
        """
        :return: total distance cost of this route
        """
        if self.distance == 0:
            for i in range(len(self.route)):
                from_city = self.route[i]
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                self.distance += self.city_map[from_city][to_city]
        return self.distance

    def get_fitness(self):
        """
        Fitness score is calculated in terms of the inverse of total distance.
        The lower total distance is, the higher fitness score is.
        :return: fitness score of this route
        """
        if self.fitness == 0:
            self.fitness = 1 / float(self.get_total_distance())
        return self.fitness
