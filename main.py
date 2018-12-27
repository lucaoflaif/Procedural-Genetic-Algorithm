import random
from util import *

def new_chromosome():
    return "".join([random.choice(letters) for _ in range(len(SENTENCE))])

def generate_population():
    for _ in range(POPULATION_LENGTH):
        POPULATION.append(new_chromosome())

def order_population_by_fitness():
    global POPULATION

    raw_population_dict = {chromosome:fitness(SENTENCE, chromosome) for chromosome in POPULATION}
    sorted_population_dict = sorted(raw_population_dict.items(), key=lambda kv: kv[1])
    
    POPULATION = [chromosome for chromosome, fitness_point in sorted_population_dict]

def mutation(chromosome):
    for idx in range(len(chromosome)):
        if random.random() < (MUTATION_ERROR/100):
            chromosome = list(chromosome)
            chromosome[idx] = random.choice(letters)
            chromosome = "".join(chromosome)

    return chromosome
    

def crossover_fittest_chromosomes():
    global POPULATION
    #  the first 1/4 of couples are picked (1/2 of chromosomes)
    new_population = []
    for _ in range(int(POPULATION_LENGTH/4)):
        for born_chromosome in crossover(POPULATION.pop(), POPULATION.pop()): 
            new_population.append(mutation(born_chromosome))
    
    POPULATION = new_population

def replace_dead_chromosomes():
    global POPULATION
    # Population lenght - actual population lenght gives us the number of dead chomosomes
    for _ in range(POPULATION_LENGTH-len(POPULATION)):
        POPULATION.append(new_chromosome())


if __name__ == '__main__':
    POPULATION_LENGTH = int(input("POPULATION LENGTH: "))
    SENTENCE = input("SENTENCE: ")
    MUTATION_ERROR = float(input("MUTATION ERROR PERCENTAGE: "))

    POPULATION = [] # initialize population data structure
    
    gen=0
    generate_population()
    while (True):
        order_population_by_fitness()

        print("Generation %d, fittest: " % gen, POPULATION[-1])
        if POPULATION[-1] == SENTENCE: break

        crossover_fittest_chromosomes()
        replace_dead_chromosomes()
        
        gen +=1