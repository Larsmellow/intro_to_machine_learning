import numpy as np


class Network(object):

    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(self,z):
        return 1.0/(1.0+np.exp(-z))

    def feedforwards(self,a):
        #Return the output of the network if a is input
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a)+b)
        return a
    
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        #Train the neural network
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(trainig_data)
            mini_batches = [training_data[k:mini_batch_size]
                        for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch,eta)
                if test_data:
                    print "Epoch {0}: {1}/{2}".format(
                    j,self.evaluate(test_data),n_test)
                else:
                    print "Epoch {0} complete".format(j)
            
