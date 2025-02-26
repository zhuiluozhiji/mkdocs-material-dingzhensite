

## hash

**1. Hash 的插入可以有这样的操作**

```   
Unordered_map <string,int> result;
Result[“aa”] = 23;
```
> 作为对比：Vector 的插入不可以直接用数组的方式，必须使用 `emplace_back/push_back` 或者 `insert(“position”,things)`;


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

    ``` cpp
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



### code 


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

## vector

创建 row 行 col 列并且初始化为 0：

```cpp
        int row = board.size();
        int col = board[0].size();
        vector<vector<int>> use(row,vector<int>(col,0));
```

初始化一个元素 pair 的容器，用.first 和.second 来访问前后元素

```
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
```

