project(core)
file(GLOB SOURCES "src/*.cc")

add_library(core SHARED ${SOURCES})

target_include_directories(${PROJECT_NAME}
  PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

install(DIRECTORY include/ DESTINATION "${INSTALL_INCLUDE_DIR}")
