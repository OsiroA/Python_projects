class Category:
    # This makes it possible to instantiate objects based on different categories
    # Creates an instance variable called ledger that is a list
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.balance = 0
    def __str__(self):
      title = f"{self.category_name.center(30, '*')}\n"
      items = ""
      total = 0
      for item in self.ledger:
        items += f"{item['description'][0:23].ljust(23)}{item['amount']:>7.2f}\n"
        total += item['amount']
      output = title + items + f"Total: {total:.2f}"
      return output
    # The class also contains the methods below
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        self.balance = balance
        return self.balance

    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another_category.category_name}")
            another_category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    # The following part works on the display requirements
    def get_ledger_string(self):
        # This creates the title line
        title = f"{self.category_name.center(30, '*')}\n"

        # This creates ledger lines
        ledger_lines = [f"{entry['description'][:23]:23}" \
                        f"{format(entry['amount'], '.2f'):>7}" \
                        for entry in self.ledger]

        # This joins the title, ledger lines and total lines into a single string
        total = f"\nTotal: {format(self.get_balance(), '.2f')}"
        return title + '\n'.join(ledger_lines) + total

    def get_withdrawals(self):
        withdrawals = 0
        for transaction in self.ledger:
            if transaction['amount'] < 0:
                withdrawals -= transaction['amount']
        return withdrawals

def create_spend_chart(categories):
    # Calculate percentage spent for each category
    total_withdrawals = sum(category.get_withdrawals() for category in categories)
    percentages = [int(category.get_withdrawals() / total_withdrawals * 10) * 10 for category in categories]

    # Create horizontal line and labels
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:>3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * len(categories) * 3 + "-\n"

    # Get maximum length of category names
    max_length = max(len(category.category_name) for category in categories)

    # Add vertical category names
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category_name):
                chart += category.category_name[i] + "  "
            else:
                chart += "   "
        if i != max_length - 1:
            chart += "\n"

    return chart