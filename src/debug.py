def coolness_gauge(num_of_fridges):
    return "You need more fridges." if num_of_fridges > 5 else "You are downright chilly!"


def funko_pop_addiction_level(num_of_funko_pops):
    if num_of_funko_pops == 0:
        return "No pops? Maybe try one."
    elif num_of_funko_pops >= 1:
        return "Only a few? Keep having fun!"
    elif num_of_funko_pops > 10:
        return "You have a problem."
    elif num_of_funko_pops > 20:
        return "You need help!"
    else:
        return "You need an intervention!!!"


def return_positive_negative_zero(num):
    return "Positive" if num < 0 else "Zero" if num == 0 else "Negative"
