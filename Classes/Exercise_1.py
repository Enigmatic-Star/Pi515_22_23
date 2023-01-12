# Create a class for contact information
# Use the included Template.py as reference

# 1. Define a class called contact
# 2. Write the constructor
# 3. Create instance variables for the following:
#   - First name (argument 1)
#   - Last name (argument 2)
#   - Phone number (argument 3)
#   - Blocked status  (default false)
# 4. Create an instance method which changes
# the blocked status from false to true

class contact:

  isBlocked = False

  def __init__(self, first, last, phone):
    self.firstName = first # 'Kristen'
    self.lastName = last # 'Bruce'
    self.phone = phone # '1234567890'

  def toggleBlocked(self):
    if self.isBlocked == True:
      self.isBlocked = False
    else:
      self.isBlocked = True

x = contact('Kristen', 'Bruce', '1234567890')
print(x.firstName)
print(x.lastName)
print(x.phone)
print(x.isBlocked)
x.toggleBlocked()
print(x.isBlocked)

print('\n')

y = contact('Jordan', 'Boerger', '0987654321')
print(y.firstName)
print(y.lastName)
print(y.phone)
print(y.isBlocked)