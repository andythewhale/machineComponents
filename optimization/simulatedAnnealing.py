#Andrew J Miller

#This is an example of a simulated annealing skeleton where there are helper functions that help us define the external problem.
#This specific example was developed alongside the traveling salesmen problem. I use analogies to chemistry / physics because it helps me think about the content.

    #What is our initial and current state?
    current_state = problem
    
    #This is the lowest energy we want in our system before we cease the reaction.
    lowest_possible_energy = 0.00001
    
    #This is us, looping based on our scheduled temperature reduction regimen.
    for t in range(sys.maxsize):
        T = schedule(t)
        
        #If our temperature is less than or equal to the lowest possible energy state:
        if T <= lowest_possible_energy:
            return current_state
        
        #If we're not at the minimum energy state we still have moves to make.
        #The next move's change difference depends on the total energy in the system.
        #Lower energies mean lower changes.
        #Our successors will store this information.
        next_move = random.choice(current.successors())
        #If we don't have a next move it means we're done.
        if not next_move:
            return current_state
        
        #This is the energy difference in the current state and the next state.
        #Remember, molecules want the lowest energy state possible. This is what we're modeling.
        energy_state_change = next_move.get_value() - current.get_value()
        
        #If the next energy state is not lower than the current energy state...
        #OR the probability of a change is high due to temperture...
        if energy_state_change > 0 or probability(math.exp(energy_state_change / T)):
            
            #Then the next state is now our current state.
            #REMEMBER: This happens at high temperatures.
            #Or when the change in energy for the next energy state is minimal.
            current = next_move