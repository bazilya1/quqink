def remove_palindroms(spells):
    a = 0
    for i in spells:
        if i.lower().split() == i[::-1].lower().split():
            spells.pop(a)
        a += 1