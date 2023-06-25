from algorithm.kmeans import KMeans, load_ecomm_data, load_ext_data

if __name__ == "__main__":
    # data = load_ext_data()s
    data = load_ecomm_data('./data/E-commerce.csv', ['n_clicks', 'amount_discount', 'amount_spent'])
    # model = KMeans(data, 3, dist_metric='minkowski')
    model = KMeans(data, 3, dist_metric='minkowski', p=2)
    model.train()