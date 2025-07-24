# cpp game
用arch linux in wsl2开发一个cpp的游戏项目
## get started

!!! tip "available options"
    在 Windows 上使用 WSL2 + Arch Linux 来开发一个 C++ 游戏项目时，要实现图形化界面支持，你可以结合以下技术来实现开发环境、图形显示和调试体验：

    ---

    ## 🎮 1. 图形界面支持方式

    ### ✅ 方案一：使用 Windows 上的图形服务（推荐）

    **使用 Windows 的 X Server + WSLg**
    WSL2 从 Windows 11 开始自带 **WSLg（Windows Subsystem for Linux GUI）**，它支持在 Linux 子系统中直接运行 GUI 程序（包括基于 X11 和 Wayland 的程序）。

    * **适合人群**：使用 Windows 11 的开发者（最推荐）
    * **优点**：

    * 零配置 GUI 支持
    * 可以运行 Linux 下的 GUI 工具（如 VS Code、SDL/OpenGL 窗口）
    * **兼容性**：WSLg 兼容 SDL2、OpenGL、Vulkan 等图形库

    🛠 **使用方法**：

    * 确保你的 WSL2 版本为 Windows 11 的 WSLg 支持版本
    * 在 Arch 中安装游戏相关库：

    ```bash
    sudo pacman -S sdl2 sdl2_image glew glfw mesa vulkan-icd-loader
    ```
    * 编译并运行 SDL/OpenGL 程序，窗口会自动弹出（由 Windows 的 WSLg 显示）

    ---

    ### ✅ 方案二：使用 Windows 的 X Server（例如 VcXsrv、X410）

    如果你使用 Windows 10 或禁用了 WSLg，可以使用 X Server：

    * **安装 X Server（Windows）**：

    * [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
    * [X410](https://x410.dev/)
    * 启动 X Server 后，在 Arch 中设置环境变量：

    ```bash
    export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
    export LIBGL_ALWAYS_INDIRECT=1
    ```
    * 之后运行图形程序（如 SDL/OpenGL），会通过 X Server 在 Windows 上显示

    ---

    ## 🔧 2. 游戏开发相关工具链建议

    | 类型   | 工具/库                          | 安装命令                                                |
    | ---- | ----------------------------- | --------------------------------------------------- |
    | 编译器  | `gcc` / `clang`               | `sudo pacman -S gcc clang`                          |
    | 构建系统 | `cmake` / `meson`             | `sudo pacman -S cmake meson ninja`                  |
    | 图形库  | `SDL2`, `OpenGL`, `Vulkan`    | `sudo pacman -S sdl2 glew glfw mesa vulkan-headers` |
    | 编辑器  | `neovim` / `vscode` / `CLion` | VSCode可用Windows端，连接WSL调试                            |

    ---

    ## 🕹 示例：编译一个简单的 SDL2 程序

    1. 安装 SDL2：

    ```bash
    sudo pacman -S sdl2
    ```

    2. 编写 `main.cpp`：

    ```cpp
    #include <SDL2/SDL.h>
    int main() {
        SDL_Init(SDL_INIT_VIDEO);
        SDL_Window* window = SDL_CreateWindow("Hello SDL2", 100, 100, 800, 600, SDL_WINDOW_SHOWN);
        SDL_Delay(3000);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 0;
    }
    ```

    3. 编译并运行：

    ```bash
    g++ main.cpp -o sdl_app `sdl2-config --cflags --libs`
    ./sdl_app
    ```

    如果你用的是 WSLg 或配置好了 X Server，窗口就能正常显示。

    ---

    ## 💡 如果你用 Vulkan 或 OpenGL：

    * WSLg 支持 **OpenGL + Vulkan 显示加速**
    * 可结合 `vulkan-tools` 测试：

    ```bash
    sudo pacman -S vulkan-tools
    vulkaninfo | less
    ```

    ---

    ## 🚀 推荐开发流程（Windows + WSL2）：

    1. 用 VS Code 的 **WSL Remote 插件** 开发代码
    2. 在 Arch 下使用 `cmake` 构建
    3. 用 SDL/OpenGL 编写游戏逻辑
    4. 用 WSLg 或 X Server 显示图形界面
    5. （可选）使用 git + GitHub/GitLab 做版本管理

    ---

    如果你告诉我你具体的图形技术栈（SDL/OpenGL/Vulkan/ImGui 等），我还可以给你定制化开发配置建议。需要我帮你搭一个开发框架吗？
