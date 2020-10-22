BASE_PATH = 'http://data.fixer.io/api/latest?access_key='
API_KEY = '1efae8c05a77a3bafc8754fbd12e43f2'

url = BASE_PATH + API_KEY





rules = {
    'archive' : True,
    'email' : {'send' : False },
    'prefer' :
    {'AED' : {'max' :  0, 'min' : 0},
     'AMD' : {'max' : 0, 'min' : 0}}
    }

