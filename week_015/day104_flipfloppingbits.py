# Given a positive integer N, return whether or not it has alternating bit values.

# Ex: Given the following value for N…

# N = 5, return true.
# 5 in binary is 101 which alternates bit values between 0 and 1.
# Ex: Given the following value for N…

# N = 8, return false
# 8 in binary is 1000 which does not alternate bit values between 0 and 1.
# Time O(logn)
# Space O(logn)
def flifloppingbits(N):
  bin_N = bin(N)[2:]

  for i in range(1,len(bin_N)):
    if bin_N[i] == bin_N[i-1]:
      return False
  return True

print(flifloppingbits(5))
print(flifloppingbits(8))