#pragma once

#include <memory>

namespace mine {
  class IWindow {
    public:
      IWindow();
      ~IWindow();

      void init();
    private:
      int width;
      int height;
  };
} // namespace mine
