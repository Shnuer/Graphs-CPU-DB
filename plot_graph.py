import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import cpu_read

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys1 = []
ys2 = []




def animate(i, xs, ys1, ys2):

    new_value = cpu_read.get_percentage_CPU()
    
    first_core = round(new_value[0], 2)
    second_core = round(new_value[1], 2)
    

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys1.append(first_core)
    ys2.append(second_core)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys1 = ys1[-20:]
    ys2 = ys2[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys1)
    ax.plot(xs, ys2)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('CPU utilization')
    plt.ylabel('Percentage (deg %)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys1, ys2), interval=1000)
while 1:
    print('Im here')
    plt.show()
