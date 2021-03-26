import equations

from generate import permutations, get_results, at_least
print("""   
            #############################
            ## WELCOME TO KNUCKLEBONES ##
            #############################
                 ***MEMORY WARNING***
        THIS PROGRAM CALCULATES PERMUTATIONS OF 
        EXPONENTIAL NUMBERS. DOUBLE DIGIT NUMBERS
        IN THE 'DICE' AND 'FACES' FIELDS GENERATE
        MILLIONS OF RESULTS AND MAY TAKE A LONG TIME
        TO PROCESS AND / OR EXCEED YOUR COMPUTER'S MEMORY.""")
dice = int(input("Number of dice: "))
faces = int(input("Number of faces: "))
target = int(input("Target number:"))

perms = permutations(dice, faces)
results = get_results(perms, faces)
at_least = at_least(results, target, dice * faces)

print(f"When rolling {dice}d{faces}...")
print(f"The range of possible results is {dice} - {dice * faces}.")
print(f"There are {faces ** dice} possible dice combinations. ")
print(f"The most likely result is {equations.avg(dice, faces)}.")
print(f"The likelihood of rolling EXACTLY {target} is {round((results.count(target) / len(results) * 100), 3)}%")
print(f"The likelihood of rolling AT LEAST {target} is {round((len(at_least) / len(results) * 100), 3)}%")
