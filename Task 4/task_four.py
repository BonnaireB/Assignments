from driver_factory import * 
#
# The purpose of this small script is to search for the list of the product images 
# on the landing page of Amazon.in and to print their associated product url
#

class Amazon():

   
    def __init__(self):
        self.initiate_paths()
        self.images_hrefs= []
        self.df = DriverFactory()
        self.df.open_url(self.BASE_URL)
        
    def initiate_paths(self):
        self.images_xpath = "//img[contains(@class,'product')]/parent::a"
        self.BASE_URL = "https://www.amazon.in/"
    
    def get_images(self):
        return self.df.get_all_elements_by_xpath(self.images_xpath)

    def get_images_hrefs(self):
        imgs = self.get_images()
        self.images_hrefs+= [n.get_attribute('href') for n in imgs]
        self.df.close()


if __name__ == '__main__': 
    
    mp = Amazon()
    mp.get_images_hrefs()
    print(mp.images_hrefs)
    