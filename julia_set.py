import time
import numpy as np
from functools import wraps
import matplotlib.pyplot as plt
import line_profiler

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

# area of complex space to investigate
x1,x2,y1,y2 = -2, 2, -2, 2
c_real, c_imag = -0.62772, -0.42193


def calculate_z_serial_purepython(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z = z*z + c
            n += 1
        output[i] = n
    return output

def calc_pure_python(desired_width, max_iterations):

    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    secs = time.time() - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
    return output

if __name__ == "__main__":
    output = calc_pure_python(desired_width=5000, max_iterations=300)
    re_shaped_output = np.reshape(output, (5001, 5001))
    plt.imshow(re_shaped_output, cmap='hot', interpolation='nearest')
    plt.show()
    