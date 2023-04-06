import numpy as np

def calculate_cov_matrix():
    data = [[2, 20],
            [3, 24],
            [6, 36],
            [8, 47],
            [2.6, 22],
            [4.8, 32],
            [7, 47],
            [4, 42],
            [2, 21],
            [2.2, 21],
            [3.8, 30],
            [2.4, 25],
            [2.6, 18],
            [5.4, 38],
            [5.1, 28]
            ]
    nData = len(data)

    x = np.array(data)
    x_mean = x
    x_mean[:, 0] = x[:, 0] - np.mean(x[:, 0])
    x_mean[:, 1] = x[:, 1] - np.mean(x[:, 1])

    print('mean adjust of data')
    print(x_mean)

    res = x_mean.T @ x_mean / nData

    print('\n')
    print('covariance matrix(from definition):')
    print(res)

    c = np.cov(x.T, bias=True)
    print('\n')
    print('covariance matrix(python function):')
    print(c)

if __name__ == '__main__':
    calculate_cov_matrix()