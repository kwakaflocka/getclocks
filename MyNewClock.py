from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

font1 = {'family':'serif','color':'blue','size':20}

def philly_clock(i):
    axc.cla()  # clearing current axis
    now = datetime.now()  # Get system time
    now_time = now.strftime("%H:%M:%S")
    h, m, s = [int(i) for i in now_time.split(':')]
    h = h - 12 if h > 12 else h
    ''' Calculations related to the angle of the hands '''
    s_ = np.multiply(np.ones(5), s * 2 * np.pi / 60)
    m_ = np.multiply(np.ones(5), m * 2 * np.pi / 60) + (s_ / 60)  # Add a second element for a detailed view
    h_ = np.multiply(np.ones(5), h * 2 * np.pi / 12) + (m_ / 12)  # Add a second element for a detailed view
    axc.axis('off')
    axc.set_theta_zero_location('N')  # Start from 12 o'clock
    axc.set_theta_direction(-1)
    ''' Hands '''
    axc.plot(h_, np.linspace(0.00, 0.70, 5), c='c', linewidth=2.0)
    axc.plot(m_, np.linspace(0.00, 0.85, 5), c='b', linewidth=1.5)
    axc.plot(s_, np.linspace(0.00, 1.00, 5), c='r', linewidth=1.0)
    ''' phosphorus '''
    axc.plot(m_, np.linspace(0.73, 0.83, 5), c='w', linewidth=1.0)
    axc.plot(h_, np.linspace(0.60, 0.68, 5), c='w', linewidth=1.5)
    axc.plot(s_, np.linspace(0.80, 0.98, 5), c='w', linewidth=0.5)
    # axc.scatter(0, 0, c='k', linewidths=5, alpha=1, s=10)
    axc.set_rmax(1.06)  # A little trick
    plt.xlabel("Philadelphia", fontdict = font1)
    fig=plt.savefig("Philly_clock.png")

    plt.show()

    animation.event_source.stop()


def japan_clock(i):
    axc.cla()  # clearing current axis
    now = datetime.now()  # Get system time
    japan_now = datetime.now() + timedelta(hours=13)
    now_time = japan_now.strftime("%H:%M:%S")
    h, m, s = [int(i) for i in now_time.split(':')]
    h = h - 12 if h > 12 else h
    ''' Calculations related to the angle of the hands '''
    s_ = np.multiply(np.ones(5), s * 2 * np.pi / 60)
    m_ = np.multiply(np.ones(5), m * 2 * np.pi / 60) + (s_ / 60)  # Add a second element for a detailed view
    h_ = np.multiply(np.ones(5), h * 2 * np.pi / 12) + (m_ / 12)  # Add a second element for a detailed view
    axc.axis('off')
    axc.set_theta_zero_location('N')  # Start from 12 o'clock
    axc.set_theta_direction(-1)
    ''' Hands '''
    axc.plot(h_, np.linspace(0.00, 0.70, 5), c='c', linewidth=2.0)
    axc.plot(m_, np.linspace(0.00, 0.85, 5), c='b', linewidth=1.5)
    axc.plot(s_, np.linspace(0.00, 1.00, 5), c='r', linewidth=1.0)
    ''' phosphorus '''
    axc.plot(m_, np.linspace(0.73, 0.83, 5), c='w', linewidth=1.0)
    axc.plot(h_, np.linspace(0.60, 0.68, 5), c='w', linewidth=1.5)
    axc.plot(s_, np.linspace(0.80, 0.98, 5), c='w', linewidth=0.5)
    # axc.scatter(0, 0, c='k', linewidths=5, alpha=1, s=10)
    axc.set_rmax(1.06)  # A little trick

    plt.savefig("japan_clock.png")
    plt.show()
    animation.event_source.stop()

def seattle_clock(i):
    axc.cla()  # clearing current axis
    now = datetime.now()  # Get system time
    seattle_now = datetime.now() + timedelta(hours=13)
    now_time = seattle_now.strftime("%H:%M:%S")
    h, m, s = [int(i) for i in now_time.split(':')]
    h = h - 12 if h > 12 else h
    ''' Calculations related to the angle of the hands '''
    s_ = np.multiply(np.ones(5), s * 2 * np.pi / 60)
    m_ = np.multiply(np.ones(5), m * 2 * np.pi / 60) + (s_ / 60)  # Add a second element for a detailed view
    h_ = np.multiply(np.ones(5), h * 2 * np.pi / 12) + (m_ / 12)  # Add a second element for a detailed view
    axc.axis('off')
    axc.set_theta_zero_location('N')  # Start from 12 o'clock
    axc.set_theta_direction(-1)
    ''' Hands '''
    axc.plot(h_, np.linspace(0.00, 0.70, 5), c='c', linewidth=2.0)
    axc.plot(m_, np.linspace(0.00, 0.85, 5), c='b', linewidth=1.5)
    axc.plot(s_, np.linspace(0.00, 1.00, 5), c='r', linewidth=1.0)
    ''' phosphorus '''
    axc.plot(m_, np.linspace(0.73, 0.83, 5), c='w', linewidth=1.0)
    axc.plot(h_, np.linspace(0.60, 0.68, 5), c='w', linewidth=1.5)
    axc.plot(s_, np.linspace(0.80, 0.98, 5), c='w', linewidth=0.5)
    # axc.scatter(0, 0, c='k', linewidths=5, alpha=1, s=10)
    axc.set_rmax(1.06)  # A little trick
    plt.xlabel("Seattle")
    plt.savefig("seattle_clock.png")
    plt.show()
    animation.event_source.stop()


''' Prepare the preparations and call the MyClock '''





