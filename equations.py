def maximum(dice, faces):
    return dice * faces


def avg(dice, faces):
    mode = float((dice / 2)) + float((dice * faces) / 2)
    if mode % 1 == 0:
        return int(mode)
    else:
        mode -= 0.5
        average = f"{int(mode)} or {int(mode + 1)}"
        print()
        return average


def permutation_count(dice, faces):
    return faces ** dice
