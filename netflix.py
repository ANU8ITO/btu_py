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

    def watch_video(self):
        if(self.account_views < self.__account_limit):
            self.account_views += 1
            print(f"{self.account_name} has watched a video. Remaining views: {self.__account_limit - self.account_views}")
    
    def add_view_limit(self):
        self.__account_limit += 100
        print(f"{self.account_name} your view limit increased. new view limit - {self.__account_limit}")
    
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
        return f"Card Holder: {self.card_holder}, Card Type: {self.card_type}"
        
        
basic = BasicAccount("george")
print(basic.get_account_limit())
basic.watch_video()
basic.add_view_limit()

basic_card = NetflixCard("george", "digital", basic)
print(basic_card.get_card_info())
    
        
