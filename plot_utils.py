import matplotlib.pyplot as plt

def plot_function(x_values, y_values, title='Function Plot'):
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

