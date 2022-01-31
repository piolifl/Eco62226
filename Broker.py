import config
import pyRofex


class ECO_62226:
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


class BCCH_2474:
    user = ""
    password = ""
    account = ""

    def __init__(self):
        self.user = config.user_BCCH2447
        self.password = config.password_BCCH2447
        self.account = config.account_BCCH2447
        pyRofex._set_environment_parameter("url", "https://api.bcch.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex._set_environment_parameter( "ws", "wss://api.bcch.xoms.com.ar/", pyRofex.Environment.LIVE)
        pyRofex.initialize(self.user,self.password,self.account,environment=pyRofex.Environment.LIVE)

#DzLmCrhw2ZcH2a3