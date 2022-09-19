import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys, os, signal, colorama

colorama.init()  # Color init for Windows

# =======================
# #    DEFINES
# # =======================

colors = {
    "info": "35m",  # Orange for info messages
    "error": "31m",  # Red for error messages
    "ok": "32m",  # Green for success messages
    "menu2c": "\033[46m",  # Light blue menu
    "menu1c": "\033[44m",  # Blue menu
    "close": "\033[0m"  # Color coding close
}
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]

# =======================
#    USER CONFIG
# =======================
programtitle = "COVID ANALYSIS"

menu1_colors = {
    "ct": ct,
    "cs": cs,
    "opt": c1
}
menu1_options = {
    "title": "Main Menu",
    "1": "Show Data Frame",
    "2": "ADD Data",
    "3": "Edit Data",
    "4": "DELETE DATA",
    "5": "LINE GRAPH",
    "6": "BAR GRAPH",
    "7": "Quit (or use CNTRL+C)",
}


# =======================
#      HELPERS
# =======================
def printWithColor(color, string):
    print("\033[" + colors[color] + " " + string + cc)


def printError():
    printWithColor("error", "Error!!")
    return 1


def printSuccess():
    printWithColor("ok", "Success!!")
    return 0


# Exit program
def exit():
    sys.exit()


# Handles the CNTRL+C to leave properly the script
def sigint_handler(signum, frame):
    print("CNTRL+C exit")
    sys.exit(0)


# =======================
#      ACTIONS
# =======================

# Menu template
class menu_template():

    def __init__(self, options, colors):
        self.menu_width = 50  # Width in characters of the printed menu
        self.options = options
        self.colors = colors

    # =======================
    #      Menu prints
    # =======================
    def createMenuLine(self, letter, color, length, text):
        menu = color + " [" + letter + "] " + text
        line = " " * (length - len(menu))
        return menu + line + cc

    def createMenu(self, size):
        line = self.colors["ct"] + " " + programtitle
        line += " " * (size - len(programtitle) - 6)
        line += cc
        print(line)  # Title
        line = self.colors["cs"] + " " + self.options["title"]
        line += " " * (size - len(self.options["title"]) - 6)
        line += cc
        print(line)  # Subtitle
        for key in self.options:
            if (key != "title"):
                print(self.createMenuLine(key, self.colors["opt"], size, self.options[key]))

    def printMenu(self):
        self.createMenu(self.menu_width)

    # =======================
    #      Action calls
    # =======================
    def action(self, ch):
        if ch == '1':
            self.show_data()
        elif ch == '2':
            self.Enter_data()
        elif ch == '3':
            self.edit_data()
        elif ch == '4':
            self.del_data()
        elif ch == '5':
            self.line_chart()
        elif ch == '6':
            self.bar_chart()
        elif ch == '0':
            sys.exit()
        else:
            printError()

    def show_data(self):
        df = pd.read_csv("covid_19.csv")
        print(df)
        input("Press any key to continue")

    def edit_data(self):
        df = pd.read_csv("Covid_19.csv")
        di = input("Enter the State Name:")
        colu = input("Enter The Column To UpDATE")
        values = input("Enter Records")
        df.loc[df[df["State"] == di].indeex.values, colu] = values
        df.to_csv("Covid_19.csv")
        print("Record Has Been Updated..")
        input("Press Any key TO Continue")

    def Enter_data(self):
        print("Insert Data of into The Record:")
        d = eval(input("Enter the State Name"))
        pcase = eval("Enter no. Of Confirmed Caes:")
        rcase = eval("Enter no . Of Recovered Cases:")
        death = eval("Enter no. of Death cases:")
        active = eval("Enter no. Of Actuve Cases:")
        p = {'Districts': d, 'Confirmed': pcase, 'Recovered': rcase, 'Deaths': death, 'Active': active}
        df = pd.DataFrame(p)
        df.to_csv("Covid_19.csv", mode='a', index=False, head=False)
        print("Data Entered")
        input("Press Any Key To Continue....")

    def del_data(self):
        di = input("Enter the State Name")
        df = pd.read_csv("Covid_19.csv")
        df = df[df.Districts]
        df.to_csv("Covid_19.csv", index=False)
        print("Record Deleted...")
        input("'Press any key to continue")

    def line_chart(self):
        df = pd.read_csv("Covid_19.csv")
        state = df["State"]
        con = df["Confirmed"]
        rec = df["Recovered"]
        death = df["Deaths"]
        active = df["Active"]
        Y = 0
        print("____________________========================================================________________________")
        print("                                   LINE GRAPH")
        print("____________________=========================================================_______________________")
        print("1.State Wise Confirmed CASES")
        print("2.State Wise Recovered Cases")
        print("3.State Wise Death Case")
        print("4.State Wise Active Cases")
        print("5.All Data")
        print("Return")
        print("____________________===========================================================____________________")
        Y = 0
        while Y != 4:
            Y = int(input("Enter the Choice to plot  LIne Graph:"))
        if Y == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("State Wise Confirmed Cases")
            plt.plot(state, con, color="b")
            plt.show()
        elif Y == 2:
            plt.ylabel("Recovered cases")
            plt.title("State Wise Recovered Cases")
            plt.plot(state, rec, color="b")
            plt.show()
        elif Y == 3:
            plt.ylabel("Death Cases")
            plt.title("State Wise Death Report")
            plt.plot(state, death, color="b")
            plt.show()
        elif Y == 4:
            plt.ylabel("Active Cases")
            plt.title("State Wise active Cases")
            plt.plot(state, active, color="b")
            plt.show()
        elif Y == 5:
            plt.ylabel("Number OF Cases")
            plt.plot(state, con, color='b', label='State Wise Confurmd Cases')
            plt.plot(state, rec, color='g', label='State Wise Recovered Cases')
            plt.plot(state, death, color='c', label='State Wise Death Cases')
            plt.plot(state, active, color='r', label='State Wise Active Cases')
            plt.legend()
            plt.show()
        elif Y == 6:
            print("Closing Line Graph Interface")
        else:
            print("Sorry Invalid Option..")

    def bar_chart(self):
        df = pd.read_csv("Covid_19.csv")
        state = df["State"]
        con = df["Confirmed"]
        rec = df["Recovered"]
        death = df["Deaths"]
        active = df["Active"]
        Y = 0
        print("____________________========================================================________________________")
        print("                                   BAR GRAPH")
        print("____________________=========================================================_______________________")
        print("1.State Wise Confirmed CASES")
        print("2.State Wiswe Recovered Cses")
        print("3.State Wise Death Case")
        print("4.State Wise Active Cases")
        print("5.All Data")
        print("6.Combine Bar")
        print("Return")
        print("____________________===========================================================____________________")
        Y = 0
        while Y != 5:
            Y = int(input("Enter the Choice to plot  BAR Graph"))
            if Y == 1:
                plt.ylabel("Confirmed Cases")
                plt.title("State Wise Confirmed Cases")
                plt.bar(state, con, color="b", width=0.5)
                plt.show()
            elif Y == 2:
                plt.ylabel("Recovered cases")
                plt.title("State Wise Recovered Cases")
                plt.bar(state, rec, color="g", width=0.5)
                plt.show()
            elif Y == 3:
                plt.ylabel("Death Cases")
                plt.title("State Wise Death Report")
                plt.bar(state, death, color="c", width=0.5)
                plt.show()
            elif Y == 4:
                plt.ylabel("Active Cases")
                plt.title("State Wise active Cases")
                plt.bar(state, active, color="r", width=0.5)
                plt.show()
            elif Y == 5:
                plt.ylabel("Number OF Cases")
                plt.bar(state, con, color='b', width=0.5, label='State Wise Confurmd Cases')
                plt.bar(state, rec, color='g', width=0.5, label='State Wise Recovered Cases')
                plt.bar(state, death, color='c', width=0.5, label='State Wise Death Cases')
                plt.bar(state, active, color='r', widht=0.5, label='State Wise Active Cases')
                plt.legend()
                plt.show()
            elif Y == 6:
                d = np.arange(len(state))
                w = 0.25
                plt.bar(d, con, w, color='b', label='Sate Wise Confirmed Case')
                plt.bar(d + 0.25, rec, w, color='g', label='Sate Wise Recovered Case')
                plt.bar(d + 0.50, death, w, color='c', label='Sate Wise Death Case')
                plt.bar(d + 0.75, active, w, color='r', label='Sate Wise Active Case')
                plt.legend()
                plt.show()
            elif Y == 7:
                print('Closing Bar Graph.....')
            else:
                print("Sorry Invalid Option..")


class menu1(menu_template):
    pass


# =======================
#      MAIN PROGRAM
# =======================

class menu_handler:

    def __init__(self):
        self.current_menu = "main"
        self.m1 = menu1(menu1_options, menu1_colors)

    def menuExecution(self):
        if (self.current_menu == "main"):
            self.m1.printMenu()
        choice = input(" >> ")
        if (self.current_menu == "main"):
            if (choice == "9"):
                self.current_menu = "second"
            else:
                self.actuator(0, choice)
        if (choice == "1"):
            self.m1.show_data()
        else:
            if choice == "2":
                self.m1.Enter_data()
            if choice == "3":
                self.m1.edit_data()
            if choice == "4":
                self.m1.del_data()
            if choice == "5":
                self.m1.line_chart()
            if choice == "6":
                self.m1.bar_chart()

        print("\n")

    def actuator(self, type, ch):
        if type == 0:
            self.m1.action(ch)


# Main Program
if __name__ == "__main__":
    x = menu_handler()
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        x.menuExecution()


def show_data():
    df = pd.read_csv("covid_19.csv")
    print(df)
    input("Press any key to continue")


def Enter_Data():
    print("Insert Data of into The Record:")
    d = eval(input("Enter the State Name"))
    pcase = eval("Enter no. Of Confirmed Caes:")
    rcase = eval("Enter no . Of Recovered Cases:")
    death = eval("Enter no. of Death cases:")
    active = eval("Enter no. Of Actuve Cases:")
    p = {'Districts': d, 'Confirmed': pcase, 'Recovered': rcase, 'Deaths': death, 'Active': active}
    df = pd.DataFrame(p)
    df.to_csv("Covid_19.csv", mode='a', index=False, head=False)
    print("Data Entered")
    input("Press Any Key To Continue....")


def edit_data():
    df = pd.read_csv("Covid_19.csv")
    di = input("Enter the State Name:")
    colu = input("Enter The Column To UpDATE")
    values = input("Enter Records")
    df.loc[df[df["State"] == di].indeex.values.colu] = values
    df.to_csv("Covid_19.csv")
    print("Record Has Been Updated..")
    input("Press Any key TO Continue")


def del_data():
    di = input("Enter the State Name")
    df = pd.read_csv("Covid_19.csv")
    df = df[df.Districts]
    df.to_csv("Covid_19.csv", index=False)
    print("Record Deleted...")
    input("'Press any key to continue")


def line_chart():
    df = pd.read_csv("Covid_19.csv")
    state = df["State"]
    con = df["Confirmed"]
    rec = df["Recovered"]
    death = df["Deaths"]
    active = df["Active"]
    Y = 0
    print("____________________========================================================________________________")
    print("                                   LINE GRAPH")
    print("____________________=========================================================_______________________")
    print("1.State Wise Confirmed CASES")
    print("2.State Wise Recovered Cases")
    print("3.State Wise Death Case")
    print("4.State Wise Active Cases")
    print("5.All Data")
    print("Return")
    print("____________________===========================================================____________________")
    Y = 0
    while Y != 4:
        Y = int(input("Enter the Choice to plot  LIne Graph:"))
    if Y == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("State Wise Confirmed Cases")
        plt.plot(state, con, color="b")
        plt.show()
    elif Y == 2:
        plt.ylabel("Recovered cases")
        plt.title("State Wise Recovered Cases")
        plt.plot(state, rec, color="b")
        plt.show()
    elif Y == 3:
        plt.ylabel("Death Cases")
        plt.title("State Wise Death Report")
        plt.plot(state, death, color="b")
        plt.show()
    elif Y == 4:
        plt.ylabel("Active Cases")
        plt.title("State Wise active Cases")
        plt.plot(state, active, color="b")
        plt.show()
    elif Y == 5:
        plt.ylabel("Number OF Cases")
        plt.plot(state, con, color='b', label='State Wise Confurmd Cases')
        plt.plot(state, rec, color='g', label='State Wise Recovered Cases')
        plt.plot(state, death, color='c', label='State Wise Death Cases')
        plt.plot(state, active, color='r', label='State Wise Active Cases')
        plt.legend()
        plt.show()
    elif Y == 6:
        print("Closing Line Graph Interface")
        menu_template
    else:
        print("Sorry Invalid Option..")
        menu_template


def bar_chart():
    df = pd.read_csv("Covid_19.csv")
    state = df["State"]
    con = df["Confirmed"]
    rec = df["Recovered"]
    death = df["Deaths"]
    active = df["Active"]
    Y = 0
    print("____________________========================================================________________________")
    print("                                   BAR GRAPH")
    print("____________________=========================================================_______________________")
    print("1.State Wise Confirmed CASES")
    print("2.State Wiswe Recovered Cses")
    print("3.State Wise Death Case")
    print("4.State Wise Active Cases")
    print("5.All Data")
    print("6.Combine Bar")
    print("Return")
    print("____________________===========================================================____________________")
    Y = 0
    while Y != 5:
        Y = int(input("Enter the Choice to plot  BAR Graph"))
        if Y == 1:
            plt.ylabel("Confirmed Cases")
            plt.title("State Wise Confirmed Cases")
            plt.bar(state, con, color="b", width=0.5)
            plt.show()
        elif Y == 2:
            plt.ylabel("Recovered cases")
            plt.title("State Wise Recovered Cases")
            plt.bar(state, rec, color="g", width=0.5)
            plt.show()
        elif Y == 3:
            plt.ylabel("Death Cases")
            plt.title("State Wise Death Report")
            plt.bar(state, death, color="c", width=0.5)
            plt.show()
        elif Y == 4:
            plt.ylabel("Active Cases")
            plt.title("State Wise active Cases")
            plt.bar(state, active, color="r", width=0.5)
            plt.show()
        elif Y == 5:
            plt.ylabel("Number OF Cases")
            plt.bar(state, con, color='b', width=0.5, label='State Wise Confurmd Cases')
            plt.bar(state, rec, color='g', width=0.5, label='State Wise Recovered Cases')
            plt.bar(state, death, color='c', width=0.5, label='State Wise Death Cases')
            plt.bar(state, active, color='r', widht=0.5, label='State Wise Active Cases')
            plt.legend()
            plt.show()
        elif Y == 6:
            d = np.arange(len(state))
            w = 0.25
            plt.bar(d, con, w, color='b', label='Sate Wise Confirmed Case')
            plt.bar(d + 0.25, rec, w, color='g', label='Sate Wise Recovered Case')
            plt.bar(d + 0.50, death, w, color='c', label='Sate Wise Death Case')
            plt.bar(d + 0.75, active, w, color='r', label='Sate Wise Active Case')
            plt.legend()
            plt.show()
        elif Y == 7:
            print('Closing Bar Graph.....')
        else:
            print("Sorry Invalid Option..")
            
            
            doneby kiran
