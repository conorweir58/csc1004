def sort_on(t):
    return t.name

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
    
    def __str__(self):
        output = []
        output.append('Name: {}'.format(self.name))
        output.append('ID: {}'.format(self.tid))
        return '\n'.join(output)
    
    def __eq__(self, other):
        return self.total_time() == other.total_time()
  
    def __gt__(self, other):
        return other.total_time() < self.total_time()

class Triathlon(object):

    def __init__(self):
        self.d = {}
    
    def add(self, t):
        self.d[t.tid] = t
    
    def remove(self, tid):
        del(self.d[tid])
    
    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None
    
    def __str__(self):
        output = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(output)