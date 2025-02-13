from rest_framework.throttling import UserRateThrottle

class SanjanaRateThrottle(UserRateThrottle):
    scope = 'sanjana'