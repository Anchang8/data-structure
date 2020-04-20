class Stack:

    def __init__(self):
        self.data=[]                 #list로 초기화
    def size(self):
        return len(self.data)        #stack의 길이를 반환
    def push(self,item):
        self.data.append(item)       #stack에 item을 추가.
    def pop(self):
        if len(self.data)>0:         #stack에 마지막원소를 제외한 list를 저장
            self.data=self.data[0:-1]
        else:
            print('Stack is empty')  #stack이 비었다면, Stack is empty출력
    def top(self):                   #stack의 가장 마지막 값을 반환
        if len(self.data)>0:
            print(self.data[-1])
        else:
            print('Stack is empty')  #stack이 비었다면, Stack is empty출력
    def empty(self):                 #stack이 비었다면, True 아니면 False 출력
        return len(self.data)==0 
    def view(self):                  #stack의 원소를 반환.
        print(self.data)
    
