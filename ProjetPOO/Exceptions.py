class InstantiationError(Exception):
    def __init__(self,obj):
        self.obj = obj
    def __str__(self):
        return "La classe "+self.obj.__class__+" est abstraite"
        
