
# Welcome to dingzhens home!!!

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

- my web temporary location: [http://127.0.0.1:8000](http://127.0.0.1:8000)

:smile:



??? success

    for all the detailed information just refer to link:
    [https://jameswillett.dev/getting-started-with-material-for-mkdocs/](https://jameswillett.dev/getting-started-with-material-for-mkdocs/)

    and the author youtube: [https://www.youtube.com/watch?v=xlABhbnNrfI](https://www.youtube.com/watch?v=xlABhbnNrfI)




=== "website"

    [https://jameswillett.dev/getting-started-with-material-for-mkdocs/](https://jameswillett.dev/getting-started-with-material-for-mkdocs/)


=== "youtube"
    [https://www.youtube.com/watch?v=xlABhbnNrfI](https://www.youtube.com/watch?v=xlABhbnNrfI)
    



## Commands
tip: defalt file path : **C:\Windows\System32\dingzhensite** 

但是由于原路径`System32` 似乎操作起来都需要以管理员方式运行，乱改访问权限以我现有的知识水平有可能会出问题，遂在新路径下复刻了原先的操作
**C:\Users\78100\fortesting** 这样粘贴图片等操作就方便多了哈哈哈:smile::smile::smile:

:fontawesome-regular-face-laugh-wink:

* `mkdocs new [dir-name]` - Create a new project.(only necessary when first operation)
* `cd dingzhensite` - change to the project directory:  **C:\Windows\System32\dingzhensite**.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.




## for mkdocs testing

```py title="add_numbers.py" linenums="1"
# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Example usage
result = add_two_numbers(5, 3)
print('The sum is:', result)
```

```cpp title="example.cpp" linenums="1" hl_lines="2-4"
#include <iostream>
using namespace std;
//others 
int main() {
    return 0;
}
```


## Content Tabs

This is some examples of content tabs.

### Generic Content

=== "Plain text"

    This is some plain text

=== "Unordered list"

    * First item
    * Second item
    * Third item

=== "Ordered list"

    1. First item
    2. Second item
    3. Third item


Here is an example with different code blocks:

### Code Blocks in Content Tabs

=== "Python"

    ```py
    def main():
        print("Hello world!")

    if __name__ == "__main__":
        main()
    ```

=== "JavaScript"

    ```js
    function main() {
        console.log("Hello world!");
    }

    main();
    ```


This is an example of an adominition with a title:

!!! note "Title of the callout"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


Collapsible callout:

??? info "Collapsible callout"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
