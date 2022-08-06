class Currency:
    def __next__(self):
        n = self.counter
        self.counter += 1
        if self.counter > 2:
            raise StopIteration


    def __init__(self,rs,paisa):
        self.total = rs*100 + paisa

    def __str__(self):
        r = self.total // 100
        p = self.total % 100
        
