class FitnessCalculator:
    def __init__(self, target):
        self.__target = target

    def __calculate_fitness(self, candidate):
        """Return the number of characters matching the target in the correct positions."""
        score = 0

        for i in range(min(len(candidate), len(self.__target))):
            if candidate[i] == self.__target[i]:
                score += 1

        return score


calculator = FitnessCalculator("ABCD")

test_strings = ["ABCD", "ABXY", "AXCY", "WXYZ", "AB"]

for candidate in test_strings:
    print(f"Candidate: {candidate}, Fitness score: {calculator._FitnessCalculator__calculate_fitness(candidate)}")
import random


class GeneticAlgorithm:
    def __init__(self, target, initial_population):
        self.target = target
        self.population = initial_population.copy()
        self.population_size = len(initial_population)

    def __calculate_fitness(self, candidate):
        """Count matching characters in the correct positions."""
        score = 0

        for i in range(min(len(candidate), len(self.target))):
            if candidate[i] == self.target[i]:
                score += 1

        return score

    def __roulette_wheel_selection(self):
        """Select strings proportionally to their fitness scores."""
        fitness_scores = [
            self.__calculate_fitness(candidate)
            for candidate in self.population
        ]

        total_fitness = sum(fitness_scores)
        selected_strings = []

        for _ in range(self.population_size):
            if total_fitness == 0:
                # If all fitness scores are zero, select randomly.
                selected = random.choice(self.population)
            else:
                # Generate a random value within the total fitness.
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

    def run(self):
        """Display fitness scores and perform roulette wheel selection."""
        print("Initial population:")

        for candidate in self.population:
            print(
                f"{candidate}: "
                f"fitness = {self.__calculate_fitness(candidate)}"
            )

        self.population = self.__roulette_wheel_selection()

        print("\nSelected population:")

        for candidate in self.population:
            print(
                f"{candidate}: "
                f"fitness = {self.__calculate_fitness(candidate)}"
            )

        print("\nPopulation size:", len(self.population))
        return self.population


if __name__ == "__main__":
    random.seed(42)  # Reproducible results for testing

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
    selected = algorithm.run()

    # Verify that selection preserves the population size.
    assert len(selected) == len(initial_population)
    assert all(isinstance(item, str) for item in selected)

    print("\nAll tests passed!")
    
