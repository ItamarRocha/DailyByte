"""
This question is asked by Facebook. Releasing software can be tricky and sometimes we release new versions of our software with bugs. 
When we release a version with a bug it’s referred to as a bad release. Your product manager has just informed you that a bug you
 created was released in one of the past versions and has caused all versions that have been released since to also be bad. 
 Given that your past releases are numbered from zero to N and you have a helper function isBadRelease(int releaseNumber) that 
 takes a version number and returns a boolean as to whether or not the given release number is bad, return the release number 
 that your bug was initially shipped in.
Note: You should minimize your number of calls made to isBadRelease().

Ex: Given the following value N…

N = 5 and release number four is the release your bug was shipped in...
isBadRelease(3) // returns false.
isBadRelease(5) // returns true.
isBadRelease(4) // returns true.

return 4.
"""
class Software():
    def __init__(self, N, bad_release):
        self.N = N
        self.bad_release = bad_release
    
    def isBadRelease(self, n):
        if n >= self.bad_release:
            return True
        return False
    
    def findBadRelease(self):
        l = 0
        r = self.N

        while l <= r:
            mid = (l+r)//2
            if not self.isBadRelease(mid - 1) and self.isBadRelease(mid):
                return mid
            elif not self.isBadRelease(mid) and self.isBadRelease(mid + 1):
                return mid + 1
            elif not self.isBadRelease(mid):
                l = mid + 1
            elif self.isBadRelease(mid):
                r = mid - 1
        
        return mid

s = Software(5,4)
print(s.findBadRelease())
