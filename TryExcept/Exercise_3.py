def exponentiate(x, exp):
  """
  Prints the result of x^exp
  """
  try:
    result = x**exp
    print(result)
  # [Optional] Add specific exception handling
  # Add a catch-all exception
  # Add an else clause that prints the result
  # Add a finally clause

  except:
    print("uh oh we've got an error")
  else:
    print("executed successfully")
  finally:
    print("have a nice day!")
  
    
# Test the function below
exponentiate(2, 2)
exponentiate("Kristen", 4)