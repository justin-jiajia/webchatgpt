from json import dumps


def jsonerror(error):
    return dumps({'suc': False, 'err': error}), 400

def okreturn(th):
    th['suc']=True
    return dumps(th)
