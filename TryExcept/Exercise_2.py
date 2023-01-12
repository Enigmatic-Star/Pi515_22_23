def greet(name):
  try:
    greeting = "Hello " + name + "!"
    print(greeting)
  # Add TypeError handling
    print("ValueError")
  # Add a catch-all exception
    print("something else went wront")
  except:
    name = None

# Test the function below

greet('Kristen')
greet(None)