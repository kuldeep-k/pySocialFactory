class SocialFactory:
    social_type = ''
    so = ''
    def __init__(self, social_type):
        self.social_type = social_type
        self.so = self._import_class('socialFactory.plugins.' + social_type + 'SocialPlugin')

    def _import_class(self, name):
        mod = __import__(name)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        mod = getattr(mod, comp)
        r = mod()
        return r 
