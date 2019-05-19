from solver import solve
from checker import check


def test_3x3():
    albert, bradley, charles, diane, fergie, emily = 0, 1, 2, 0, 1, 2
    p = {
        'men': {
            albert: [diane, emily, fergie],
            bradley: [emily, diane, fergie],
            charles: [diane, emily, fergie],
        },
        'women': {
            diane: [bradley, albert, charles],
            fergie: [albert, bradley, charles],
            emily: [albert, bradley, charles],
        },
        'men_str': ['albert', 'bradley', 'charles'],
        'women_str': ['diane', 'fergie', 'emily'],
    }
    guy = {
        'albert':  ['diane', 'emily', 'fergie'],
        'bradley': ['emily', 'diane', 'fergie'],
        'charles': ['diane', 'emily', 'fergie'],
    }
    girls = {
        'diane':  ['bradley', 'albert', 'charles'],
        'fergie': ['albert', 'bradley', 'charles'],
        'emily':  ['albert', 'bradley', 'charles'],
    }
    res = solve(p)
    assert check(guy, girls, solve(p))
    assert res == {'diane': 'albert', 'emily': 'bradley', 'fergie': 'charles'}


def test_3x3_v2():
    arie, bert, carl, ann, betty, cindy = 0, 1, 2, 0, 1, 2
    p = {
        'men': {
            arie: [betty, ann, cindy],
            bert: [ann, cindy, betty],
            carl: [ann, cindy, betty],
        },
        'women': {
            ann: [bert, arie, carl],
            betty: [arie, carl, bert],
            cindy: [bert, arie, carl]
        },
        'men_str': ['arie', 'bert', 'carl'],
        'women_str': ['ann', 'betty', 'cindy'],
    }
    guy = {
        'arie':  ['betty', 'ann', 'cindy'],
        'bert': ['ann', 'cindy', 'betty'],
        'carl': ['ann', 'cindy', 'betty'],
    }
    girls = {
        'ann':  ['bert', 'arie', 'carl'],
        'betty': ['arie', 'carl', 'bert'],
        'cindy':  ['bert', 'arie', 'carl'],
    }

    res = solve(p)
    assert check(guy, girls, res)
    assert res == {'betty': 'arie', 'ann': 'bert', 'cindy': 'carl'}


def test_10x10():
    # from rosetta
    abe, bob, col, dan, ed, fred, gav, hal, ian, jon = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    abi, bea, cath, dee, eve, fay, gay, hope, ivy, jan = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    p = {
        'men': {
            abe: [abi, eve, cath, ivy, jan, dee, fay, bea, hope, gay],
            bob: [cath, hope, abi, dee, eve, fay, bea, jan, ivy, gay],
            col: [hope, eve, abi, dee, bea, fay, ivy, gay, cath, jan],
            dan: [ivy, fay, dee, gay, hope, eve, jan, bea, cath, abi],
            ed: [jan, dee, bea, cath, fay, eve, abi, ivy, hope, gay],
            fred: [bea, abi, dee, gay, eve, ivy, cath, jan, hope, fay],
            gav: [gay, eve, ivy, bea, cath, abi, dee, hope, jan, fay],
            hal: [abi, eve, hope, fay, ivy, cath, jan, bea, gay, dee],
            ian: [hope, cath, dee, gay, bea, abi, fay, ivy, jan, eve],
            jon: [abi, fay, jan, gay, eve, bea, dee, cath, ivy, hope],
        },
        'women': {
            abi: [bob, fred, jon, gav, ian, abe, dan, ed, col, hal],
            bea: [bob, abe, col, fred, gav, dan, ian, ed, jon, hal],
            cath: [fred, bob, ed, gav, hal, col, ian, abe, dan, jon],
            dee: [fred, jon, col, abe, ian, hal, gav, dan, bob, ed],
            eve: [jon, hal, fred, dan, abe, gav, col, ed, ian, bob],
            fay: [bob, abe, ed, ian, jon, dan, fred, gav, col, hal],
            gay: [jon, gav, hal, fred, bob, abe, col, ed, dan, ian],
            hope: [gav, jon, bob, abe, ian, dan, hal, ed, col, fred],
            ivy: [ian, col, hal, gav, fred, bob, abe, ed, jon, dan],
            jan: [ed, hal, gav, abe, bob, jon, col, ian, fred, dan],
        },
        'men_str': ["abe", "bob", "col", "dan", "ed", "fred", "gav", "hal", "ian", "jon"],
        'women_str': ["abi", "bea", "cath", "dee", "eve", "fay", "gay", "hope", "ivy", "jan"],
    }
    guyprefers = {
        'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
        'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
        'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
        'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
        'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
        'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
        'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
        'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
        'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
        'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}

    galprefers = {
        'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
        'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
        'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
        'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
        'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
        'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
        'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
        'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
        'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

    res = solve(p)
    assert check(guyprefers, galprefers, res)
    assert res == {'ivy': 'abe', 'cath': 'bob', 'dee': 'col', 'fay': 'dan', 'jan': 'ed',
                   'bea': 'fred', 'gay': 'gav', 'eve': 'hal', 'hope': 'ian', 'abi': 'jon'}

def test_incomp_5x5():
    abe, bob, col, dan, ed = 0, 1, 2, 3, 4
    abi, bea, cath, dee, eve = 0, 1, 2, 3, 4

    p = {
        'men': {
            abe: [bea, dee, eve],
            bob: [abi, cath],
            col: [dee, bea, cath, eve, abi],
            dan: [eve, cath, abi, dee],
            ed: [dee, eve],
        },

        'women': {
            abi: [bob, col, dan],
            bea: [col, abe],
            cath: [col, dan, bob],
            dee: [ed, abe, dan, col],
            eve: [abe, ed, col, dan],
        },
        'men_str': ["abe", "bob", "col", "dan", "ed"],
        'women_str': ["abi", "bea", "cath", "dee", "eve"],
    }

    guyprefers = {
        'abe': ['bea', 'dee', 'eve'],
        'bob': ['abi', 'cath'],
        'col': [ 'dee', 'bea', 'cath', 'eve', 'abi'],
        'dan': ['eve', 'cath', 'abi', 'dee'],
        'ed': ['dee', 'eve'],
    }
    galprefers = {
        'abi': ['bob', 'col', 'dan'],
        'bea': ['col', 'abe'],
        'cath': ['col', 'dan', 'bob'],
        'dee': ['ed', 'abe', 'dan', 'col'],
        'eve': ['abe', 'ed', 'col', 'dan']
    }

    res = solve(p)
    assert check(guyprefers, galprefers, res)
    assert res == {'cath': 'dan', 'abi': 'bob', 'bea': 'col', 'eve': 'abe', 'dee': 'ed'}