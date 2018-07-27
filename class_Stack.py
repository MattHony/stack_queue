class Stack(object):
    def __init__(self):           #栈的构造方法
        self.Stack = []
    def push(self,value):         #入栈方法
        self.Stack.append(value)
    def pop(self):                #出栈方法
        if not self.isempty():
            return self.Stack.pop()
        else:
            return None
    def top(self):                #栈顶元素方法
        if not self.isempty():
            return self.Stack[-1]
        else:
            return None
    def length(self):             #栈的长度方法
        return len(self.Stack)
    def view(self):               #查看栈元素的方法
        for i in self.Stack:
            print(i)
    def isempty(self):            #判断栈是否为空方法
        return self.Stack == []
stack1 = Stack()                  #栈实例化
#item1 = raw_input("item1:")
#stack1.push(item1)
stack1.push(6)
stack1.push(8)
print("stack1:")
stack1.view()
stack1.pop()
print("\nstack1:")
stack1.view()


