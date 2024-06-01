

def wybierz_sowe_zwroc_koszt(confirmation, dist, type_pack, spec):
    
    cost = {"galeon": 0, "sykl": 0, "knut": 0}
    sowa = [confirmation, dist, type_pack, spec]

    if sowa[0] == True:
        cost["knut"] += 7
    
    match sowa[1]:
        case "lokalna":
            if type_pack == "list":
                cost["knut"] += 2
            elif type_pack == "paczka":
                cost["knut"] += 7
        case "krajowa":
            if type_pack == "list":
                cost["knut"] += 12
            elif type_pack == "paczka":
                cost["knut"] += 2
                cost["sykl"] += 1
        case "dalekobiezna":
            if type_pack == "list":
                cost["knut"] += 12
            elif type_pack == "paczka":
                cost["knut"] += 2
                cost["sykl"] += 1

    match sowa[3]:
        case "wyjec":
            cost["knut"] += 4
        case "list gonczy":
            cost["sykl"] += 1
    
    return cost


confirmation = True
dist = "lokalna"
type_pack = "list"
spec = None

print(wybierz_sowe_zwroc_koszt(confirmation, dist, type_pack, spec))
