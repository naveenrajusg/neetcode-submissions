class KthLargest:
    def heapify(self,arr):
        arr = [0] + arr [:]
        converted = arr
        cur = (len(converted)-1)//2
        while cur>0:
            i = cur
            while 2*i < len(converted):
                if (2*i+1<len(converted)) and (converted[2*i+1]<converted[2*i]) and (converted[i]>converted[2*i+1]):
                    temp = converted[i]
                    converted[i]=converted[2*i+1] 
                    converted[2*i+1] = temp
                    i = 2*i+1
                elif converted[i]>converted[2*i]:
                    temp = converted[i]
                    converted[i]=converted[2*i] 
                    converted[2*i] = temp
                    i = 2*i
                else:
                    break
            cur-=1
        return converted

    def push(self,val):
        if len(self.heap)==0:
            self.heap = [0]
        self.heap.append(val)
        i = len(self.heap)-1

        while self.heap[i]<self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i//2

    def pop(self):
        if len(self.heap)==1:
            return None
        if (len(self.heap)) == 2:
            self.heap.pop()
            return

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        while 2*i < len(self.heap):
            if (2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1]< self.heap[i] ):
                # swap right
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[2*i+1] = temp
                i = 2*i+1
            elif self.heap[2*i]<self.heap[i]:
                # swap left child
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = temp
                i = 2*i
            else:
                break
        


    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        # heapq.heapify(self.heap)
        self.heap = self.heapify(self.heap)
        # while len(self.heap) > k:
        while len(self.heap) > k+1: #because in our custom heap we have dummy value at 0, thus our heap starts from index 1
            # heapq.heappop(self.heap)
            self.pop()


    def add(self, val: int) -> int:
        # heapq.heappush(self.heap,val)
        self.push(val)
        # if len(self.heap) > self.k:
        if len(self.heap) > self.k +1: #because in our curom heap we have dummy value at 0, thus our heap starts from index 1
            # heapq.heappop(self.heap)
            self.pop()

        # return self.heap[0]
        return self.heap[1] #becasue in our custom heap creation it starts from index 1

