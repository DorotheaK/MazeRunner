#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 28, 2019 02:58:32 PM +0100  platform: Windows NT

import sys
import os
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import threading
import maze_control_support
import time
from maze_control_support import control

scriptDirectory = os.path.dirname(os.path.realpath(__file__))
projectDirectory = os.path.join(scriptDirectory,"..","..")

teamDirecory = os.path.join(projectDirectory,"Teams")

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    maze_control_support.set_Tk_var()
    top = Toplevel1 (root)
    maze_control_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    maze_control_support.set_Tk_var()
    top = Toplevel1 (w)
    maze_control_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    maze_control_support.control.running=0
    w.destroy()
    w = None
    


class Toplevel1:

    def callback(self,eventObject):
        self.selectedTeam=eventObject.widget.get()
        if maze_control_support.control.solver_action_proc != 0:
            maze_control_support.control.solver_action_proc.kill()
        print(self.selectedTeam)

    def callbackScaleDim(self,eventObject):
        self.EntryDim.delete(0,tk.END)
        self.EntryDim.insert(0,eventObject)

    def callbackScaleEntryDim(self,eventObject):
        if not eventObject.get()=="":
            self.ScaleDim.set(eventObject.get())

    def callbackScaleComplexity(self,eventObject):
        self.EntryComplexity.delete(0,tk.END)
        self.EntryComplexity.insert(0,eventObject)

    def callbackScaleEntryComplexity(self,eventObject):
        if not eventObject.get()=="":
            self.ScaleComplexity.set(eventObject.get())

    def callbackScaleDensity(self,eventObject):
        self.EntryDensity.delete(0,tk.END)
        self.EntryDensity.insert(0,eventObject)

    def callbackScaleEntryDensity(self,eventObject):
        if not eventObject.get()=="":
            self.ScaleDensity.set(eventObject.get())

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.running=1

        self.selectedTeam=""

        top.geometry("396x489+466+203")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.076, rely=0.266, relheight=0.153
                , relwidth=0.77)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")
        self.TFrame1.configure(width=305)

        self.value_list = next(os.walk(teamDirecory))[1]

        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(relx=0.525, rely=0.467, height=25, width=76)
        self.TButton1.configure(command=lambda: maze_control_support.load_team(self.selectedTeam))
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Load Team''')

        self.TCombobox1 = ttk.Combobox(self.TFrame1)
        self.TCombobox1.place(relx=0.033, rely=0.533, relheight=0.28
                , relwidth=0.469)
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=maze_control_support.combobox)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.bind("<<ComboboxSelected>>", self.callback)

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.0, rely=0.0, height=19, width=34)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Team''')

        self.TFrame2 = ttk.Frame(top)
        self.TFrame2.place(relx=0.076, rely=0.041, relheight=0.194
                , relwidth=0.77)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")
        self.TFrame2.configure(width=305)

        self.TButton2 = ttk.Button(self.TFrame2)
        self.TButton2.place(relx=0.066, rely=0.632, height=25, width=96)
        self.TButton2.configure(command=maze_control_support.mqtt_broker)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''MQTT Broker''')
        self.TButton2.configure(width=96)

        self.TButton3 = ttk.Button(self.TFrame2)
        self.TButton3.place(relx=0.066, rely=0.316, height=25, width=96)
        self.TButton3.configure(command=maze_control_support.maze_visualize)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Maze UI''')

        self.TLabel1 = ttk.Label(self.TFrame2)
        self.TLabel1.place(relx=0.0, rely=0.0, height=19, width=63)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Framework''')

        self.TFrame3 = ttk.Frame(top)
        self.TFrame3.place(relx=0.076, rely=0.45, relheight=0.358
                , relwidth=0.846)
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief="groove")
        self.TFrame3.configure(width=335)

        self.TLabel2 = ttk.Label(self.TFrame3)
        self.TLabel2.place(relx=0.0, rely=0.0, height=19, width=56)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Generator''')

        self.ScaleDim = tk.Scale(self.TFrame3, from_=0.0, to=63.0, command=self.callbackScaleDim)
        self.ScaleDim.place(relx=0.388, rely=0.057, relwidth=0.418, relheight=0.0
                , height=42, bordermode='ignore')
        self.ScaleDim.configure(activebackground="#ececec")
        self.ScaleDim.configure(background="#d9d9d9")
        self.ScaleDim.configure(font="TkTextFont")
        self.ScaleDim.configure(foreground="#000000")
        self.ScaleDim.configure(highlightbackground="#d9d9d9")
        self.ScaleDim.configure(highlightcolor="black")
        self.ScaleDim.configure(length="134")
        self.ScaleDim.configure(orient="horizontal")
        self.ScaleDim.configure(troughcolor="#d9d9d9")
        self.ScaleDim.set(11)

        self.ScaleComplexity = tk.Scale(self.TFrame3, from_=0.0, to=100.0,command=self.callbackScaleComplexity)
        self.ScaleComplexity.place(relx=0.388, rely=0.286, relwidth=0.4
                , relheight=0.0, height=42, bordermode='ignore')
        self.ScaleComplexity.configure(activebackground="#ececec")
        self.ScaleComplexity.configure(background="#d9d9d9")
        self.ScaleComplexity.configure(font="TkTextFont")
        self.ScaleComplexity.configure(foreground="#000000")
        self.ScaleComplexity.configure(highlightbackground="#d9d9d9")
        self.ScaleComplexity.configure(highlightcolor="black")
        self.ScaleComplexity.configure(length="128")
        self.ScaleComplexity.configure(orient="horizontal")
        self.ScaleComplexity.configure(troughcolor="#d9d9d9")
        self.ScaleComplexity.set(11)

        self.Label1 = tk.Label(self.TFrame3)
        self.Label1.place(relx=0.03, rely=0.371, height=21, width=66)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Complexity''')

        self.Label2 = tk.Label(self.TFrame3)
        self.Label2.place(relx=0.03, rely=0.571, height=21, width=45)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Density''')

        self.ScaleDensity = tk.Scale(self.TFrame3, from_=0.0, to=100.0,command=self.callbackScaleDensity)
        self.ScaleDensity.place(relx=0.388, rely=0.514, relwidth=0.4
                , relheight=0.0, height=42, bordermode='ignore')
        self.ScaleDensity.configure(activebackground="#ececec")
        self.ScaleDensity.configure(background="#d9d9d9")
        self.ScaleDensity.configure(font="TkTextFont")
        self.ScaleDensity.configure(foreground="#000000")
        self.ScaleDensity.configure(highlightbackground="#d9d9d9")
        self.ScaleDensity.configure(highlightcolor="black")
        self.ScaleDensity.configure(length="128")
        self.ScaleDensity.configure(orient="horizontal")
        self.ScaleDensity.configure(troughcolor="#d9d9d9")
        self.ScaleDensity.set(11)

        self.Label3 = tk.Label(self.TFrame3)
        self.Label3.place(relx=0.03, rely=0.143, height=21, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Dimension''')
        self.Label3.configure(width=76)

        self.ActionButtonGenerator = ttk.Button(self.TFrame3)
        self.ActionButtonGenerator.place(relx=0.806, rely=0.143, height=25
                , width=56)
        self.ActionButtonGenerator.configure(takefocus="")
        self.ActionButtonGenerator.configure(text='''action''')
        self.ActionButtonGenerator.configure(width=56)


        self.sv_dim = tk.StringVar(value='11')
        self.sv_dim.trace("w", lambda name, index, mode, sv=self.sv_dim: self.callbackScaleEntryDim(self.sv_dim))

        self.EntryDim = tk.Entry(self.TFrame3,textvariable=self.sv_dim)
        self.EntryDim.place(relx=0.269, rely=0.171,height=20, relwidth=0.101)
        self.EntryDim.configure(background="white")
        self.EntryDim.configure(disabledforeground="#a3a3a3")
        self.EntryDim.configure(font="TkFixedFont")
        self.EntryDim.configure(foreground="#000000")
        self.EntryDim.configure(highlightbackground="#d9d9d9")
        self.EntryDim.configure(highlightcolor="black")
        self.EntryDim.configure(insertbackground="black")
        self.EntryDim.configure(selectbackground="#c4c4c4")
        self.EntryDim.configure(selectforeground="black")

        self.sv_complexity = tk.StringVar(value='11')
        self.sv_complexity.trace("w", lambda name, index, mode, sv=self.sv_complexity: self.callbackScaleEntryComplexity(self.sv_complexity))

        self.EntryComplexity = tk.Entry(self.TFrame3,textvariable=self.sv_complexity)
        self.EntryComplexity.place(relx=0.269, rely=0.4, height=20
                , relwidth=0.101)
        self.EntryComplexity.configure(background="white")
        self.EntryComplexity.configure(disabledforeground="#a3a3a3")
        self.EntryComplexity.configure(font="TkFixedFont")
        self.EntryComplexity.configure(foreground="#000000")
        self.EntryComplexity.configure(insertbackground="black")
        self.EntryComplexity.configure(width=34)


        self.sv_density = tk.StringVar(value='11')
        self.sv_density.trace("w", lambda name, index, mode, sv=self.sv_density: self.callbackScaleEntryDensity(self.sv_density))
        self.EntryDensity = tk.Entry(self.TFrame3,textvariable=self.sv_density)
        self.EntryDensity.place(relx=0.269, rely=0.629, height=20
                , relwidth=0.101)
        self.EntryDensity.configure(background="white")
        self.EntryDensity.configure(disabledforeground="#a3a3a3")
        self.EntryDensity.configure(font="TkFixedFont")
        self.EntryDensity.configure(foreground="#000000")
        self.EntryDensity.configure(insertbackground="black")
        self.EntryDensity.configure(width=34)


        self.ActionButtonGenerator.configure(command=lambda: maze_control_support.generator_action(self.EntryDim.get(),self.EntryDim.get(),self.EntryComplexity.get(),self.EntryDensity.get()))

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="NewCommand")

        self.TFrame4 = ttk.Frame(top)
        self.TFrame4.place(relx=0.076, rely=0.791, relheight=0.140
                , relwidth=0.846)
        self.TFrame4.configure(relief='groove')
        self.TFrame4.configure(borderwidth="2")
        self.TFrame4.configure(relief="groove")
        self.TFrame4.configure(width=335)

        self.TButton4 = ttk.Button(self.TFrame4)
        self.TButton4.place(relx=0.066, rely=0.462, height=25, width=96)
        self.TButton4.configure(command=maze_control_support.maze_solver_loader)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Start Solver''')

        self.Label4 = tk.Label(self.TFrame4)
        self.Label4.place(relx=0.0, rely=0.0, height=21, width=34)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Solver''')

        self.TButton5 = ttk.Button(self.TFrame4)
        self.TButton5.place(relx=0.746, rely=0.462, height=25, width=76)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Solve Maze''')
        self.TButton5.configure(command=maze_control_support.maze_solver_action)     
        threading.Thread(target=self.monitor).start()           

    def monitor(self):
        while self.running:

            if maze_control_support.control.mqtt_broker_state==1:
                self.TButton2.config(state='disabled')
            else:
                self.TButton2.config(state='normal')

            if maze_control_support.control.maze_gui_state==1:
                self.TButton3.config(state='disabled')
            else:
                self.TButton3.config(state='normal')

            if maze_control_support.control.solver_action_state==1:
                self.TButton4.config(state='disabled')
            else:
                self.TButton4.config(state='normal')

            #print("Monitor: {} {} {}".format(maze_control_support.control.mqtt_broker_state, maze_control_support.control.maze_gui_state, maze_control_support.control.solver_action_state))
            time.sleep(1)


if __name__ == '__main__':
    vp_start_gui()





