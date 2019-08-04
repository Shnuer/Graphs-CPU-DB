import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import cpu_read

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Create list for time line and list with core threads
time_line = []
list_core = [[] for num_core in cpu_read.get_percentage_CPU()]

def animate(i, time_line, list_core):

    # Add time to list time_line
    time_line.append(dt.datetime.now().strftime('%H:%M:%S'))
    time_line = time_line[-20:]
    
    # Add new value core threads to list value_core
    for value_core, new_value_core in zip(list_core, cpu_read.get_percentage_CPU()):
        value_core.append(new_value_core)
    
    # Limit list with core
    for index_core in range(len(list_core)):
        list_core[index_core] = list_core[index_core][-20:]


    # Plot graph
    ax.clear()
    for value_core in list_core:
        ax.plot(time_line, value_core)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('CPU utilization')
    plt.ylabel('Percentage (deg %)')

# Set up plot to call animate() function periodically

ani = animation.FuncAnimation(fig, animate, fargs=(time_line, list_core), interval=1000)


plt.show()
