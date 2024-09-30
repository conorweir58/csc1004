class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
    
    def __str__(self):
        output = []
        output.append('Name: {}'.format(self.name))
        output.append('ID: {}'.format(self.tid))
        return '\n'.join(output)