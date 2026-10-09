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


# Execute the program and verify the fitness scores
calculator = FitnessCalculator("ABCD")

test_strings = ["ABCD", "ABXY", "AXCY", "WXYZ", "AB"]

for candidate in test_strings:
    print(f"Candidate: {candidate}, Fitness score: {calculator._FitnessCalculator__calculate_fitness(candidate)}")