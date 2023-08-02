class CalcAttr(object):

    def __init__(self, a):
        self.a = a

    @property
    def b(self):
        return self.a + 5

    @property
    def c(self):
        return self.a * self.b