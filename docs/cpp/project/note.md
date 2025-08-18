# cpp开发经验

## 关于跨文件
![1755268419003](image/note/1755268419003.png)


如果宏定义在头文件里，并且这个头文件被 #include 到多个 .cpp 里，那么在这些 .cpp 编译单元中宏也都有效（因为 #include 会把宏文本复制进去）。

📌 但是，不同 .cpp 文件之间的宏定义是互相独立的，编译器在编译单个文件时只知道这个文件里（以及它包含的头文件）有哪些宏。

## inline
与类成员无关的工具函数，建议独立定义，方便复用。h文件声明定义一起写
```cpp
// utils.h
#pragma once
#include <iostream>
#include <chrono>
#include <ctime>

inline void printCurrentTime() {
    auto now = std::chrono::system_clock::now();
    std::time_t t = std::chrono::system_clock::to_time_t(now);
    std::cout << std::ctime(&t);
}
```

1. 在一个工具头文件（如 utils.h）中定义:
2. 静态成员函数