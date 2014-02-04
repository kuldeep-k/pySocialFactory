class SocialAuthInterface:
    def login(self, auth_info):
        raise NotImplementedError('method should be implemented in child class')
    def logout(self):
        raise NotImplementedError('method should be implemented in child class')
