class SecretAgent:
    
    _codeword = None 
    
    def __init__(self, codename):
        self.codename = codename
        self._secrets = []
    
    def __del__(self):
        print(f'Agent {self.codename} has been disavowed!')
    
    def remember(self, secret):
        self._secrets.append(secret)
    
    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword
    
    @staticmethod
    def inquire(question):
        print('I know nothing.')
    
    @classmethod
    def _encrypt(cls, message, *, decrypt=False):
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)
    
    secret = property()
    
    @secret.getter
    def secret(self):
        return self._secrets[-1] if self._secrets else None 
    
    @secret.setter
    def secret(self, value):
        self._secrets.append(self._encrypt(value))
    
    @secret.deleter
    def secret(self):
        self._secrets = [] 
    
    

mouse = SecretAgent('Mouse')
mouse.inform('Parmesano')

print(mouse.secret)
mouse.secret = '12345 Main Street'
mouse.secret = "555-1234"

print(mouse.secret)