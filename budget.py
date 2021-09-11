import math

class Category:
  def __init__ (self, name = "", amount = 0):
    amount = round(amount, 2)
    self.name = name
    self.balance = amount
    self.ledger = []
    self.totalSpent = 0

  def __str__(self):
    printString = self.name.center(30, '*') + '\n'

    for line in self.ledger:
      desc = line["description"]

      entry = "{:.2f}".format(float(line["amount"]))
      if((len(entry) + len(desc)) > 30):
        desc = desc[0:30 - len(entry) - 1]


      printString += desc + entry.rjust(30 - len(desc), ' ') + '\n'
    printString += "Total: " + str(self.balance)
    return printString


  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def deposit(self, amount, description = ""):
    amount = round(amount, 2)
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
    return True

  def withdraw(self, amount, description = ""):
    amount = round(amount, 2)
    if not self.check_funds(amount):
      return False
    self.balance -= amount
    self.ledger.append({"amount": -1 * amount, "description": description})
    self.totalSpent += amount
    return True
  
  
  def formatDolars(amount):
    return str(math.floor(amount)) + "." + str(math.floor(amount * 100) % 100)

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destinationCategory):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + destinationCategory.name)
      destinationCategory.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

def create_spend_chart(categories):
  spentAllCategories = 0
  percentages = []

  for category in categories:
    spentAllCategories += category.totalSpent

  for category in categories:
    percentage = math.floor(category.totalSpent / spentAllCategories * 100)
    percentages.append({"name": category.name, "percentage": percentage, "length": len(category.name)})

  chart = "Percentage spent by category\n"

  i = 100

  while not(i < 0):
    chart += str(i).rjust(3, ' ') + '|'
    for percentage in percentages:
      if percentage["percentage"] < i:
        chart += "   "
      else:
        chart += " o "
    chart += " "
    chart += '\n'
    i -= 10
  chart += "    "

  longestNameLength = 0

  for percentage in percentages:
    if percentage["length"] > longestNameLength:
      longestNameLength = percentage["length"]
    chart += "---"
  chart += "-"
  chart += "\n    "

  i = 0

  while i < longestNameLength:
    for percentage in percentages:
      if i < percentage["length"]:
        chart += ' ' + percentage["name"][i] + ' '
      else:
        chart += "   "
    chart += " "
    if i != longestNameLength - 1:
      chart += "\n    "
    i += 1

  return chart