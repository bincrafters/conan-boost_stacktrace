project(test_package CXX)
cmake_minimum_required(VERSION 3.1.2)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(MPI)

file(GLOB SOURCE_FILES *.cpp)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} 
  CONAN_PKG::boost_array
  CONAN_PKG::boost_config
  CONAN_PKG::boost_container_hash
  CONAN_PKG::boost_core
  CONAN_PKG::boost_lexical_cast
  CONAN_PKG::boost_stacktrace
  CONAN_PKG::boost_static_assert
  CONAN_PKG::boost_type_traits
  CONAN_PKG::boost_winapi)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)

if(MPI_CXX_FOUND)
  target_link_libraries(${CMAKE_PROJECT_NAME} CONAN_PKG::openmpi)
endif(MPI_CXX_FOUND)
