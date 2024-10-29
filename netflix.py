class NetflixAccount:
    def __init__(self, account_name, account_type="basic"):
        self.account_name = account_name
        self.account_type = account_type
        self.__account_limit = self.__set_account_limit()
        self.account_views = 0
        
    def __set_account_limit(self):
        if(self.account_type == "basic"):
            return 100
        elif(self.account_type == "premium"):
            return 500
        elif(self.account_type == "vip"):
            return 9999
    
    def get_account_limit(self):
        return f"{self.account_name} Your account limit is {self.__account_limit}"

    
class BasicAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="basic")
        
class PremiumAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="premium")

class VIPAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="vip")
        
        
        
basic = BasicAccount("george")
print(basic.get_account_limit())
            
    
        