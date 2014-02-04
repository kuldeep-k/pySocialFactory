from socialFactory.core.SocialFactory import SocialFactory
#from socialFactory.plugins import FBSocialPlugin
#from socialFactory.plugins import TwitterSocialPlugin

fbo = SocialFactory('FB')
fbv = fbo.so
print fbv
fbv.login({'username' : 'fb', 'password' : 'fb' })
print fbv.getMyProfile()



two = SocialFactory('Twitter')
twv = two.so
print twv
twv.login({'username' : 'tw', 'password' : 'tw' })
print twv.getMyProfile()

