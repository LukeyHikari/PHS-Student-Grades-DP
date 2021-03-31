import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import StringVar
import exportgrade as exgrades
import sycreator

class App:
    def __init__(self, root):
        #setting title
        root.title("PyGraPre")
        #setting window size
        width=750
        height=381
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg = '#383737')

        directorydisplaytext = StringVar()

        quarters = ["Quarter 1","Quarter 2","Quarter 3","Quarter 4"]
        dropquarter = tk.StringVar(root)
        dropquarter.set(quarters[0])
        dpdqt = tk.OptionMenu(root, dropquarter, *quarters)
        dpdqt.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdqt.place(x=20,y=15)
        dpdqt.pack
        def qtselect(*args):
            global dpqt
            dpqt = str(dropquarter.get())
            return(dpqt)
        dropquarter.trace("w", qtselect)

        dpdsections = ["Aguinaldo", "Agoncillo"]
        dropsects = tk.StringVar(root)
        dropsects.set(dpdsections[0])
        dpdst = tk.OptionMenu(root, dropsects, *dpdsections)
        dpdst.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdst.place(x=140,y=15)
        dpdst.pack
        def stselect(*args):
            global dpst
            dpst = str(dropsects.get())
            return (dpst)
        dropsects.trace("w", stselect)

        dpdschooly = ["2020-2021", "2021-2022"]
        dropschooly = tk.StringVar(root)
        dropschooly.set(dpdschooly[0])
        dpdsy = tk.OptionMenu(root, dropschooly, *dpdschooly)
        dpdsy.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdsy.place(x=260,y=15)
        dpdsy.pack
        def syselect(*args):
            global dpsy
            dpsy = str(dropschooly.get())
            return dpsy
        dropschooly.trace("w", syselect)

        qtsecsydirectory= tk.Message(root)
        ft = tkFont.Font(family='Times', size=14)
        qtsecsydirectory["width"] = "10000"
        qtsecsydirectory["font"] = ft
        qtsecsydirectory["bg"] = "#8a8a8a"
        qtsecsydirectory["fg"] = "#f4f4f4"
        qtsecsydirectory["justify"] = "left"
        qtsecsydirectory["textvariable"] = directorydisplaytext
        qtsecsydirectory.place(x=380,y=15,width=350,height=32)
        qtsecsydirectory.pack
        
        #Directory updater
        def dupdate(*args):
            directorydisplaytext.set("Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()))
        dropschooly.trace("w",dupdate)
        dropsects.trace("w",dupdate)
        dropquarter.trace("w",dupdate)
        
        directorydisplaytext.set("Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()))
        
        def addptcmd(*args): #Add PT
            print("Adding Performance Task")


        def addwtcmd(*args): #Add WT
            print("Adding Written Task")


        def findstudwmisactcmd(*args): #Find Stud Mis Act
            print("Finding Student With Missing Activities")


        def createsycmd(*args): #Create S.Y.
            print("Creating School Year")
            sycreator.sycreate(crsy, sy, sec, numstud)


        def addstudscmd(*args): #Add Studs
            print("Adding Students")


        def recordmisactcmd(*args): #Record Missing Act.
            print("Recording Missing Activities")


        def findstudmisactcmd(*args): #Find Student's Missing Act
            print("Finding Student Missing Activities")

        def exportcmd(*args): #Experimental export command
            print("Exporting Sheet")
            exgrades.exportgrades(dpsy, dpst, dpqt)
           

        #Add Performance Task Button
        addperftask = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#f4f4f4", justify = "center", text = "Add Performance Task", command = addptcmd)
        addperftask.place(x=20,y=210,width=186,height=30)
        
        #Add Written Task Button
        addwrittask = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Add Written Task", command = addwtcmd)
        addwrittask.place(x=20,y=250,width=186,height=30)

        #Create School Year Button
        createsybut = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Create School Year", command = createsycmd)
        createsybut.place(x=220,y=210,width=189,height=30)

        #Add Students Button
        addstudbut = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Add Students", command = addstudscmd)
        addstudbut.place(x=220,y=250,width=190,height=30)

        #Find Student's Missing Acts. Button
        fstudsmisactbut = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Find Student's Missing Act.", command = findstudmisactcmd)
        fstudsmisactbut.place(x=20,y=290,width=185,height=30)

        #Record Missing Acts. Button
        recmisactbut = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Record Missing Act.", command = recordmisactcmd)
        recmisactbut.place(x=220,y=290,width=190,height=30)

        #Find Students with Missing Acts. Button
        findstudwithmisact = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Find Students with Missing Act.", command = findstudwmisactcmd)
        findstudwithmisact.place(x=120,y=330,width=189,height=30)

        #Export Button
        exportbut = tk.Button(root, bg = "#383737", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff", justify = "center", text = "Export", command = exportcmd)
        exportbut.place(x=610,y=330,width=124,height=30)

        #Display Box Updater and Input Value Storer
        tracertext = StringVar()
        displaytext = StringVar()
        inputtedtext = ""
        #Diplay Box
        displaybox = tk.Message(root, bg = "#8a8a8a", width = "10000", font= tkFont.Font(family = 'Times', size = 20), fg = "#f4f4f4", justify = "left", textvariable = displaytext)
        displaybox.place(x=20,y=60,width=707,height=129)

        def onReturn(self):
            tracertext.set(inputareabox.get())
            inputareabox.delete(0,'end')

        def assigntext(*args):
            displaytext.set(inputareabox.get())
            inputtedtext = inputareabox.get()
            print(inputtedtext)
        tracertext.trace("w", assigntext)
        
        #Input Area Box
        inputareabox = tk.Entry(root, bg = "#808585", font= tkFont.Font(family = 'Times', size = 15), fg = "#ffffff", justify = "center")
        inputareabox.bind('<Return>', onReturn)
        inputareabox.place(x=420,y=210,width=315,height=109)
   
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    