# Import packages
import numpy as np
import chainer
import chainer.functions as F
import chainer.links as L

# Network definition in chainer
class MLP(chainer.ChainList):

    # Initilize the nueral network architecture
    def __init__(self, conv_layer = [], fully_connected_layer = []):
        super(MLP, self).__init__()
        self.n_Conv = len(conv_layer)          # The number of convolution layer
        self.n_FC = len(fully_connected_layer) # The number of fully connected layer
        with self.init_scope():
            # Add convolution layer to network
            for n_kernels in conv_layer:
                self.add_link(L.Convolution2D(None, out_channels = n_kernels, ksize = (3, 3), stride = 1))
            # Add fully connected layer to network
            for n_units in fully_connected_layer:
                self.add_link(L.Linear(None, n_units))

    def __call__(self, x):
        return self.forward(x)

    # Forward propagation processes
    def forward(self, x):
        for i_Conv in range(self.n_Conv):
            out = F.relu(self[i_Conv](x))
            out = F.max_pooling_2d(out, 2)
        for i_FC in range(self.n_FC):
            out = F.relu(self[i_Conv + 1 + i_FC](out))
        return out

# Get predicted answer
# Input: Img data (28 * 28, gray scale)
# Output: Predicted answer (0-9)
def get_predicted_answer(data):
    # Feed into the model and Output predicted value
    predicted_value = MODEL(data).data
    print(predicted_value)

    # Now, predicted_value is probability value.
    # Predicted_value is applied argmax,
    # because we want the answer (The answer is integer 0-9).
    answer = np.argmax(predicted_value)
    return answer

if __name__ == 'ans_prediction':
    # Set up the model
    FILE_NAME = './MNIST_Model_C16_f30_20_10.npz' # Model path
    MODEL = MLP(conv_layer = [16], fully_connected_layer = [30, 20, 10])
    chainer.serializers.load_npz(FILE_NAME, MODEL) # Load the model
