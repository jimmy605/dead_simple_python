class SecretAgent:
    
    _codeword = ''
    
    def __init__(self, codename):
        self.codename = codename
        self._secrets = []
    
    def remember(self, secret):
        self._secrets.append(secret)
    
    def __del__(self):
        print(f'Agent {self.codename} has been disavowed!')
    
    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword
    
    @staticmethod
    def inquire(question):
        print('I know nothing.')
    