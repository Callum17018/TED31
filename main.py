"""
Canteen Ordering System
By Callum Rutledge
"""

# Imports
import GUI.CanteenGUI
import GUI.ShoppingCart as Shopping


# Starts the shopping cart variable
shopping_cart = Shopping.Cart()


def main():
    """ Main method to run everything """
    if __name__ == '__main__':
        GUI.CanteenGUI.openGUI()


# Runs the program
main()
