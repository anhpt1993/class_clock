from Class_Clock import Clock
import turtle as t

clock = Clock(10, 20, 30, 300)
clock.draw_clock(t)
t.Screen().update()
#clock.draw_hands(t)
pen = t.Turtle()
clock.draw_motion_clock(pen)

t.done()