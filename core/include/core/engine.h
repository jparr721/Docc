#pragma once

namespace mine {
  class Engine {
    public:
      explicit Engine(int agents) : agents_(agents) {};
      void init();

    private:
      int agents_;
  };
} // namespace mine
