# Create a class to hold your contact list
# 1. Define a class called contactList
# 2. Create a class variable list
# 3. Create an instance method called printList()
#  to print class variable list

# 4. Below your class definition, create a
#  new instance of contactList
# 5. Create 2 contacts and add them to list
#  inside your contactList object
# 6. Run your instance method printList()

from Exercise_1 import contact

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

class contactList:
  def --init--(self):
    self.list = []

  def printList(self):
    for i in self.list:
      print(i.firstName, i.lastName)
    
jordan = contact('Jodan', 'Boerger', '123')

matt = contact('Matt', 'O', '456')

addressBook = contactList()
addressBook.list.append(jordan)
addressBook.list.append(matt)
x = contact('Jordan', 'Boerger', '123')

print(x.firstName)