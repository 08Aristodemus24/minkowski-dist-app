import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class KMeans:
    def __init__(self, X, K, epochs=10, initializer="permutation", dist_metric='euclidean', p=3):
        self.X = X
        self.K = K
        self.num_instances = X.shape[0]
        self.num_features = X.shape[1]
        self.epochs = epochs
        self.initializer = initializer
        self.dist_metric = dist_metric

        # this is used if distance metric is minkowski
        self.p = p


    def init_centroids(self, X):
        # num features and clusters
        num_instances, K = self.num_instances, self.K

        if self.initializer == "random_sampling":
            # sample K samples from the list of indeces
            rand_idxs = np.random.choice(list(range(num_instances)), size=K, replace=False)
            print(rand_idxs)

        elif self.initializer == "permutation":
            # Randomly reorder the indices of examples
            rand_idxs = np.random.permutation(num_instances)[:K]


        # get the data points with these random indeces
        init_centroids = X[rand_idxs, :]

        # init_centroids = np.array([
        #     [35, 500],
        #     [45, 800],
        #     [22, 300]
        # ])
        return init_centroids

    def get_dist(self, curr_x, centroids):
        dist_metric = self.dist_metric

        if dist_metric == 'manhattan':
            return np.sum(np.abs(curr_x - centroids), axis=1)
        
        elif dist_metric == 'euclidean':
            temp = np.sum((curr_x - centroids) ** 2, axis=1)
            
            return np.sqrt(temp)

        elif dist_metric == 'minkowski':
            p = self.p
            temp = np.sum((curr_x - centroids) ** p, axis=1)

            return np.power(temp, 1 / p)

    def _assign_centroids_to_xs(self, X, centroids):
        """
        assigns the appropriate centroid for every example
        
        Args:
            X (ndarray): (m, n) Input values      
            centroids (ndarray): (K, n) centroids
        
        Returns:
            xs_centroids (array_like): (m,) values that indicate the
            respective centroids of each training example
        
        """

        # the vector which contains all the 
        # centroids assigned to a particular index
        num_instances = self.num_instances
        xs_centroids = np.zeros(shape=(num_instances))

        for index in range(num_instances):
            # index denotes what training example is to be assigned to the closest 
            # centroid there are k centroids so np.argmin will be values from 0 to k-1
            dist = self.get_dist(X[index], centroids)
            xs_centroids[index] = np.argmin(dist)

        return xs_centroids

    def _calc_centroids(self, X, xs_centroids, K):
        """
        Returns the new centroids by computing the means of the 
        data points assigned to each centroid.
        
        Args:
            X (ndarray):   (m, n) Data points
            xs_centroids (ndarray): (m,) Array containing index of closest centroid for each 
                        example in X. Concretely, idx[i] contains the index of 
                        the centroid closest to example i
            K (int):       number of centroids
        
        Returns:
            new_centroids (ndarray): (K, n) New centroids computed
        """

        # Useful variables
        n = self.num_features
        
        # You need to return the following variables correctly
        new_centroids = np.zeros((K, n))
        
        
        # loops from 0 to k-1
        for k in range(K):
            # extract all the points closest/assigned to centroid k
            points_of_ck = X[np.where(xs_centroids == k)]
            print(f'points of cluster {k}: {points_of_ck}\n')

            # calculate the mean of these data points
            new_centroids[k] = np.sum(points_of_ck, axis=0) / len(points_of_ck)
        
        return new_centroids


    def train(self):
        X, K = self.X, self.K
        print(X)
        init_centroids = self.init_centroids(X)

        print(f'initial centroids {init_centroids}\n')
        self.visualize(X, dimension='3d')

        prev_centroids = []
        
        # somehow store the assigned datapoints to each centroid here

        # assign centroids to initial centroids since this will change overtime
        centroids = init_centroids
        for epoch in range(self.epochs):
            # print(f'epoch {epoch}/{self.epochs - 1}')

            # assign appropriate centroids to every data point
            xs_centroids = self._assign_centroids_to_xs(X, centroids)

            # save previous centroids before assining new centroids
            prev_centroids.append(centroids)
            print(f'centroid at epoch {epoch}/{self.epochs - 1}: \n{centroids}\n')

            # calculate new centroids after assigning
            # appropriate centroids to every data point
            centroids = self._calc_centroids(X, xs_centroids, K)
        
        # assign appropriate centroids and then
        # add last centroid to the prev_centroids
        xs_centroids = self._assign_centroids_to_xs(X, centroids)
        prev_centroids.append(centroids)
        print(f'centroid at epoch {epoch}/{self.epochs - 1}: \n{centroids}\n')


        # plot centroids across iterations
        self.plot_evolution(X, np.array(prev_centroids), xs_centroids, dimension='3d')
            
    def plot_evolution(self, X, centroids, xs_centroids, dimension='2d'):
        """
        centroids - a 3D tensor of shape (epochs, K, n)
        """
        K = self.K


        fig = plt.figure(figsize=(11, 11))

        if dimension.lower() == '2d':
            axis = fig.add_subplot()
            axis.scatter(X[:, 0], X[:, 1], color='#90b2e8', marker='p',alpha=0.75,)
            # axis.scatter(X[:, 0], X[:, 1], c=np.random.randn(self.num_instances), marker='p',alpha=0.75, cmap='magma')

            for k in range(K):
                # gets all the centroids of cluster K at each epoch
                cs_of_k = centroids[:, k, :]
                m = cs_of_k.shape
                print(f'm: {m}')
                
                print(f'centroids of cluster {k}: {cs_of_k}\n')
                axis.plot(cs_of_k[:, 0], cs_of_k[:, 1], 'x--', alpha=0.25, color='black')
                axis.plot(cs_of_k[-1, 0], cs_of_k[-1, 1], 'p', color='#d60f7d')

        elif dimension.lower() == '3d':
            # 3d figure
            axis = fig.add_subplot(111, projection='3d')
            # axis.scatter(X[:, 0], X[:, 1], X[:, 2], c=np.random.randn(X.shape[0]), marker='p',alpha=0.5, cmap='magma')
            # axis.scatter(X[:, 0], X[:, 1], X[:, 2], color='#90b2e8', marker='p',alpha=0.75,)

            colors = ['viridis', 'magma', 'twilight']
            for k in range(K):
                # extract all datapoints assigned to certain cluster
                cluster_k = X[xs_centroids == k]
                axis.scatter(cluster_k[:, 0], cluster_k[:, 1], cluster_k[:, 2], c=np.random.randn(cluster_k.shape[0]), marker='p',alpha=0.375, cmap=colors[k])

            for k in range(K):
                # gets all the centroids of cluster K at each epoch
                cs_of_k = centroids[:, k, :]
                m = cs_of_k.shape
                print(f'm: {m}')
                
                print(f'centroids of cluster {k}: {cs_of_k}\n')
                axis.plot(cs_of_k[:, 0], cs_of_k[:, 1], cs_of_k[-1, 2], 'x--', color='black')
                axis.plot(cs_of_k[-1, 0], cs_of_k[-1, 1], cs_of_k[-1, 2], 'p--', color='#ff00bf')

            # n_clicks, amount_discount, amount_spent
            axis.set_xlabel('x: n_clicks')
            axis.set_ylabel('y: amount_discount')
            axis.set_zlabel('z: amount_spent')

            

            

        plt.legend()
        plt.show()

    def visualize(self, X, dimension='2d'):
        fig = plt.figure(figsize=(11, 11))

        if dimension.lower() == '2d':    
            axis = fig.add_subplot()
            axis.scatter(X[:, 0], X[:, 1], color='#000000', marker='p',alpha=0.75,)
            axis.set_xlabel('age')
            axis.set_ylabel('monthly_mileage')

        elif dimension.lower() == '3d':
            # 3d figure
            axis = fig.add_subplot(111, projection='3d')
            axis.scatter(X[:, 0], X[:, 1], X[:, 2], color='#000000', marker='p',alpha=0.75,)

            # n_clicks, amount_discount, amount_spent
            axis.set_xlabel('x: n_clicks')
            axis.set_ylabel('y: amount_discount')
            axis.set_zlabel('z: amount_spent')
        

        plt.legend()
        plt.show()


def load_ext_data():
    X = np.load("data/ex7_X.npy")
    return X

def load_ecomm_data(path, features: list):
    X = pd.read_csv(path)
    # drop ID and profile information column column
    X.drop(columns=['ID', 'profile_information'], inplace=True)
    
    return X[features].to_numpy()

