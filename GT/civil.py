class civil:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['structure', 'transportation']

    def printMembers(self):
        print('Printing programs of the civil-eng. dept')
        for member in self.members:
            print('\t%s ' % member)