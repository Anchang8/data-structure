class Queue:

    def __init__(self):
        self.data=[]                 #list로 초기화
    def size(self):
        return len(self.data)        #Queue의 길이를 반환
    def enqueue(self,item):
        self.data.insert(0,item)       #Queue에 item을 추가.
    def dequeue(self):
        if len(self.data)>0:         #Queue에 마지막원소를 제외한 list를 저장
            deq=self.data[-1]
            self.data=self.data[0:-1]
            return deq
        else:
            print('Queue is empty')  #Queue가 비었다면, Stack is empty출력
    def peek(self):                   #Queue의 가장 앞쪽의 값을 반환
        if len(self.data)>0:
            print(self.data[-1])
        else:
            print('Queue is empty')  #Queue가 비었다면, Queue is empty출력
    def empty(self):                 #Queue가 비었다면, True 아니면 False 출력
        return len(self.data)==0 
    def view(self):                  #Queue의 원소를 반환.
        print(self.data)
