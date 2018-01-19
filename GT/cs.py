class cs:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['AI', 'ML', 'Security']

    def printMembers(self):
        print('Printing programs of the CS dept.')
        for member in self.members:
            print('\t%s ' % member)