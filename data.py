men = []
women = []
p = {
    'men': {},
    'women': {},
    'men_str': men,
    'women_str': women
}


def update_global_pref(pref, sex):
    sex = sex.replace('a', 'e').lower()
    for key in pref:
        p[sex][key] = pref[key]
    print(p)
