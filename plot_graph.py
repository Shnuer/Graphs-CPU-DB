import datetime as dt
from pyqtgraph import QtGui, QtCore
import numpy as np 
import pyqtgraph as pg 

import cpu_read
import mysql_for_graph
# Create figure for plotting


# Create list for time line and list with core threads
time_line = []
list_core = [[] for num_core in cpu_read.get_percentage_CPU()]
list_legend = []
# Set up plot to call animate() function periodically




app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="basic plotting")
win.resize(1200, 600)
win.setWindowTitle('Ploting CPU percent')

p = win.addPlot(title = 'Bassic')
p.setWindowTitle('Percent CPU threads')

p.setLabel('bottom', 'Index', units = 'B' )

curves = []

im_legend = pg.LegendItem()




for i in range(len(list_core)):
    c = pg.PlotCurveItem(pen=(i, len(list_core)*1.3))
    num_threads = i + 1
    new_name = 'Num core: %d' % num_threads
    im_legend.addItem(item = c, name = new_name)
    p.addItem(c)

    
    
    
    # c.setPos(0, i*6)
    curves.append(c)

p.resize(1000,500)

win.addItem(im_legend)


ptr = 0

p.enableAutoRange('xy', True)

def update():
    global curve, ptr, p, time_line, list_with_value_core
    
    # time_line.append(dt.datetime.now().strftime('%H:%M:%S'))
    time_line.append(ptr)
    ptr += 1
    time_line = time_line[-20:]

    current_value_cpu = cpu_read.get_percentage_CPU()
    mysql_for_graph.updateTable(current_value_cpu)
    # Add new value core threads to list value_core
    for list_with_value_core, new_value_core in zip(list_core, current_value_cpu):
        list_with_value_core.append(new_value_core)
        
    
        
    # print(list_with_value_core)
    # Limit list with core
    for index_core in range(len(list_core)):
        list_core[index_core] = list_core[index_core][-20:]
        curves[index_core].setData(time_line, list_core[index_core])
    

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    mysql_for_graph.createTable()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
    mysql_for_graph.deleteTable()