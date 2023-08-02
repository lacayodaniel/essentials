class Question1:
    def reverseArray(self, A, i, j):
        print("run")
        if i > j:
            print(A)
            return
        A[i], A[j] = A[j], A[i]
        self.reverseArray(A, i+1, j-1)