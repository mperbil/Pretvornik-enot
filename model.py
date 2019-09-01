#DOLZINA
def v_osnovno_enoto_d(st, x):
    if x == 'km':
        return st*1000
    elif x == 'm':
        return st
    elif x == 'dm':
        return st/10
    elif x == 'cm':
        return st/100
    elif x == 'mm':
        return st/1000
    else:
        return 'Napaka'

def v_zeleno_enoto_d(st, x):
    if x == 'km':
        return str(st/1000) + ' km'
    elif x == 'm':
        return str(st) + ' m'
    elif x == 'dm':
        return str(st*10) + ' dm'
    elif x == 'cm':
        return str(st*100) + ' cm'
    elif x == 'mm':
        return str(st*1000) + ' mm'
    else:
        return 'Napaka'


def pretvarjanje_dolzine(st, vhodna, izhodna):
    a = v_osnovno_enoto_d(st, vhodna)
    b = v_zeleno_enoto_d(a, izhodna)
    return b

#PROSTORNINA
def v_osnovno_enoto_p(st, x):
    if x == 'hl':
        return st*100
    elif x == 'l':
        return st
    elif x == 'dl':
        return st/10
    elif x == 'cl':
        return st/100
    elif x == 'ml':
        return st/1000
    else:
        return 'Napaka'

def v_zeleno_enoto_p(st, x):
    if x == 'hl':
        return str(st/100) + ' hl'
    elif x == 'l':
        return str(st) + ' l'
    elif x == 'dl':
        return str(st*10) + ' dl'
    elif x == 'cl':
        return str(st*100) + ' cl'
    elif x == 'ml':
        return str(st*1000) + ' ml'
    else:
        return 'Napaka'


def pretvarjanje_prostornine(st, vhodna, izhodna):
    a = v_osnovno_enoto_p(st, vhodna)
    b = v_zeleno_enoto_p(a, izhodna)
    return b

#TEŽA
def v_osnovno_enoto_t(st, x):
    if x == 'kg':
        return st*1000
    elif x == 'g':
        return st
    elif x == 't':
        return st * 1000000
    elif x == 'mg':
        return st/1000
    else:
        return 'Napaka'

def v_zeleno_enoto_t(st, x):
    if x == 'kg':
        return str(st/1000) + ' kg'
    elif x == 'g':
        return str(st) + ' g'
    elif x == 't':
        return str(st/1000000) + ' t'
    elif x == 'mg':
        return str(st*1000) + ' mg'
    else:
        return 'Napaka'


def pretvarjanje_teze(st, vhodna, izhodna):
    a = v_osnovno_enoto_t(st, vhodna)
    b = v_zeleno_enoto_t(a, izhodna)
    return b

#ČAS
def v_osnovno_enoto_c(st, x):
    if x == 'd':
        return st*24
    elif x == 'h':
        return st
    elif x == 'min':
        return st/60
    elif x == 's':
        return st/3600
    else:
        return 'Napaka'

def v_zeleno_enoto_c(st, x):
    if x == 'd':
        return str(st/24) + ' d'
    elif x == 'h':
        return str(st) + ' h'
    elif x == 'min':
        return str(st*60) + ' min'
    elif x == 's':
        return str(st*3600) + ' s'
    else:
        return 'Napaka'
    
def pretvarjanje_casa(st, vhodna, izhodna):
    a = v_osnovno_enoto_c(st, vhodna)
    b = v_zeleno_enoto_c(a, izhodna)
    return b



def pretvarjanje(kolicina, st, vhodna, izhodna):
    if kolicina == 1:
        return pretvarjanje_dolzine(st, vhodna, izhodna)
    elif kolicina == 2:
        return pretvarjanje_prostornine(st, vhodna, izhodna)
    elif kolicina == 3:
        return pretvarjanje_teze(st, vhodna, izhodna)
    elif kolicina == 4:
        return pretvarjanje_casa(st, vhodna, izhodna)
    



