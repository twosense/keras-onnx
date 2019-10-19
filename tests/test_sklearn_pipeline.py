import unittest

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import MinMaxScaler

from keras2onnx.proto import keras
from tests.test_layers import Dense, Sequential


class TestSklearnPipeline(unittest.TestCase):


    def test_keras_estimator_in_pipeline(self):
        pipeline = make_pipeline([MinMaxScaler(),
                                  KerasEstimator()])




class KerasEstimator(Sequential):
    def __init__(self):
        super().__init__()
        super().add(Dense(5, input_shape=(4,), activation='sigmoid'))
        super().add(Dense(3, input_shape=(5,)))
        super().compile('sgd', 'mse')

if __name__ == '__main__':
    unittest.main()
