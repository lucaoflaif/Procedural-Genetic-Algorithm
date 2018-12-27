import random
import string

letters = string.ascii_letters + ' '

def crossover(chromosome1, chromosome2):
    chromosome1 = list(chromosome1)
    chromosome2 = list(chromosome2)

    for idx in range(random.randint(0, len(chromosome1))):
        chromosome1[idx], chromosome2[idx] = chromosome2[idx], chromosome1[idx]

    return ("".join(chromosome1), "".join(chromosome2))

def fitness(string_to_find, chromosome):
    points=0
    for idx in range(len(string_to_find)):
        try:
            if string_to_find[idx] == chromosome[idx]:
                points += 1
        except:
            pass
    return points