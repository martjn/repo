class jorss(object):

    def faggers(self):
        print("jorss Class()")
    
class martin(jorss):
    
    def faggers(self):
        print("faggers Class()")

Tom = jorss()
Mar = martin()

Tom.faggers()
Mar.faggers()
