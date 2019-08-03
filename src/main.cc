#include <iostream>
#include <memory>
#include <X11/Xlib.h>
#include <X11/X.h>
#include <X11/Xutil.h>

XKeyEvent createKeyEvent(Display *display, Window &win,
                         Window &root, bool press,
                         int keycode, int modifiers) {
  XKeyEvent event;
  event.display = display;
  event.window = win;
  event.root = root;
  event.subwindow = None;
  event.time = CurrentTime;
  event.x = 1;
  event.y = 1;
  event.x_root = 1;
  event.y_root = 1;
  event.same_screen = True;
  event.keycode = 0xff1b;
  event.state = modifiers;
  event.type = KeyPress;

  return event;
}

int main(int argc, char** argv) {
  Display *dpy = XOpenDisplay(0);
  Screen* s = DefaultScreenOfDisplay(dpy);
  XKeyEvent xke;
  xke.display = dpy;
  xke.keycode = 0xff1b;
  Window root_window;

  auto height = s->height;
  auto width = s->width;
  std::cout << height << std::endl;
  std::cout << width << std::endl;
  auto center_x = height / 2;
  auto center_y = height /2;

  root_window = XRootWindow(dpy, 0);
  XSelectInput(dpy, root_window, KeyReleaseMask);

  XWarpPointer(dpy, None, root_window, 0, 0, 0, 0, center_x, center_y);

  XFlush(dpy);

  return 0;
}
