"""
This is the GUI class which opens the GUI
"""
from appJar import gui
import ctypes
import Backend.FromData as fd

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def openGUI():
    canteen_gui = GUI()
    canteen_gui.start_app()
    return canteen_gui


class GUI:
    # Initialise the app
    def __init__(self):
        app = gui("RHS Canteen", "fullscreen")
        app.setBg("Gainsboro")
        app.setFont(16)
        app.setImageLocation("GUI/images")

        self._app = app

        self.add_side_bar()

    def add_side_bar(self):
        fill_color = "SkyBlue"
        self._app.addCanvas("sidebar")
        self._app.addCanvasCircle("sidebar", -70, -20, 200, fill=fill_color, outline=fill_color)
        self._app.addCanvasRectangle("sidebar", 0, 67, 130, 1080, fill=fill_color, outline=fill_color)

        self.add_exit_button()
        self.add_cart_button()
        self.add_menu_items()
        self.add_running_total()

    def add_exit_button(self):
        self._app.setSticky("sw")
        self._app.setPadding([21, 20])
        self._app.addButton("Exit", self.exit, colspan=0, column=0, row=0)

    def add_cart_button(self):
        self._app.setSticky("nw")
        self._app.setPadding([30, 50])
        self._app.addIconButton("Cart", self.cart, "cart-alt-1", colspan=0, column=0, row=0)
        self._app.setPadding([2, 90])
        self._app.addLabel("Checkout", colspan=0, row=0, column=0)

        self._app.setLabelBg("Checkout", "Skyblue")

    def add_menu_items(self):
        self._app.setPadding([450, 30])
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
        self._app.startTab("Breakfast")

        self._app.setSticky("ew")
        self._app.setFont(20)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Breakfast"))
        for x in range(5):
            for y in range(5):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Breakfast"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 20)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()

    def menu_add_cold_food(self):
        self._app.startTab("Cold Food")

        self._app.setSticky("ew")
        self._app.setFont(20)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Cold Food"))
        for x in range(5):
            for y in range(5):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Cold Food"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 20)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()

    def menu_add_hot_food(self):
        self._app.startTab("Hot Food")
        print("\nHot Food")

        self._app.setSticky("ew")
        self._app.setFont(20)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Hot Food"))
        for x in range(5):
            for y in range(5):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Hot Food"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y
                    print(f"{data_name}, {data_price}")
                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 20)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()

    def menu_add_ice_blocks(self):
        self._app.startTab("Ice blocks")

        self._app.setSticky("ew")
        self._app.setFont(20)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Ice Blocks"))
        for x in range(5):
            for y in range(5):
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
        self._app.startTab("Drinks")

        self._app.setSticky("ew")
        self._app.setFont(20)
        counter = 0
        len_of_data = fd.get_length(fd.get_data("Drinks"))
        for x in range(5):
            for y in range(5):
                if counter < len_of_data:
                    data_name, data_price = fd.get_item_and_price(fd.get_data("Drinks"), counter)
                    name = f"{data_name}\n${data_price}"
                    x1 = x
                    y1 = y

                    self._app.addButton(name, self.add, row=x, column=y)
                    self._app.setButtonHeights(name, 7)
                    self._app.setButtonWidths(name, 20)
                    self._app.setButtonBg(name, "White")
                    counter += 1

        self._app.stopTab()

    def add_running_total(self):
        self._app.setPadding([150, 30])
        self._app.startFrame("Total", colspan=0, row=0, column=0)
        self._app.startLabelFrame("Running_Total", colspan=0, column=0, row=0)

        self._app.addLabel("--------------------------")
        for num in range(1, 10):
            self._app.addLabel(f"Order Num: {num}\nFOODNAME", colspan=0, row=num, column=0)

        self._app.stopLabelFrame()
        self._app.stopFrame()

    def exit(self, button):
        if button == "Exit":
            self._app.stop()

    def cart(self, button):
        if button == "Cart":
            print("CART TIME")

    def add(self, button):
        if button == "Add 1 1,1":
            print("Adding")

    # To Start the GUI
    def start_app(self):
        self._app.go()