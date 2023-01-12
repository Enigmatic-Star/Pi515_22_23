n=23
def enforce_even(n):
  """
  Checks if n is even and raises an
  exception if it is not.

  HINT: recall that the % operator
  will give you the remainder of a/b
  in a%b.
  """
  # Implement the function
  if n%2 !=0:
    #print(n%2)
    raise Exception("oops")
try:
  enforce_even(3)
except:
  print("Exception raised successfully.")
else:
  print("Exception failed to raise.")
