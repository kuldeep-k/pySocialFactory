from socialFactory.core.SocialInterface import SocialInterface
from socialFactory.core.SocialAuthInterface import SocialAuthInterface
from socialFactory.core.SocialFriendInterface import SocialFriendInterface
from socialFactory.core.AuthenticationError import AuthenticationError

class TwitterSocialPlugin(SocialInterface, SocialAuthInterface, SocialFriendInterface):
    authenticated = False
    def login(self, auth_info):
        if auth_info['username'] != 'tw' or auth_info['password'] != 'tw':
            raise AuthenticationError('login info incorrect')
        else:
            self.authenticated = True
            print "Twitter authenticated"


    def getMyProfile(self):
        if not self.authenticated:
            raise AuthenticationError('you are not authenticated')
        profile = {'firstname' : 'John', 'lastname' : 'Doe', 'profile_url' : 'http://twitter.com/johndoe'}
        return profile
