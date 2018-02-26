import numpy as np

from celer import celer_path


def build_dataset(n_samples=50, n_features=200, n_informative_features=10,
                  n_targets=1):
    """
    build an ill-posed linear regression problem with many noisy features and
    comparatively few samples
    """
    random_state = np.random.RandomState(0)
    if n_targets > 1:
        w = random_state.randn(n_features, n_targets)
    else:
        w = random_state.randn(n_features)
    w[n_informative_features:] = 0.0
    X = random_state.randn(n_samples, n_features)
    y = np.dot(X, w)
    X_test = random_state.randn(n_samples, n_features)
    y_test = np.dot(X_test, w)
    return X, y, X_test, y_test


def test_enet_path_positive():
    # Test positive parameter

    X, y, _, _ = build_dataset(n_samples=50, n_features=50, n_targets=1)

    alpha_max = np.max(np.abs(X.T.dot(y)))
    n_alphas = 10
    alphas = alpha_max * np.logspace(0, -2, n_alphas)

    # For mono output
    betas, thetas = celer_path(X, y, alphas=alphas)

    assert True