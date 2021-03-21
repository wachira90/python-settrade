from settrade.openapi import Investor

investor = Investor( app_id="app_id",       
                            app_secret="app_secret",
                            broker_id="broker_id", 
                            app_code="app_code", 
                            is_auto_queue = False)
# Derivatives Account
# deri = investor.Derivatives(account_no="wachira-D")
# account_info = deri.get_account_info()

# Equity Acount
equi = investor.Equity(account_no="wachira-E")
account_info = equi.get_account_info()

print(account_info )
