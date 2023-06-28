from algorithm.kmeans import KMeans, load_ecomm_data, load_ext_data
import sys

if __name__ == "__main__":
    p = int(sys.argv[1])

    
    feature_sets = [
        ['n_clicks', 'amount_discount', 'amount_spent'],
        ['n_visits', 'amount_discount', 'amount_spent'],
        ['amount_spent', 'n_clicks', 'amount_discount'],
        ['amount_spent', 'n_visits', 'amount_discount'],
        ['amount_spent', 'amount_discount', 'n_clicks'],
        ['amount_spent', 'amount_discount', 'n_visits'],
        ['amount_spent', 'days_since_registration', 'amount_discount'],
        ['amount_discount', 'n_clicks', 'n_clicks'],
        ['amount_discount', 'n_visits', 'amount_spent'],
        ['amount_discount', 'days_since_registration', 'amount_spent']
    ]

    # data = load_ext_data()
    data = load_ecomm_data('./data/E-commerce.csv', ['n_clicks', 'amount_discount', 'amount_spent'])

    # model = KMeans(data, 3,)
    model = KMeans(data, 3, dist_metric='minkowski', p=p)
    model.train()