from rest_framework.throttling import UserRateThrottle

class BrustRateThrottle(UserRateThrottle):
    scope = 'burst'


class SustainedRateThrottle(UserRateThrottle):
    scope = "sustained"