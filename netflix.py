class NetflixAccount:
    def __init__(self, account_name, account_type="basic"):
        self.account_name = account_name
        self.account_type = account_type
        self.__account_limit = self.__set_account_limit()
        self.account_views = 0
        self.deactivated = False
        
    def __set_account_limit(self):
        if(self.account_type == "basic"):
            return 100
        elif(self.account_type == "premium"):
            return 500
        elif(self.account_type == "vip"):
            return 9999
    
    def get_account_limit(self):
        print(f"{self.account_name} Your account limit is {self.__account_limit}")
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_status(self):
        if(self.deactivated == True):
            return "Deactivated"
        else:
            return "Active"

    def watch_video(self):
        if(self.deactivated == True):
            print(f"{self.account_name} your account is not active")
        elif(self.account_views < self.__account_limit):
            self.account_views += 1
            print(f"{self.account_name} has watched a video. Remaining views: {self.__account_limit - self.account_views}")
    
    def add_view_limit(self):
        if(self.deactivated == True):
            print(f"{self.account_name} your account is not active")
        else:
            self.__account_limit += 100
            print(f"{self.account_name} your view limit increased. new view limit - {self.__account_limit}")
        
    def upgrade_account(self):
        if(self.deactivated == True):
            print(f"{self.account_name} your account is not active")
        elif(self.account_type == "basic"):
            self.account_type = "premium"
            self.__account_limit = self.__set_account_limit()
            print(f"{self.account_name} your account has been upgraded to {self.account_type}")
        elif(self.account_type == "premium"):
            self.account_type = "vip"
            self.__account_limit = self.__set_account_limit()
            print(f"{self.account_name} your account has been upgraded to {self.account_type}")
        elif(self.account_type == "vip"):
            print(f"{self.account_name} your account is already vip")
            
    def downgrade_account(self):
        if(self.deactivated == True):
            print(f"{self.account_name} your account is not active")
        elif(self.account_type == "premium"):
            self.account_type = "basic"
            self.__account_limit = self.__set_account_limit()
            print(f"{self.account_name} your account has been downgraded to {self.account_type}")
        elif(self.account_type == "vip"):
            self.account_type = "premium"
            self.__account_limit = self.__set_account_limit()
            print(f"{self.account_name} your account has been downgraded to {self.account_type}")
        elif(self.account_type == "basic"):
            print(f"{self.account_name} your account is already basic")
            
    def deactivate_account(self):
        if(self.deactivated == False):
            self.deactivated = True
            print(f"{self.account_name} your account has been deactivated")
        else:
            print(f"{self.account_name} your account is already deactivated")
            
    def activate_account(self):
        if(self.deactivated == True):
            self.deactivated = False
            print(f"{self.account_name} your account has been activated")
        else:
            print(f"{self.account_name} your account is already activated")

    
class BasicAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="basic")
        
class PremiumAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="premium")

class VIPAccount(NetflixAccount):
    def __init__(self, account_name):
        super().__init__(account_name, account_type="vip")
        
class NetflixCard:
    def __init__(self, card_holder, card_type, netflix_account):
       self.card_holder = card_holder
       self.card_type = card_type
       self.netflix_account = netflix_account
       
    def get_card_info(self):
        print(f"Card Holder: {self.card_holder}, Card Type: {self.card_type}, Account Type: {self.netflix_account.get_account_type()}, Account status: {self.netflix_account.get_account_status()}")
        
        
basic = BasicAccount("george")
basic.get_account_limit()
basic.deactivate_account()
basic.watch_video()
basic.add_view_limit()
basic.upgrade_account()
basic.get_account_limit()
basic.watch_video()

vip = VIPAccount("john")
vip.get_account_limit()
vip.watch_video()
vip.add_view_limit()
vip.upgrade_account()
vip.deactivate_account()
vip.downgrade_account()
vip.downgrade_account()
vip.activate_account()
vip.upgrade_account()

basic_card = NetflixCard("george", "digital", basic)
basic.deactivate_account()
basic_card.get_card_info()

vip_card = NetflixCard("john", "digital", vip)
vip_card.get_card_info()
        