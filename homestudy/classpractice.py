class korean:

    nationality = ''
    
    def __init__(self, nation):
        self.nationality = nation
    
    def printNationality(self):
        print(self.nationality)
        
i = korean('대한민국')
you = korean('대한민국')

i.printNationality()
you.printNationality()