#!/usr/bin/env python3
import argparse

import numpy as np
import sklearn.datasets
import sklearn.model_selection

def main(args):
    # Load Boston housing dataset
    dataset = sklearn.datasets.load_boston()
    print(dataset.DESCR)

    # The input data are in dataset.data, targets are in dataset.target.

    # TODO: Pad a value of "1" to the input data.

    # TODO: Split data so that the last `args.test_size` data are the test
    # set and the rest is the training set

    # TODO: Solve the linear regression using the algorithm from the lecture,
    # explicitly computing the matrix inverse (using np.linalg.inv).

    # TODO: Predict target values on the test set

    # TODO: Compute root mean square error on the test set predictions
    rmse = None

    with open("linear_regression_manual.out", "w") as output_file:
        print("{:.2f}".format(rmse), file=output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_size", default=50, type=int, help="Test size to use")
    args = parser.parse_args()
    main(args)
