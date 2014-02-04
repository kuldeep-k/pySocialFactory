class SocialFriendInterface:
    def getMyFriends(self):
        raise NotImplementedError('method should be implemented in child class')
    def sendFriendRequest(self, user_id):
        raise NotImplementedError('method should be implemented in child class')
    def acceptFriendRequest(self, user_id):
        raise NotImplementedError('method should be implemented in child class')
    def declineFriendRequest(self, user_id):
        raise NotImplementedError('method should be implemented in child class')
