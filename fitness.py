import random


class GeneticAlgorithm:
    def __init__(self, target, initial_population):
        self.target = target
        self.population = initial_population.copy()
        self.population_size = len(initial_population)

    def __calculate_fitness(self, candidate):
        """Count characters matching the target in the correct positions."""
        score = 0

        for i in range(min(len(candidate), len(self.target))):
            if candidate[i] == self.target[i]:
                score += 1

        return score

    def __roulette_wheel_selection(self):
        """Select strings with probabilities proportional to fitness."""
        fitness_scores = [
            self.__calculate_fitness(candidate)
            for candidate in self.population
        ]

        total_fitness = sum(fitness_scores)
        selected_strings = []

        for _ in range(self.population_size):
            if total_fitness == 0:
                selected = random.choice(self.population)
            else:
                pick = random.random() * total_fitness
                cumulative_fitness = 0
                selected = self.population[-1]

                for candidate, fitness in zip(
                    self.population, fitness_scores
                ):
                    cumulative_fitness += fitness

                    if pick < cumulative_fitness:
                        selected = candidate
                        break

            selected_strings.append(selected)

        return selected_strings

    def __crossover(self, parent1, parent2):
        """Perform single-point crossover and return two children."""
        if len(parent1) != len(parent2):
            raise ValueError("Parent strings must have equal lengths.")

        if len(parent1) < 2:
            return parent1, parent2

        # Choose a crossover point between the first and last positions.
        point = random.randint(1, len(parent1) - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    def run(self):
        """Select parents and perform crossover to create a new population."""
        print("Initial population:")

        for candidate in self.population:
            print(
                f"{candidate}: "
                f"fitness = {self.__calculate_fitness(candidate)}"
            )

        # Step 1: Select parents using roulette wheel selection.
        parents = self.__roulette_wheel_selection()

        print("\nSelected parents:")
        print(parents)

        # Step 2: Perform crossover in pairs.
        offspring = []

        for i in range(0, self.population_size, 2):
            parent1 = parents[i]
            parent2 = parents[(i + 1) % self.population_size]

            child1, child2 = self.__crossover(parent1, parent2)

            offspring.append(child1)

            if len(offspring) < self.population_size:
                offspring.append(child2)

        # Replace the population with the offspring.
        self.population = offspring

        print("\nNew population after crossover:")

        for candidate in self.population:
            print(
                f"{candidate}: "
                f"fitness = {self.__calculate_fitness(candidate)}"
            )

        print("\nPopulation size:", len(self.population))

        return self.population


if __name__ == "__main__":
    random.seed(42)

    target = "ABCD"

    initial_population = [
        "ABCD",
        "ABCE",
        "ABXY",
        "AXCY",
        "WXYZ",
        "ABCD",
    ]

    algorithm = GeneticAlgorithm(target, initial_population)

    # Test single-point crossover directly.
    parent1 = "ABXY"
    parent2 = "CDZW"

    child1, child2 = algorithm._GeneticAlgorithm__crossover(
        parent1, parent2
    )

    print("Crossover test:")
    print("Parent 1:", parent1)
    print("Parent 2:", parent2)
    print("Child 1:", child1)
    print("Child 2:", child2)

    # Verify that the children are valid single-point crossovers.
    valid_crossover = any(
        child1 == parent1[:point] + parent2[point:]
        and child2 == parent2[:point] + parent1[point:]
        for point in range(1, len(parent1))
    )

    assert valid_crossover, "Crossover did not work as expected!"
    print("Crossover test passed!")

    # Run selection and crossover.
    offspring = algorithm.run()

    # Verify the resulting population.
    assert len(offspring) == len(initial_population)
    assert all(isinstance(child, str) for child in offspring)
    assert all(len(child) == len(target) for child in offspring)

    print("\nAll tests passed!")
    
