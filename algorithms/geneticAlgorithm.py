#Andrew J Miller
#This is a genetic algorithm skeleton
#This is an exercise
#Credits to Zivia

#fuzzywuzzy just does fuzzy string matching. This genertic algorithm thing is an example and our example is matching strings.

from fuzzywuzzy import fuzz
import random
import string

#First we need to represent the algorithm as an egent:
class Agent:

	#Now we initialize a constructor
	def __init__(self, string_length):

		#Indicates that the string variable is part of the self, the agent we're currently operating in.
		#There's a functional basis here and it is confusing.
		#We're assinging string a random choice from string.letters and this happens for the string length.
		#At this point comprehensions still seem a bit odd to me. I can read them, but I find them hard to come up with.
		self.string = ''.join(random.choice(string.letter) for _ in xrange(string_length))

		#Okay so this is a genetic algorithm. The cool thing about it as it is trying to get as fit as possible. 
		#We need a function that assigns the fitness of our algorithm, so we know who's the best
		#-1 means the evaluation has not taken palce yet for the object.
		self.fitness = -1


	#Definition of special methods
	#This allows you to alter the behavior of this class
	def __str__(self):

		#So we just want to output what the string was and that strings corresponding fitness was:
		return 'string ' + str(self.string) + 'fitness ' + str(self.fitness)

#Global data:
#This could go in another file but this is an example so it's fine.
in_str = None
in_str_len = None
population = 20
generations = 1000

#This is the algorithm that contains eveything we're going to use to evolve our agents:
def genetic_algorithm():

	#First we need to define our agents:
	agents = init_agents(population, in_str_len)

	#There are 4 primary functions in a genetic algorithm 
	#1. Determine fitness
	#2. Select the best performing agents
	#3. Reproduce using the best agents using cross over and mutation
	#4. Do this multiple times

	#So for each generation:
	for generation in xrange(generations):

		#Tell us what generation we're on...
		print('generation ' + str(generation))

		#Run the fitness on our agent
		agents = fitness(agents)
		#Run selection on our agents
		agents = selection(agents)
		#Run crossover on our agents
		agents = crossover(agents)
		#Run mutation on our agents
		agents = mutation(agents)

		#There are many ways we can run our algorithm to completion. But we can just look for something that's fit enough
		if any(agent.fitness >= 95 for agent in agents):
			print("We've met our candidate that's good enough.")
			exit(0)

	#So we need to define our functions, here we define the init agents function.
	#This generates a list of agents that have been initialized:
	def init_agents(population, string_length):

		return (Agent(string_length for _ in xrange(population))

	#Now we need to figure out how we do our fitness:
	def fitness(agents):

		for agent in agents:
			agent,fitness = fuzz.ratio(agent.string, in_str)

		return agents

	#We also need a function to select who was the best:
	def selection (agents):
		#So this sorts our agents and then uses a lambda function to make sure it's sorted by agent fitness.
		agents = sorted(agents, key = lambda agent: agent.fitness, reverse = True)
		print(''.join(map(str, agents)))

		#I want half of the best agents to live.
		agents = agents[:int(0.5 * len(agents))]

	#This is a confusing function. But this is crossover.
	#The idea is mixing the qualities of the agents in the current iteration with the next iteration.
	#Previously we selected the most fit parents, so the average of the whole population should be better. 
	def crossover(agents):

		#These are the babies for the next iteration:
		babies = []

		#So for each difference in our number of agents and the population... divided by 2
		for _ in xrange((population - len(agents)) / 2):

			#We randomly select parents...
			parent1 = random.choice(agents)
	        parent2 = random.choice(agents)

	        #We get our children...
	        child1 = Agent(in_str_len)
	        child2 = Agent(in_str_len)
	        #We decide where that split is (randomly, that's the point)
	        split = random.randint(0, in_str_len)

	        #We create the string that the child represents
	        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
	        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

	        #Now we have to append these to the babies list.
	        babies.append(child1)
	        babies.append(child2)

		#extend is weird. It just adds 2 lists.
		agents.extend(babies)
		return agents

	#Now all we need is our mutation function. I think just sport mutations will be fine:
	def mutation(agents):

		for agent in agents:
			for ix, param in enemerate(agent.string):

				if random.uniform(0.0, 1.0) <=0.1:

					agent.string = agent.string[0:idx] + random.choice(string.letters) + agent.string[idx+1:in_str_len]

		return agents


if __name__ == '__main__':

    in_str = 'AndyMiller'
    in_str_len = len(in_str)
    genetic_algorithm()