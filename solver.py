from z3 import Solver, If, Not, Bool, And, Int, Distinct, sat


def _if_x(x, ind, i):
    if i == len(x) - 1:
        return If(x[i] == ind, i, -1)
    return If(x[i] == ind, i, _if_x(x, ind, i+1))


def _if_xy(x, y, i):
    if i == len(y) - 1:
        return If(x == y[i], i, -1)
    return If(x == y[i], i, _if_xy(x, y, i+1))


def solve(data):
    men_str = data['men_str']
    women_str = data['women_str']
    men_prefer = data['men']
    women_prefer = data['women']

    s = Solver()
    size = len(men_prefer)
    men_choice = [Int(f'men_choice_{i}') for i in range(size)]
    women_choice = [Int(f'women_choice_{i}') for i in range(size)]

    for i in range(size):
        s.add(And(men_choice[i] >= 0, men_choice[i] <= size-1))
        s.add(And(women_choice[i] >= 0, women_choice[i] <= size-1))

    s.add(Distinct(men_choice))

    for i in range(size):
        s.add(women_choice[i] == _if_x(men_choice, i, 0))

    men_choice_in_own_rating = [Int(f'men_choice_in_own_rating_{i}') for i in range(size)]
    women_choice_in_own_rating = [Int(f'women_choice_in_own_rating_{i}') for i in range(size)]

    for m in range(size):
        s.add(men_choice_in_own_rating[m] == _if_xy(men_choice[m], men_prefer[m], 0))

    for w in range(size):
        s.add(women_choice_in_own_rating[w] == _if_xy(women_choice[w], women_prefer[w], 0))

    man_would_prefer = [[Bool(f'man_would_prefer_{m}_{w}') for w in range(size)] for m in range(size)]
    woman_would_prefer = [[Bool(f'woman_would_prefer_{w}_{m}') for m in range(size)] for w in range(size)]

    for m in range(size):
        for w in range(size):
            s.add(man_would_prefer[m][w] == (men_prefer[m].index(w) < men_choice_in_own_rating[m]))

    for w in range(size):
        for m in range(size):
            s.add(woman_would_prefer[w][m] == (women_prefer[w].index(m) < women_choice_in_own_rating[w]))

    for m in range(size):
        for w in range(size):
            s.add(Not(And(man_would_prefer[m][w], woman_would_prefer[w][m])))

    if s.check() != sat:
        raise Exception('not a valid input')

    mdl = s.model()
    res = {}
    for m in range(size):
        w = mdl[men_choice[m]].as_long()
        res[women_str[w]] = men_str[m]

    return res
