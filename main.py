import random
import string


class RandomStringPopulation:
    def __init__(self, target_word, population_size=10):
        if not target_word or not target_word.islower() or not target_word.isalpha():
            raise ValueError("Target word must contain lowercase letters only.")

        if population_size < 1:
            raise ValueError("Population size must be at least 1.")

        self.target_word = target_word
        self.population_size = population_size
        self.population = []

        # Initialise the random strings when an object is created.
        self.__initialize_population()

    def __initialize_population(self):
        """Create random lowercase strings of the target word's length."""
        word_length = len(self.target_word)

        self.population = [
            "".join(
                random.choices(string.ascii_lowercase, k=word_length)
            )
            for _ in range(self.population_size)
        ]


if __name__ == "__main__":
    target = "hello"
    population = RandomStringPopulation(target, population_size=10)

    # Verify that initialisation worked correctly.
    assert len(population.population) == 10
    assert all(len(word) == len(target) for word in population.population)
    assert all(word.islower() and word.isalpha()
               for word in population.population)

    print("Target word:", population.target_word)
    print("Population size:", len(population.population))
    print("Initial population:")
    for word in population.population:
        print(word)

    print("\nAll initialisation checks passed.")