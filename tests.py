from algorithm.kmeans import KMeans, load_ecomm_data, load_ext_data
import sys

if __name__ == "__main__":
    p = int(sys.argv[1])

    
    feature_sets = [
        ['n_clicks', 'amount_discount', 'amount_spent'],
        ['n_visits', 'amount_discount', 'amount_spent'],
        ['amount_spent', 'days_since_registration', 'amount_discount'],
    ]

    # data = load_ext_data()
    

    for feature_set in feature_sets:
        data = load_ecomm_data('./data/E-commerce.csv', feature_set)
        # model = KMeans(data, 3,)
        model = KMeans(data, 3, dist_metric='minkowski', features=feature_set, p=p)
        model.train()