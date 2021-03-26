# Creates a list that represents a "Maximum" throw.
def permutations(dice, faces):
    perms = []
    for each in range(dice):
        perms.append(faces)
    return perms


###################################################


# Checks if all items in a list are equal to 1.
# If they are it means that iteration is finished. (unless there are zeroes.)
def end_check(perms):
    if sum(perms) == len(perms):
        return True
    else:
        return False


####################################################


# Finds the index of the first digit greater than 1.
def find_pos(perms):
    pos = 0
    for each in perms:
        if each == 1:
            pos += 1
        else:
            return pos


####################################################


# Resets all ones left of the current position to face value.
def reset(perms, faces, pos):
    for idx, item in enumerate(perms):
        if idx == pos:
            break
        if item == 1:
            perms[idx] = faces
    return perms


##############################################################


# Compiles a list of all possible outcomes of an "xdy" dice throw.
def get_results(perms, faces):
    results = []
    loop = True
    while loop:
        loop = not end_check(perms)
        if not loop:
            results.append(sum(perms))
            break
        results.append(sum(perms))
        index = find_pos(perms)
        perms[index] -= 1
        perms = reset(perms, faces, index)
    return results


#############################################################


# removes all results greater than the target value.
def at_least(results, target, maximum):
    output = []
    if target > maximum:
        return output
    elif target == maximum:
        output.append(maximum)
        return output
    for number in results:
        if number <= target:
            output.append(number)
    return output
#############################################################
