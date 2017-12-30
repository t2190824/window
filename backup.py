import sys,os
import curses
from random import randrange
cs = [curses.COLOR_BLACK,curses.COLOR_BLUE,curses.COLOR_CYAN,curses.COLOR_GREEN,curses.COLOR_MAGENTA,curses.COLOR_RED,curses.COLOR_WHITE,curses.COLOR_YELLOW]
def d_m(x):
  k = 0
  x.clear()
  x.refresh()
  curses.halfdelay(4)
  curses.start_color()
  p_i = 4
  pair_start = p_i
  n_c = 0
  for i in xrange(0, len(cs)):
    for j in xrange(0, len(cs)):
      if i == j:
        continue
      curses.init_pair(p_i, cs[i], cs[j])
      p_i += 1
      n_c += 1
  color_pairs = [4, 5, 6]
  colors_index = 0
  def r_c():
    return curses.color_pair(randrange(pair_start, n_c))
  while True:
    if k == ord('q'):
      break
    x.clear()
    h, w = x.getmaxyx()
    t = " im gay "[:w-1]
    x.attron(curses.A_BOLD)
    x.attron(curses.A_STANDOUT)
    for i in xrange(0, h):
      t_c = 0
      while t_c < w - len(t):
        x.addstr(i, t_c, t, r_c())
        t_c += len(t)
    x.refresh()
    k = x.getch()
curses.wrapper(d_m)