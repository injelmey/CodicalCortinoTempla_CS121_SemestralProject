class PersonalBudgetTracker:
    def __init__(self):
        self.income = 0.0
        self.expenses = {}
        sel.categories = []
        self.loadData()
    
    def addIncome(self, amount):
        if amount > 0:
            self.income += amount
            print(f"Income of ${amount:.2f} is added.")
        else:
            print("Income should be a positive amount or number.")

    def createCategory(self, category):
        if category not in self.categories:
            self.categories.append(category)
            print(f"Category '{category}' created.")
        else:
            print(f"Category '{category}' is already exists.")

    def getBalance(self, category):
        if category not in self.categories:
            print(f"Category '{category}' does not exist.")
            return 0.0

        spent = self.expenses.get(category, 0)
        balance = self.income - spent
        print(f"Remaining budget for category '{category}': ${balance:.2f}")
        return balance

    def getTotalSpent(self):
        total_spent = sum(self.expenses.values())
        return total_spent
