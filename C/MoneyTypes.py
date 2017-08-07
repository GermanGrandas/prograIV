class Money(object):
    def __init__(self,conf):
        self.type=conf[0]
        self.value=conf[1]
        self.description=conf[3]
    
    def getType(self):
        return self.type
    def getValue(self):
        return self.value
    def getDescription(self):
        return self.description


