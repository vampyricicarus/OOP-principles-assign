
class BudgetCategory:

    def __init__(self, food, entertainment, utilities):
        self.__food = food
        self.__entertainment = entertainment
        self.__utilities = utilities

    def get_food(self):
        return self.__food

    def get_entertainment(self):
        return self.__entertainment

    def get_utilities(self):
        return self.__utilities
    
    def viewBalance(self):
        print(self.__food + self.__entertainment + self.__utilities)


def add_cost():
    food = 0
    entertainment = 0
    utilities = 0
    while True:
        category = input("Food, entertainment, or utilities? (Write F to finish) ")
        if category == "food":
            food = int(input("How much did it cost? "))
            
        elif category == "entertainment":
            entertainment = int(input("How much did it cost? "))
            
        elif category == "utilities":
            utilities = int(input("How much did it cost? "))
        elif category == "F":
            break
        else:
            print("Invalid selection")
    return food, entertainment, utilities

def main():
    bill1 = None
    while True:
        
        menu = "1. Define budget\n2. View balance\n3. Exit"
        print(menu)
        selectItem = input("Select item by numeral: ")
        if selectItem == "1":
            food, entertainment, utilities = add_cost()
            bill1 = BudgetCategory(food, entertainment, utilities)
            
        elif selectItem == "2":
            if bill1 == None:
                print("There is no balance for now")
            else:
                bill1.viewBalance()
        elif selectItem == "3":
            break
        else:
            print("Invalid selection")
            
main()
    
