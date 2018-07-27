class Queue(object):
    def __init__(self):        #队列的构造函数方法
        self.Queue = []
    def enqueue(self,value):      #入队列方法
        self.Queue.append(value)
    def bequeue(self):            #出队列方法
        if not self.isempty():
            return self.Queue.remove(self.Queue[0])
        else:
            return None
    def top(self):                #队列顶部方法
        if not self.isempty():
            return self.Queue[0]
        else:
            return None
    def length(self):             #队列长度方法
        return len(self.Queue)
    def view(self):               #查看队列元素方法
        for i in self.Queue:
            print(i)
    def isempty(self):            #判断队列是否为空方法
        return self.Queue == []
queue1 = Queue()                  #队列实例化
#item1 = raw_input("item1:")
#stack1.push(item1)
queue1.enqueue(6)
queue1.enqueue(8)

queue1.view()
queue1.length()
print("stack1:")


queue1.bequeue()
print("\nstack1:")
queue1.view()


class Stack:
    """使用 list 来模拟栈"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):  #入栈顶方法
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
#s.isEmpty() = True
s.push(4)
s.push('dog')
# s.peek() = 'dog'
# s.size() = 2
# s.pop() = 'dog'
# s.pop() = 4

'''
常见Linux命令
SuperUseDo
sudo su

/home$ ls
处理home文件夹下的目录文件和文件夹

更改目录进入到当前文件下的下一个文件目录中
/home $ cd usr
/home/usr $

更改目录后创建一个新文件夹
$ mkdir folderName

粘贴 复制 命令 要粘贴的文件  要去的地址（文件）
$ cp src des

删除
$ rm nyfile.txt
 
 更新
 $sudo apt—get update
 
 $ sudo dnf update
 
 查找一个文件
 $ grep user /etc/passwd
 
 查找文档或者代码
 $ cat CMakeLists.txt
 
 关机操作
 $ sudo poweroff
 
'''
