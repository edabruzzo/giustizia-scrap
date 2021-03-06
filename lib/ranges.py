import json


def load_ids_from_json(filename):
    f = open(filename)
    json_objs = f.read().split("\n")
    f.close()

    sets = {}
    out = {}

    for oj in json_objs:
        try:
            o = json.loads(oj)
        except:
            continue

        if not sets.get(o['case_yr']):
            sets[o['case_yr']] = set()
        sets[o['case_yr']].add(int(o['case_no']))

    for year in sets:
        out[year] = list(sets[year])
        out[year].sort()

    return out
