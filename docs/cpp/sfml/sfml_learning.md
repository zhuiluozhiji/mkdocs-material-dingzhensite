# sfml learning
https://www.sfml-dev.org/tutorials/2.6/

直接使用 g++ 编译时没有链接SFML库，所以应该要
```shell
g++ main.cpp -o a -lsfml-graphics -lsfml-window -lsfml-system
```

替代方案：使用CMake构建
```shell
cmake_minimum_required(VERSION 3.28)
project(CMakeSFMLProject LANGUAGES CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

include(FetchContent)
FetchContent_Declare(SFML
    GIT_REPOSITORY https://github.com/SFML/SFML.git
    GIT_TAG 2.6.1
    GIT_SHALLOW ON
    EXCLUDE_FROM_ALL
    SYSTEM)
FetchContent_MakeAvailable(SFML)

add_executable(main src/main.cpp)
target_compile_features(main PRIVATE cxx_std_17)
target_link_libraries(main PRIVATE SFML::Graphics)

```

CMakeLists.txt 文件当前使用了 FetchContent 来下载 SFML 源码。如果网络延迟较高导致卡住，可以改为直接使用系统安装的 SFML（通过 apt 安装的 2.6.1 版本）。以下是修改后的 CMakeLists.txt 文件：

```shell
cmake_minimum_required(VERSION 3.28)
project(CMakeSFMLProject LANGUAGES CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# 使用系统安装的 SFML
find_package(SFML 2.6 REQUIRED COMPONENTS graphics window system)

add_executable(main src/main.cpp)
target_compile_features(main PRIVATE cxx_std_17)

# 链接到系统安装的 SFML 库
target_link_libraries(main PRIVATE sfml-graphics sfml-window sfml-system)
```



```shell
# 进入build目录
cd ~/newfolder/build

# 编译项目
make

# 运行程序
./MySFMLGame
```