class ChoiceGenerator:
    '''
    Generates (nonrecursively) all of the combinations of a choose b, where a, b
    are nonnegative integers and a >= b.  The values of a and b are given in the
    constructor, and the sequence of choices is obtained by repeatedly calling
    the next() method.  When the sequence is finished, null is returned.
    A valid combination for the sequence of combinations for a choose b
    generated by this class is an array x[] of b integers i, 0 <= i < a, such
    that x[j] < x[j + 1] for each j from 0 to b - 1.
    '''

    def __init__(self, a, b):
        '''
        Constructs a new choice generator for a choose b. Once this
        initialization has been performed, successive calls to next() will
        produce the series of combinations.  To begin a new series at any time,
        call this init method again with new values for a and b.

        Parameters
        ----------
        a: the number of objects being selected from.
        b: the number of objects in the desired selection.

        Returns
        -------
        ChoiceGenerator : ChoiceGenerator instance
        '''

        self.a = a
        self.b = b
        self.diff = a - b
        self.choiceLocal = []
        for i in range(b - 1):
            self.choiceLocal.append(i)
        if b > 0:
            self.choiceLocal.append(b - 2)
        self.choiceReturned = [ 0 for i in range(b)]
        self.begun = False

    def fill(self, index):
        self.choiceLocal[index] += 1
        for i in range(index+1, self.b):
            self.choiceLocal[i] = self.choiceLocal[i - 1] + 1

    def next(self):
        i = self.b

        while i > 0:
            i -= 1
            if self.choiceLocal[i] < (i + self.diff):
                self.fill(i)
                self.begun = True
                for j in range(self.b):
                    self.choiceReturned[j] = self.choiceLocal[j]
                return self.choiceReturned

        if self.begun:
            return None
        else:
            self.begun = True
            for j in range(self.b):
                self.choiceReturned[j] = self.choiceLocal[j]
            return self.choiceReturned