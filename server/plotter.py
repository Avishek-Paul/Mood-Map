import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
happy_ax = fig.add_subplot(2,2,1)
sad_ax = fig.add_subplot(2,2,2)
angry_ax = fig.add_subplot(2,2,3)
fear_ax = fig.add_subplot(2,2,4)

x_vals = list()
happy_vals = list()
sad_vals = list()
angry_vals = list()
fear_vals = list()

def animate(i):
    try:
        raw_data = open('server/data/total_values.csv').read()
        data = raw_data.split('\n')[1:]
    
        happy_datum = int(data[0].split(',')[0])/1000
        sad_datum = int(data[1].split(',')[0])/1000
        angry_datum = int(data[2].split(',')[0])/1000
        fear_datum = int(data[3].split(',')[0])/1000

        if len(x_vals)>=100:
            x_vals.pop(0)
            happy_vals.pop(0)
            sad_vals.pop(0)
            angry_vals.pop(0)
            fear_vals.pop(0)

        x_vals.append(time.time())
        happy_vals.append(happy_datum)
        sad_vals.append(sad_datum)
        angry_vals.append(angry_datum)
        fear_vals.append(fear_datum)
        
    except Exception:
        pass

    happy_ax.clear()
    happy_ax.plot(x_vals, happy_vals)
    sad_ax.clear()
    sad_ax.plot(x_vals, sad_vals)
    angry_ax.clear()
    angry_ax.plot(x_vals, angry_vals)
    fear_ax.clear()
    fear_ax.plot(x_vals, fear_vals)

    #plt.savefig('server/data/graph.png')

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=25)
    plt.savefig('server/data/graph.png')
    plt.show()
