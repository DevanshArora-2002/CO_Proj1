class SyntaxException(Exception):
    def __init__(self,msg,line):
        super().__init__(msg+" at line no-"+str(line))
        pass
    pass
class ImmediateException(Exception):
    def __init__(self,msg,line):
        super().__init__(msg+" at line no-"+str(line))
        pass
    pass
class IllegalHltInstruction(Exception):
    def __init__(self,msg,line):
        super().__init__(msg+" at line no-"+str(line))
        pass
    pass
class IllegalVariable(Exception):
    def __init__(self,msg,line):
        super().__init__(msg+" at line no-"+str(line))
        pass
    pass
class IllegalLabel(Exception):
    def __init__(self,msg,line):
        super().__init__(msg+" at line no-"+str(line))
        pass
    pass
