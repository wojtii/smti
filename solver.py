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
    size_range = range(size)
    men_choice = [Int(f'men_choice_{i}') for i in size_range]
    women_choice = [Int(f'women_choice_{i}') for i in size_range]

    for i in size_range:
        s.add(And(men_choice[i] >= 0, men_choice[i] <= size-1))
        s.add(And(women_choice[i] >= 0, women_choice[i] <= size-1))

    s.add(Distinct(men_choice))

    for i in size_range:
        s.add(women_choice[i] == _if_x(men_choice, i, 0))

    men_own_choice = [Int(f'men_own_choice_{i}') for i in size_range]
    women_own_choice = [Int(f'women_own_choice_{i}') for i in size_range]

    for m in size_range:
        s.add(men_own_choice[m] == _if_xy(men_choice[m], men_prefer[m], 0))

    for w in size_range:
        s.add(women_own_choice[w] == _if_xy(women_choice[w], women_prefer[w], 0))

    men_want = [[Bool(f'men_want_{m}_{w}') for w in size_range] for m in size_range]
    women_want = [[Bool(f'women_want_{w}_{m}') for m in size_range] for w in size_range]

    for m in size_range:
        for w in men_prefer[m]:
            s.add(men_want[m][w] == (men_prefer[m].index(w) < men_own_choice[m]))

    for w in size_range:
        for m in women_prefer[w]:
            s.add(women_want[w][m] == (women_prefer[w].index(m) < women_own_choice[w]))

    for m in size_range:
        for w in size_range:
            s.add(Not(And(men_want[m][w], women_want[w][m])))

    if s.check() != sat:
        raise Exception('not a valid input')

    with open('z3_input.txt', 'w') as f:
        f.write(s.sexpr())

    mdl = s.model()
    res = {}
    for m in size_range:
        res[women_str[mdl[men_choice[m]].as_long()]] = men_str[m]

    return res
