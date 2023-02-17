cmake_minimum_required(VERSION 3.25)

project(unvm CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_EXPERIMENTAL_CXX_MODULE_DYNDEP 1)
set(CMAKE_EXPERIMENTAL_CXX_MODULE_CMAKE_API  "2182bf5c-ef0d-489a-91da-49dbc3090d2a")
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (MSVC)
    add_compile_options(/W4 /WX)
else()
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()

find_package(CURL REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)
find_package(libzip CONFIG REQUIRED)

add_executable(unvm
    src/main.cxx
)

target_link_libraries(unvm
    PRIVATE
    CURL::libcurl
    nlohmann_json::nlohmann_json
    libzip::zip
)