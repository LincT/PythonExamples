# GUI with checkboxes for itemized service charges.
# gives total when button clicked.
# procedural generation to reduce code and generate menu.
# update values in self.services dictionary to add/update/remove services.
import tkinter

__author__ = 'LincT, https://github.com/LincT/PythonExamples'


class AutoEstimateGUI:
    def __init__(self):
        # main window and our frames
        self.mainWindow = tkinter.Tk()
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.btmFrame = tkinter.Frame(self.mainWindow)

        # service types and costs
        self.services = {
            'oil change': 30.00,
            'lube job': 20.00,
            'radiator flush': 40.00,
            'transmission flush': 100.00,
            'inspection': 35.00,
            'muffler replacement': 200.00,
            'tire rotation': 20.00,
            'espresso': 3.00
        }

        # hold the check button variables
        self.cbValues = {}

        # form generation
        for each in self.services.keys():
            titleText = each.title()
            priceText = self.services[each]
            padLength = len(titleText) + len(format(priceText, '.2f'))

            # make each an IntVar
            self.cbValues[each] = tkinter.IntVar()
            self.cbValues[each].set(0)  # set each
            self.cb = tkinter.Checkbutton(
                self.topFrame,
                text=str(each.title().ljust(40-padLength, '.') + ' $ ' + format(self.services[each], '.2f')),
                variable=self.cbValues[each])

            # pack each checkbutton as it finishes
            self.cb.pack(side='top')

        self.topFrame.pack()  # pack the frame

        self.totalLabel = \
            tkinter.Label(
                self.btmFrame,
                text='Total:\t$')

        # stringVar to hold data
        self.value = tkinter.StringVar()

        # create label, link w/ self.value
        self.estimateLabel = \
            tkinter.Label(
                self.btmFrame,
                textvariable=self.value)

        # Pack the bottom frame's labels.
        self.totalLabel.pack(side='left')
        self.estimateLabel.pack(side='left')
        # button widget
        self.myButton = \
            tkinter.Button(
                self.btmFrame,
                text='Get Estimate',
                command=self.getTotal)
        # pack the button
        self.myButton.pack(side='right')
        self.btmFrame.pack()  # pack the frame
        tkinter.mainloop()  # enter main loop

    def getTotal(self):
        total = 0.00  # initialize total
        # get our checkbutton values
        for key in self.cbValues:
            val = self.cbValues[key]
            cbVal = val.get()
            if cbVal == 1:
                total += self.services[key]
        # set the total, round to 2 places
        self.value.set(format(total, '.2f'))


my_gui = AutoEstimateGUI()
