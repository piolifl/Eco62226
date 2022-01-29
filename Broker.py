import config
import pyRofex


class EV_62226:
    user = ""
    password = ""
    account = ""

    def __init__(self):
        self.user = config.user
        self.password = config.password
        self.account = config.account
        pyRofex._set_environment_parameter("url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex._set_environment_parameter( "ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex.initialize(self.user,self.password,self.account,environment=pyRofex.Environment.LIVE)



