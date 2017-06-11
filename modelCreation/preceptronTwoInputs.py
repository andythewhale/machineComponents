#Good perceptron example with 2 inputs that another user showed.


class TwoStepFun(object):
   
    def __init__(self, threshold=0.5):
        self.threshold = threshold
    def __call__(self, value):
        if value < self.threshold:
            return 0
        else:
            return 1
class Perceptron(object):
    """Represent a perceptron with 2 inputs, bias.
    >>> p1 = Perceptron(TwoStepFun(1))
    >>> p1.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p1(a,b) for a in bits for b in bits]
    [0, 0, 0, 1]
    >>> p2 = Perceptron(TwoStepFun(0.5))
    >>> p2.weights = [0.6, 0.6, 0.0]
    >>> bits = [0,1]
    >>> [p2(a,b) for a in bits for b in bits]
    [0, 1, 1, 1]
    """
    def __init__(self, transfer):
        from random import random
        self.transfer = transfer
        self.weights = [random()*4-2,
                        random()*4-2,
                        random()*4-2]
    def __call__(self, x0, x1):
        avg = (x0 * self.weights[0] +
               x1 * self.weights[1] +
               1  * self.weights[2])
        return self.transfer(avg)
    def learn(self, x0, x1, target):
    
        out = self(x0,x1)
        error = target-out
        learning_rate = 0.2
        delta0 = learning_rate * error * x0
        delta1 = learning_rate * error * x1
        delta2 = learning_rate * error  * 1
        self.weights[0] += delta0
        self.weights[1] += delta1
        self.weights[2] += delta2
        return error
        
if __name__ == "__main__":
    
    from datetime import datetime
    import random
    import doctest
    random.seed(datetime.now())
    doctest.testmod()
    p = Perceptron(TwoStepFun(0.5))
    print(p.weights)
    bits = [0,1]
    wrong = 0
    for a in bits:
        for b in bits:
            wrong += abs(p.learn(a,b, a*b)) #AND
            print(p.weights)
            if wrong == 0:
                print("Done!")
                break