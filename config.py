from local_config import MAIL_API_KEY

BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


url = BASE_PATH + MAIL_API_KEY





rules = {
    'archive' : True,
    'email' :  False ,

    #Prefer default is None
    'prefer' : 
    {'on' : True,
    'cur' :
    {'AED' : {'max' :  0, 'min' : 0},
     'AMD' : {'max' : 400, 'min' : 0}
     }}}



sms_config = {

}