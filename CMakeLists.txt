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
  set(STEINWURF_TOP_NAME ${PROJECT_NAME})
endif()

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


  add_executable(np_gtest_tests ${gtest_test_sources})
  target_link_libraries(np_gtest_tests gtest_main)
  target_link_libraries(np_gtest_tests steinwurf::gtest)

  add_test(np_gtest_tests np_gtest_tests)

endif()


