import matplotlib.pyplot as plt
import numpy as np

def plot_sin_wave():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.show()

if __name__ == '__main__':
    plot_sin_wave()

