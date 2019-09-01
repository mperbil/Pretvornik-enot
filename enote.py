import bottle
import model
result = ''
kolicina2 = 0
st = 0
vhodna = ''
izhodna = ''


@bottle.get('/')
def index():
    return bottle.template('index.tpl', result=result)


@bottle.get('/pretvori/')
def pretvori():
    kolicina = kolicina2
    global st
    st = float(bottle.request.query['st'])
    global vhodna
    vhodna = bottle.request.query['enota1']
    global izhodna
    izhodna = bottle.request.query['enota2']
    result = model.pretvarjanje(kolicina, st, vhodna, izhodna)
    return bottle.template('rezultat.tpl', result = result, st=st, vhodna=vhodna, izhodna=izhodna)

@bottle.get('/na_dolzino/')
def na_dolzino():
    global kolicina2
    kolicina2 = 1
    return bottle.template('dolzina.tpl', result=result)

@bottle.get('/na_prostornino/')
def na_prostornino():
    global kolicina2
    kolicina2 = 2
    return bottle.template('prostornina.tpl', result=result)

@bottle.get('/na_tezo/')
def na_tezo():
    global kolicina2
    kolicina2 = 3
    return bottle.template('teza.tpl', result=result)

@bottle.get('/na_cas/')
def na_cas():
    global kolicina2
    kolicina2 = 4
    return bottle.template('cas.tpl', result=result)
  
@bottle.get('/nazaj/')
def nazaj():
    return bottle.template('index.tpl')



bottle.run(reloader=True, debug=True)