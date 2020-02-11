from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 == x1 and y0 == y1: return
    if x0 > x1: return draw_line(x1, y1, x0, y0, screen, color)
    if x1 - x0 == 0:
        if y1 > y0:
            plot(screen, color, y0 + 1, y1)
            return draw_line(x0, y0 + 1, x1, y1, screen, color)
        else:
            plot(screen, color, y0 - 1, y1)
            return draw_line(x0, y0 - 1, x1, y1, screen, color)
    slope = (y1 - y0) / (x1 - x0)
    if slope > 1:
        plot(screen, color, x0, y0 + 1)
        return draw_line(x0, y0 + 1, x1, y1, screen, color)
    elif slope == 1:
        plot(screen, color, x0 + 1, y0 + 1)
        return draw_line(x0 + 1, y0 + 1, x1, y1, screen, color)
    elif slope > 0:
        plot(screen, color, x0 + 1, y0)
        return draw_line(x0 + 1, y0, x1, y1, screen, color)
    elif slope > -1:
        plot(screen, color, x0 + 1, y0)
        return draw_line(x0 + 1, y0, x1, y1, screen, color)
