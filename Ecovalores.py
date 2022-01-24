import Configuracion
import pyRofex

class Ecovalores:
    user = ""
    password = ""
    account = ""

    def __init__(self):
        self.user = Configuracion.user
        self.password = Configuracion.password
        self.account = Configuracion.account
        pyRofex._set_environment_parameter("url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex._set_environment_parameter( "ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex.initialize(self.user,self.password,self.account,environment=pyRofex.Environment.LIVE)

        
        

