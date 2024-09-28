def wave(people):
    s = ""
    l = []
    length = len(people)
    people = list(people)
    n = 0
    while n < length:
        if people[n] != " ":
            people[n] = people[n].upper()
            s = "".join(people)
            l.append(s)
            people[n] = people[n].lower()
        n += 1
    return l
