from driver_factory import * 
#
# The purpose of this small script is to search for the list of the Malaysian bank names
# and their associated swift code on the specific page
#

class MalaysiaSwift():

   
    def __init__(self):
        self.initiate_paths()
        self.df = DriverFactory()
        self.df.open_url(self.BASE_URL)
        
    def initiate_paths(self):
        self.bank_name_xpath = "//td[@class='table-name']"
        self.bank_swift_xpath = "//td[@class='table-swift']"
        self.BASE_URL = "https://www.theswiftcodes.com/malaysia/"
    
    def get_bank_infos(self):
        names = [n.text for n in self.df.get_all_elements_by_xpath(self.bank_name_xpath)]
        swifts = [n.text for n in  self.df.get_all_elements_by_xpath(self.bank_swift_xpath)]
        self.bank_infos = zip(names,swifts)
        self.df.close()
    


if __name__ == '__main__': 
    
    ms = MalaysiaSwift()
    ms.get_bank_infos()
    for n in ms.bank_infos : print(n)
    