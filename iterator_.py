class MyCount:
    def __iter__(self):
        self.c = 1
        return self
    
    def __next__(self):
        if self.c<20:
            self.c+=1
            return self.c
        else:
            return StopIteration

        
count_down = MyCount()
for c in count_down:
    print(c)
