import numpy as np

def cubic_spline_interpolation(x, y, left_derivative, right_derivative):
    n = len(x)
    h = np.diff(x)
    delta = np.diff(y) / h
    l = np.zeros(n)
    u = np.zeros(n)
    z = np.zeros(n)
    c = np.zeros(n+1)
    b = np.zeros(n)
    d = np.zeros(n)
    
    l[0] = 1
    u[0] = 0
    z[0] = 0
    
    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * u[i-1]
        u[i] = h[i] / l[i]
        z[i] = (delta[i] - h[i-1] * z[i-1]) / l[i]
    
    l[n-1] = 1
    z[n-1] = 0
    c[n] = 0
    
    for j in range(n-2, -1, -1):
        c[j] = z[j] - u[j] * c[j+1]
        b[j] = delta[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    
    return b, c[:-1], d

def evaluate_cubic_spline(x, y, b, c, d, xi):
    n = len(x)
    for i in range(n-1):
        if x[i] <= xi <= x[i+1]:
            dx = xi - x[i]
            return y[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3

x = np.array([1, 2, 4])
y = np.array([-1, 1, -2])
left_derivative = 1
right_derivative = -1

b, c, d = cubic_spline_interpolation(x, y, left_derivative, right_derivative)

xi = 3
yi = evaluate_cubic_spline(x, y, b, c, d, xi)

print("Interpolated value at xi:", yi)