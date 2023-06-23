import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

def view_clusters_3d(X, features=['n_clicks', 'n_visits', 'amount_spent']):

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    ax.scatter(X[features[0]], X[features[1]], X[features[2]], c=np.random.randn(X.shape[0]), marker='p',alpha=0.75, cmap='magma')
    ax.set_xlabel(features[0])
    ax.set_ylabel(features[1])
    ax.set_zlabel(features[2])
    plt.show()