class dot:
    def __init__(self, *params, **keys):
        self.params = params
        self.keys = keys

    def log(self):
        if self.params:
            for p in self.params:
                print(p)
        if self.keys:
            for k in self.keys:
                print(k)
