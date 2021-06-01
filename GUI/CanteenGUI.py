"""
This is the GUI class which opens the GUI
"""
from appJar import gui
import main as main
import ctypes
import Backend.FromData as fd

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def openGUI():
    """ Opens the GUI """
    canteen_gui = GUI()
    canteen_gui.start_app()
    return canteen_gui


class GUI:
    """ Runs the GUIs internal components """

    def __init__(self):
        """ Starts the App with appjar"""
        app = gui("RHS Canteen", "fullscreen")
        app.setBg("Gainsboro")
        app.setFont(size=10)
        app.setImageLocation("GUI/images")

        self._app = app

        self.add_side_bar()

    def add_side_bar(self):
        """ Adds a nice looking sidebar and
        starts the proccess of creating the widgets on the gui
        """
        fill_color = "SkyBlue"
        self._app.addCanvas("sidebar")
        self._app.addCanvasCircle("sidebar", -70, -20, 200, fill=fill_color, outline=fill_color)
        self._app.addCanvasRectangle("sidebar", 0, 67, 130, 1080, fill=fill_color, outline=fill_color)

        self.add_exit_button()
        self.add_cart_button()
        self.add_menu_items()
        self.add_running_total()

    def add_exit_button(self):
        """ Makes the exit button and places it on the GUI """
        self._app.setSticky("sw")
        self._app.setPadding([21, 20])
        self._app.addButton("Exit", self.exit, colspan=0, column=0, row=0)

    def add_cart_button(self):
        """ Makes the cart button and places it on the GUI """
        self._app.setSticky("nw")
        self._app.setPadding([30, 50])
        self._app.addIconButton("Cart", self.cart, "cart-alt-1", colspan=0, column=0, row=0)
        self._app.setPadding([2, 90])
        self._app.addLabel("Checkout", colspan=0, row=0, column=0)

        self._app.setLabelBg("Checkout", "Skyblue")

    def add_menu_items(self):
        """ Makes the menu items and places them on the GUI """
        self._app.setPadding([480, 30])
        self._app.startFrame("Items", colspan=0, row=0, column=0)

        self._app.startLabelFrame("Menu", colspan=0, column=0, row=0)
        self._app.startTabbedFrame("Menu_Items")

        self.menu_add_breakfast()
        self.menu_add_hot_food()
        self.menu_add_cold_food()
        self.menu_add_ice_blocks()
        self.menu_add_drinks()

        self._app.stopTabbedFrame()
        self._app.stopLabelFrame()
        self._app.stopFrame()

    def menu_add_breakfast(self):
        """ Makes the menu items and places them on the GUI """
        self._app.startTab("Breakfast")

        self._app.setSticky("ew")
        self._app.setFont(18)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Breakfast"))
        for x in range(4):
            for y in range(4):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Breakfast"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 25)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()


    def menu_add_cold_food(self):
        """ Makes the menu items and places them on the GUI """
        self._app.startTab("Cold Food")

        self._app.setSticky("ew")
        self._app.setFont(18)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Cold Food"))
        for x in range(4):
            for y in range(4):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Cold Food"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 25)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()


    def menu_add_hot_food(self):
        """ Makes the menu items and places them on the GUI """
        self._app.startTab("Hot Food")

        self._app.setSticky("ew")
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Hot Food"))
        for x in range(4):
            for y in range(4):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Hot Food"), counter)

                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y
                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 25)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()


    def menu_add_ice_blocks(self):
        """ Makes the menu items and places them on the GUI """
        self._app.startTab("Ice blocks")

        self._app.setSticky("ew")
        self._app.setFont(size=6)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Ice Blocks"))
        for x in range(4):
            for y in range(4):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Ice Blocks"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 20)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()


    def menu_add_drinks(self):
        """ Makes the menu items and places them on the GUI """
        self._app.startTab("Drinks")


        self._app.setSticky("ew")
        self._app.setFont(18)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Drinks"))

        for x in range(4):
            for y in range(4):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Drinks"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 25)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()


    def add_running_total(self):
        """ Makes the running total and places them on the GUI """
        self._app.setPadding([140, 30])
        self._app.startFrame("Total", colspan=0, row=0, column=0)
        self._app.startLabelFrame("Running_Total", colspan=0, column=0, row=0)

        self._app.addLabel("----------------------------------------")

        self._app.stopLabelFrame()
        self._app.stopFrame()


    def refresh_totals(self):
        """ Updates the running totals frame """

        self._app.openFrame("Total")
        cart = main.shopping_cart.get_items()
        self._app.emptyCurrentContainer()
        self._app.startLabelFrame("Running_Total", colspan=0, column=0, row=0)

        self._app.addLabel("----------------------------------------")

        count = 1
        for item in cart:
            price, amount = cart[item]
            self._app.addLabel(f"{amount}x {item}: ${price * amount}", colspan=0, row=count, column=0)
            count += 1

        self._app.stopLabelFrame()
        self._app.stopFrame()


    def exit(self, button):
        """ Run when the exit button is pressed """
        if button == "Exit":
            self._app.stop()


    def order(self, button):
        """ Run when the order button is pressed """
        if button == "Order":
            self._app.stop()


    def cart(self, button):
        """ Run when the cart button is pressed """
        if button == "Cart":
            self._app.hide()
            self._app.startSubWindow("Checkout", modal=True)
            # self._app.addLabel("l1", "Checkout")
            self._app.setSize(400, 400)

            self._app.addLabel("checkout_total", f"  Checkout Total: ${main.shopping_cart.get_total_cost()}  ", row=0)
            self._app.setLabelBg("checkout_total","Blue")

            self._app.addLabelEntry("Name")
            self._app.addLabelEntry("ID/Cypher")
            self._app.addLabelEntry("Class")

            self._app.addButton("Order", self.order)

            self._app.stopSubWindow()
            self._app.showSubWindow("Checkout")


    def add(self, button):
        """ Run when the any menu item is pressed """
        print(main.shopping_cart.get_items())
        split = button.split("\n")
        split[1] = float(split[1].replace('$', ''))
        main.shopping_cart.add_item(split[0], split[1])
        self.refresh_totals()



    # To Start the GUI
    def start_app(self):
        """ Actually vissily opens the window """
        self._app.go()
