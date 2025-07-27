

## hash

`unordered_set` 和 `unordered_map` 是 C++ 标准库中的关联容器，它们与 `set` 和 `map` 类似，但与 `set` 和 `map` 不同的是，它们并不保持元素的顺序，而是基于哈希表实现的，因此它们的查找、插入和删除操作的平均时间复杂度为 O(1)，相比于 `set` 和 `map`（基于红黑树，时间复杂度为 O(log n)），性能在某些场景下可能更好。

### 1. **`unordered_set`**:

`unordered_set` 是一个不允许重复元素的集合，它通过哈希表来存储元素，因此元素的顺序是不可预测的。

- **示例代码：**

```cpp
#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    unordered_set<int> uset;  // 创建一个unordered_set容器

    // 插入元素
    uset.insert(10);
    uset.insert(20);
    uset.insert(30);
    uset.insert(20);  // 20会被忽略，因为unordered_set不允许重复元素

    // 查找元素
    if (uset.find(10) != uset.end()) {
        cout << "10 found in the unordered_set." << endl;
    }

    // 输出容器中的所有元素
    cout << "Elements in the unordered_set: ";
    for (const int& val : uset) {
        cout << val << " ";
    }
    cout << endl;

    // 删除元素
    uset.erase(20);

    cout << "After erasing 20, elements in the unordered_set: ";
    for (const int& val : uset) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
```

- **主要操作：**

- `insert(value)`：插入一个元素，若元素已存在，则插入失败。
- `find(value)`：查找某个元素，返回一个迭代器指向该元素（如果找到）或 `end()`。
- `erase(value)`：删除指定的元素。
- `size()`：返回容器中元素的个数。
- `empty()`：检查容器是否为空。

### 2. **`unordered_map`**:

`unordered_map` 是一个基于哈希表实现的关联容器，它存储键值对，每个键只能有一个对应的值。与 `unordered_set` 不同的是，`unordered_map` 允许根据键值查找、插入和删除。

1. **用法：**

- 它提供了通过键访问值的能力，键是唯一的，值可以重复。
- 键是哈希表中的哈希值，用于在 **常数时间** 内查找对应的值。

2. **示例代码：**

```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, string> umap;

    // 插入键值对
    umap[1] = "apple";
    umap[2] = "banana";
    umap[3] = "cherry";

    // 查找键是否存在
    if (umap.find(2) != umap.end()) {
        cout << "Key 2 found, value: " << umap[2] << endl;
    }

    // 输出unordered_map中的所有元素
    cout << "Elements in the unordered_map:" << endl;
    for (const auto& pair : umap) {
        cout << "Key: " << pair.first << ", Value: " << pair.second << endl;
    }

    // 删除元素
    umap.erase(2);  // 删除键为2的元素

    cout << "After erasing key 2, elements in the unordered_map:" << endl;
    for (const auto& pair : umap) {
        cout << "Key: " << pair.first << ", Value: " << pair.second << endl;
    }

    return 0;
}
```

3. **主要操作：**

- `insert({key, value})` 或 `operator[]`：插入一个键值对。如果键已存在，`operator[]` 会更新其对应的值。
- `find(key)`：查找键 `key` 对应的值。如果键存在，返回指向该元素的迭代器，否则返回 `end()`。
- `erase(key)`：删除指定键的元素。
- `size()`：返回容器中键值对的个数。
- `empty()`：检查容器是否为空。

4. **总结：**

- 两者都提供常数时间的查找、插入和删除操作，因此在需要快速查找的场景下非常有用。

---



**1. Hash 的插入可以有这样的操作**

```   
Unordered_map <string,int> result;
Result[“aa”] = 23;
```
> 作为对比：Vector 的插入不可以直接用数组的方式，必须使用 `emplace_back/push_back` 或者 `insert(“position”,things)`;



或者可以使用：

```cpp
unordered_map<int,int> m; //<string,string>,<char,char>,数据类型任意
m.insert(pair<int,int>(1, 10));
m.insert(pair<int,int>(2, 20));
```

**2. Hash 的遍历**

   - 第一种遍历：

    ``` cpp
    unordered_map<int,int> count;
    for(auto p : count){
        int front = p.first;//key
        int end = p.second;//value
    }
    ```
   - 第二种遍历：

```cpp

unordered_map<int,int> count;
for(auto iter = count.begin();iter!=count.end();iter++){
    int front = iter->first;//key
    int end = iter->second;//value
}
```
**<span style="color:red">关于iterator :</span>**


> eg1  : auto_iterator :
``` cpp
    vector<string> v6 = { "hi","my","name","is","lee" };
    //for (vector<string>::iterator iter = v6.begin(); iter != v6.end(); iter++)
    for (auto iter = v6.begin(); iter != v6.end(); iter++)
    {
        cout << *iter << " ";
        //下面两种方法都行
        cout << (*iter).empty() << " ";
        cout << iter->empty() << endl; 
    }
```
it turns out that : 
```
hi 0 0
my 0 0
name 0 0
is 0 0
lee 0 0
```

> eg2:  auto_iterator()
``` cpp    
    string s[7] = {"aa","bb","cc","dd","ee","ff","gg"};
    vector<string> words(s,s+7);
    cout << "not insert things yet!" << endl; 
    for(auto w:words){  //pay attention to this for_iteration
    	cout << w<<" " ;
	}
	words.insert(words.begin()+3,"-insertion-");  
	cout << endl << "after insert" << endl ; 
	for(auto w:words){
    	cout << w<<" " ;
	}
```
it turn out that:
```
not insert things yet!
aa bb cc dd ee ff gg
after insert
aa bb cc  -insertion-  dd ee ff gg

```

> eg3:  vec_iterator: `vector.front(),vector.back()` VS `vector.begin(),vector.end()`

``` cpp
 vector<char> v1;
 vector<char>::iterator iter1;
 vector<char>::iterator iter2;
 v1.push_back('m');
 v1.push_back('n');
 v1.push_back('o');
 v1.push_back('p');

 cout << "v1.front() = " << v1[0] << endl;
 cout << "v1.back() = " << v1.back() << endl;

 iter1 = v1.begin();
 cout << *iter1 << endl;
 cout <<*v1.begin()<<endl;
 iter2 = v1.end()-1;    //注意v1.end()指向的是最后一个元素的下一个位置，所以访问最后一个元素的正确操作为：v1.end() - 1;
 cout << *iter2 << endl;
 cout <<*(v1.end()-1)<<endl;
```
it turn out that:
```
v1.front() = m
v1.back() = p
m
m
p
p
```

> eg4 : 将 vector <string > copy 到 hashset 中

``` cpp
        unordered_set <string> word;
        for(auto p : wordDict){
            word.insert(p);
        } 
```


**3. 相关教学：**

[unordered_set](https://blog.csdn.net/qq_60831089/article/details/131465770?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522172388209316800180681968%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=172388209316800180681968&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-131465770-null-null.142%5ev100%5epc_search_result_base2&utm_term=%E5%93%88%E5%B8%8C%E8%A1%A8c%2B%2B%20set&spm=1018.2226.3001.4187)

[unordered_map](https://blog.csdn.net/m0_51233386/article/details/126000760?spm=1001.2014.3001.5506)





??? note
    useful

```cpp
unordered_map<int, string> phoneMap;

// 插入一些键值对
phoneMap[1] = "One";
phoneMap[2] = "Two";
phoneMap[3] = "Three";

// 使用 at() 访问值
try {
string letters = phoneMap.at(2);  // 查找键为 2 的值
cout << "The value for key 2 is: " << letters << endl;
} catch (const out_of_range& e) {
cout << "Key not found!" << endl;
}

// 如果键不存在，使用 at() 会抛出异常
try {
string letters = phoneMap.at(4);  // 查找键为 4 的值
cout << "The value for key 4 is: " << letters << endl;
} catch (const out_of_range& e) {
cout << "Key not found!" << endl;  // 输出：Key not found!
}
```




- **eg1. unordered_map** : two sum problem(leetcode100)
``` cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> result;
        for(int i =0;i<nums.size();i++){       
            if(result.find(target-nums[i]) != result.end()){
                return {result[target-nums[i]],i};
            }
            else{
            //we can also use :
            //result.insert(pair<int,int>(nums[i],i));
            result[nums[i]] = i;
            }
        }
        return {};
    }
};
```
- **eg2. unordered_set :** 只出现一次的数字(leetcode100)
``` cpp
//只出现一次的数字
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream> 
#include<unordered_map> 
#include<unordered_set> 

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set <int>ans;
        for(int i=0;i<nums.size();i++){
            if(ans.find(nums[i]) != ans.end()){
                ans.erase(nums[i]);
            }
            else{
                ans.insert(nums[i]);
            } 
        }
        return *(ans.begin());
        
    }
};
```

---

## string 
1. 截取：
   ``` cpp
   string str = "C++ Programming";
    string sub = str.substr(0, 3);  // 从位置0开始，截取3个字符
   
    cout << "Substring: " << sub << endl;  // 输出 "C++"
   ```
   
2. 查找：
   ``` cpp
    string str = "Hello, C++ World!";
    size_t pos = str.find("C++");  // 查找子字符串"C++"
   
    if (pos != string::npos) {
        cout << "Found C++ at position: " << pos << endl;
    } else {
        cout << "C++ not found!" << endl;
    }
   
   ```
   
   3. 初始化：
   
      `string row = string(n, '.');` `row[position] = 'Q'`
   
   3. 遍历：
   

=== "vector <string>:: iterator it"

    ```cpp
    vector<string> vec = {"apple", "banana", "cherry"};
       
    // 使用迭代器遍历
    for (vector<string>::iterator it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
       
    ```

=== "auto"
    
    ```cpp
    vector<string> vec = {"apple", "banana", "cherry"};
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    ```

string:

=== "本体"

    ```cpp
    string str = "Hello, World!";
    
    // 使用基于范围的for循环遍历字符串
    for (char ch : str) {
        cout << ch << " ";  // 输出每个字符
    }
    
    for (auto ch : str) {
        cout << ch << " ";  // 输出每个字符
    }
    
    ```

=== "迭代器"

    ```cpp
    string str = "Hello, World!";
    
    // 使用迭代器遍历字符串
    for (auto it = str.begin(); it != str.end(); ++it) {
        cout << *it << " ";  // 输出每个字符
    }
    ```

!!! tip "关于 `const auto &` VS `auto`"
    `const string &` 来代替 string： string 会进行复制操作，创建一个新对象，而 `const string &` 不会进行复制操作，直接使用原来的对象，且不改变存储值 。函数形参里面不会变了 like ： string digits 也可以用 `const string &digits`，又或者是在 for 循环之中, 可以使用 `for (const auto &dir: directions)` 代替... 

    在函数参数中，& 表示 引用类型，它可以避免拷贝传递对象，从而提高效率。如果省略 &，则意味着传递的是 按值传递，即函数会拷贝一份参数对象到函数内部。
    
    & 的作用：
      pair<int, int>& m 表示 m 是对传入 pair<int, int> 对象的 引用，函数内部修改 m 会影响传入的对象。
      如果省略 &，则是按 值传递，意味着函数内部的修改不会影响原始的对象。




## vector

```cpp
 auto queens = vector<int>(n, -1);
```

创建 row 行 col 列并且初始化为 0：

```cpp
        int row = board.size();
        int col = board[0].size();
        vector<vector<int>> use(row,vector<int>(col,0));
```

初始化一个元素 pair 的容器，用.first 和.second 来访问前后元素

```cpp
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
```

使用 `ele : vec` : (most recommended)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<string> vec = {"apple", "banana", "cherry"};
    
    // 使用范围-based for 循环打印所有元素
    for (const string& elem : vec) {
        cout << elem << " ";
    }
    
    for (auto elem : vec) {
        cout << elem << " ";
    }
    
    cout << endl;
    return 0;
}

```

从 vector 中删除所有值为特定值的元素：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 初始化一个vector，包含一些整数
    vector<int> vec = {1, 2, 3, 4, 2, 5, 2, 6};
    int value_to_remove = 2;  // 要删除的特定值

    // 使用 remove 将值为 2 的元素移到末尾，并返回新有效区的迭代器
    auto new_end = remove(vec.begin(), vec.end(), value_to_remove);

    // 使用 erase 删除从 new_end 到 vec.end() 范围内的元素
    vec.erase(new_end, vec.end());

    // 打印删除后的结果
    for (const auto& num : vec) {
        cout << num << " ";
    }

    cout << endl;
    return 0;
}

```

`erase` 和 `remove` 是 C++ 中用于操作容器的两个常用函数，它们通常一起使用，尤其是在删除 `std::vector` 或 `std::list` 中的特定元素时。它们的作用不同，但可以结合起来完成删除操作。

###  **`remove` 函数**:

定义：

用于重新排列容器中的元素，使得所有不等于指定值的元素被移动到容器的前面，返回一个指向新“有效区域”末尾的迭代器。

语法：

```cpp
Iterator std::remove(Iterator first, Iterator last, const T& value);
```

- **`first`** 和 **`last`**：指定要操作的范围（通常是容器的迭代器）。
- **`value`**：指定要删除的元素的值。

特点：

- `std::remove` **并不会删除容器中的元素**，它只是将容器中的元素重新排列，把所有不等于 `value` 的元素移到前面，而将所有等于 `value` 的元素移到容器的末尾。
- 它返回的是一个新的迭代器，指向容器中不等于 `value` 的元素的末尾。

示例：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> vec = {1, 2, 3, 4, 2, 5, 2, 6};
    int value_to_remove = 2;

    // 使用 std::remove 将值为 2 的元素移到末尾
    auto new_end = remove(vec.begin(), vec.end(), value_to_remove);

    // 打印容器的状态，注意此时只将值为 2 的元素移到末尾，并没有删除
    for (auto it = vec.begin(); it != new_end; ++it) {
        cout << *it << " ";
    }
    cout << endl;

    return 0;
}
```

**输出**：

```
1 3 4 5 6
```

###  **`erase` 函数**:

定义：

`erase` 是容器（如 `std::vector`, `std::list`, `std::deque` 等）成员函数，用于删除容器中的元素。对于 `std::vector` 或 `std::deque`，`erase` 会真正删除指定位置的元素，并且缩小容器的大小。

语法：

```cpp
Iterator erase(Iterator position);
Iterator erase(Iterator first, Iterator last);
```

- **`position`**：指向容器中要删除元素的迭代器。
- **`first`** 和 **`last`**：指定一个范围，删除该范围内的所有元素。

特点：

- `erase` **真正删除元素**，并调整容器大小





- **删除索引 j 的元素 直接 erase**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec = {1, 2, 3, 4, 5, 6};
    int j = 2;  // 要删除的索引

    // 使用 erase 删除索引为 j 的元素
    if (j >= 0 && j < vec.size()) {
        vec.erase(vec.begin() + j);
    }

    // 打印删除后的结果
    for (const auto& num : vec) {
        cout << num << " ";
    }

    cout << endl;
    return 0;
}

```

## priority_queue

```cpp
#include<iostream>
#include <queue>
using namespace std;
int main() 
{
    //对于基础类型 默认是大顶堆
    priority_queue<int> a; 
    //等同于 priority_queue<int, vector<int>, less<int> > a;


    priority_queue<int, vector<int>, greater<int> > c;  //这样就是小顶堆
    priority_queue<string> b;

    for (int i = 0; i < 5; i++) 
    {
        a.push(i);
        c.push(i);
    }
    while (!a.empty()) 
    {
        cout << a.top() << ' ';
        a.pop();
    } 
    cout << endl;

    while (!c.empty()) 
    {
        cout << c.top() << ' ';
        c.pop();
    }
    cout << endl;

    b.push("abc");
    b.push("abcd");
    b.push("cbd");
    while (!b.empty()) 
    {
        cout << b.top() << ' ';
        b.pop();
    } 
    cout << endl;
    return 0;
}

```

输出：

```
4 3 2 1 0
0 1 2 3 4
cbd abcd abc
```

pari的比较，先比较第一个元素，第一个相等比较第二个:

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main() 
{
    priority_queue<pair<int, int> > a;
    pair<int, int> b(1, 2);
    pair<int, int> c(1, 3);
    pair<int, int> d(2, 5);
    a.push(d);
    a.push(c);
    a.push(b);
    while (!a.empty()) 
    {
        cout << a.top().first << ' ' << a.top().second << '\n';
        a.pop();
    }
}

```

输出：

```
2 5
1 3
1 2
```

### 自定义比较函数

#### simple method

```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// 自定义比较函数
bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    return a.first < b.first;  // a.first 小于 b.first 时返回 true，表示 a 会被排到后面
}

int main() {
    // 创建一个最大堆的 priority_queue
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(&cmp)> q(cmp);
    
    // 向优先队列中添加元素
    q.push({1, 100});
    q.push({3, 200});
    q.push({2, 150});
    
    // 输出堆顶元素
    while (!q.empty()) {
        cout << "(" << q.top().first << ", " << q.top().second << ")" << endl;
        q.pop();
    }

    return 0;
}

```

> 其中的 `decltype(&cmp)` 的类型是 `bool (*)(const pair<int, int>&, const pair<int, int>&)`，即它是一个 **指向比较函数** 的指针，返回类型是 `bool`，参数类型是 `const pair<int, int>&` 和 `const pair<int, int>&`。

??? bug

    **传递方式的区别：**
    
    - `const pair<int, int>& a` 表示通过 **常量引用** 传递 `pair<int, int>` 对象。引用避免了对象的拷贝，同时 `const` 修饰符保证了函数内部不能修改该对象。
    - `pair<int, int> a` 表示通过 **值传递** 传递一个 `pair<int, int>` 对象。此时会发生拷贝操作，传递的是对象的副本，可能会消耗额外的内存和时间。

!!! success
    **关于`decltype()`**用法




    ```cpp
    
    decltype(expression)
    
    - `expression`：这是你想要查询类型的表达式或变量。
    - `decltype` 返回该表达式的类型。
    ```



    ```cpp
    //eg. 获取变量的类型：
    int a = 10;
    decltype(a) b = 20;  // b 的类型与 a 相同，都是 int
    
    //eg. 函数指针类型
    
    bool cmp(int, int);
    decltype(&cmp) ptr = &cmp;  // ptr 是指向 cmp 函数的指针，类型是 bool(*)(int, int)
    
    ```

#### common method

```cpp linenums="1" hl_lines="12-19" 
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
 
struct node
{
    int x, y;
    node(int x,int y):x(x),y(y){}
};
 
struct cmp
{
    bool operator()(node a,node b)
    {
        if(a.x == b.x)  return a.y >= b.y;
        else return a.x > b.x;
    }
};
 
int main()
{
    priority_queue<node,vector<node>,cmp> pq;    //带有三个参数的优先队列;
    for(int i = 1; i <= 5; i++)
        for(int j = 1; j <= 5; j++)
            pq.push(node(i,j));
    while(!pq.empty())
    {
        cout<<pq.top().x<<" "<<pq.top().y<<endl;
        pq.pop();
    }
    return 0;
}
```



`operator()`  是 C++ 中的一个 **运算符重载** 的特殊形式，用于重载函数调用运算符，使得一个对象能够像函数一样被调用。它是 **固定的**，不能改成其他单词。

 **`operator()` 的作用：**

- `operator()` 使得你可以定义一个对象的行为，使其在调用时类似于函数的调用。
- 这种语法通常被称为 **函数对象**（或称为 **仿函数**）。通过重载 `operator()`，你可以让对象表现得像一个普通函数一样，接受参数并返回值。

 **示例：**

假设你有一个结构体 `cmp`，它重载了 `operator()`，使得其对象能够像函数一样被调用：

```cpp
#include <iostream>
using namespace std;

struct cmp {
    bool operator()(int a, int b) {
        return a > b;  // 比较两个整数，返回较大的那个
    }
};

int main() {
    cmp compare;  // 创建一个 cmp 类型的对象
    cout << compare(5, 3) << endl;  // 使用对象像函数一样调用，输出 1，因为 5 > 3
    return 0;
}
```

在这个例子中，`compare(5, 3)` 调用了 `operator()`，使得 `cmp` 对象 `compare` 充当了一个比较两个整数的函数。

于是自定义比较方式可以这么写





## 杂项

