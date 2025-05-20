cmake_minimum_required(VERSION 3.12)
project(gtest)

find_package(Python COMPONENTS Interpreter)

# Use waf to resolve dependencies
if(NOT DEFINED STEINWURF_RESOLVE)
  message(STATUS "Resolving dependencies...")
  execute_process(
    COMMAND ${Python_EXECUTABLE} waf resolve ${STEINWURF_RESOLVE_OPTIONS}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE STATUS)
  if(STATUS AND NOT STATUS EQUAL 0)
    message(FATAL_ERROR "Failed: ${STATUS}")
  endif()
  set(STEINWURF_RESOLVE "${CMAKE_CURRENT_SOURCE_DIR}/resolve_symlinks")
endif()

# Set code position independent
if(CMAKE_SYSTEM_NAME MATCHES "Linux|Android|iOS|Darwin")
  set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

# On mac use -stdlib=libc++
if(CMAKE_SYSTEM_NAME MATCHES "Darwin")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
endif()

# Include common CMake settings
include("${STEINWURF_RESOLVE}/toolchains/common_settings.cmake")

if(CMAKE_C_COMPILER_ID MATCHES "MSVC")
  # For Windows: Prevent overriding the parent project's compiler/linker
  # settings
  set(gtest_force_shared_crt
      ON
      CACHE BOOL "" FORCE)
endif()

add_subdirectory("${STEINWURF_RESOLVE}/gtest-source" gtest EXCLUDE_FROM_ALL)

add_library(steinwurf::gtest ALIAS gtest)
add_library(steinwurf::gmock ALIAS gmock)

if(${PROJECT_NAME} STREQUAL ${CMAKE_PROJECT_NAME})


  # Build test executable
  file(GLOB_RECURSE gtest_test_sources ./test/*.cpp)

  add_executable(sw_gtest_tests ${gtest_test_sources})
  target_link_libraries(sw_gtest_tests steinwurf::gtest)

  enable_testing()
  add_test(sw_gtest_tests sw_gtest_tests)

endif()


