#include <iostream>
#include <memory>
#include <unistd.h>
#include <X11/Xlib.h>
#include <X11/X.h>
#include <X11/Xutil.h>

XKeyEvent create_key_event(Display *display, Window &win,
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
  /* event.keycode = 0xff1b; */
  event.keycode = XKeysymToKeycode(display, keycode);
  event.state = modifiers;
  event.type = KeyPress;

  return event;
}

int main(int argc, char** argv) {
  Display *dpy = XOpenDisplay(0);
  Screen* s = DefaultScreenOfDisplay(dpy);
  Window root_window;

  auto height = s->height;
  auto width = s->width;

  auto center_x = height / 2;
  auto center_y = height /2;

  root_window = XRootWindow(dpy, 0);
  XSelectInput(dpy, root_window, KeyReleaseMask);

  XWarpPointer(dpy, None, root_window, 0, 0, 0, 0, center_x, center_y);
  usleep(100000);

  for (int i = 0; i < 50; ++i) {
    Window focus_window;

    XKeyEvent event = create_key_event(dpy, focus_window, root_window, true, 0xff0d, 0);
    XSendEvent(event.display, event.window, True, KeyPressMask, (XEvent *)&event);
    std::cout << "Key pressed" << std::endl;

    usleep(100000);

    event = create_key_event(dpy, focus_window, root_window, false, 0xff0d, 0);
    XSendEvent(event.display, event.window, True, KeyPressMask, (XEvent *)&event);
    std::cout << "Key unpressed" << std::endl;
  }

  XFlush(dpy);

  return 0;
}
