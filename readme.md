## Usage:
in the directory where `tests.py` exists run command `python tests.py <p value e.g. 1, 2, 3, ..., n>`

## Questions and insights:
### **Where is the minkowski distance metric usually used. To what problem setting does it apply?**
ChatGPT
The Minkowski distance metric is a generalization of other distance metrics such as the Euclidean distance and the Manhattan distance. It is used in various problem settings and is particularly applicable in cases where you need to measure the similarity or dissimilarity between two objects in a multidimensional space.

The Minkowski distance metric is defined as:

D(x, y) = (Σ(|xi - yi|^p))^(1/p)

Here, x and y represent two data points in a d-dimensional space, and p is a parameter that determines the type of Minkowski distance. Depending on the value of p, different distance metrics are obtained:

When p = 1, the Minkowski distance reduces to the Manhattan distance, also known as the L1 distance. It represents the sum of absolute differences between the coordinates of two points. It is commonly used in applications where movement along grid-like paths is more restricted, such as routing problems or image recognition.

When p = 2, the Minkowski distance becomes the Euclidean distance, which represents the straight-line distance between two points in Euclidean space. It is widely used in various fields, including clustering algorithms, recommendation systems, and image recognition.

When p -> ∞, the Minkowski distance becomes the Chebyshev distance. It represents the maximum absolute difference between the coordinates of two points and is used in applications where movement is allowed in any direction.

The choice of the value of p depends on the specific problem and the characteristics of the data. The Minkowski distance metric provides flexibility in adjusting the sensitivity to different dimensions and can be tailored to different problem settings.

### **so what characteristics does a dataset need to have where usually the minkowski distance is used to determine distance between two datapoints?**
ChatGPT
The Minkowski distance can be used with datasets that have the following characteristics:

Numerical Features: The Minkowski distance is suitable for datasets that consist of numerical features or variables. It measures the distance between two data points based on the differences in their numerical values.

Continuous or Discrete Variables: The Minkowski distance can be applied to datasets with continuous or discrete variables. It is not limited to a specific type of variable and can handle both types of data.

Multidimensional Space: The Minkowski distance is particularly useful when dealing with datasets that exist in a multidimensional space. It calculates the distance between data points by considering the differences in each dimension or feature.

Equal Importance of Features: The Minkowski distance assumes equal importance or weightage for each feature. It treats all dimensions equally when calculating the distance between two data points. If certain features have different levels of importance, feature scaling or weighting may be necessary.

Data Normalization: It is advisable to normalize the data before applying the Minkowski distance, especially if the features have different scales or units. Normalization ensures that all variables contribute proportionally to the distance calculation.

Flexible Distance Measure: The Minkowski distance provides flexibility in choosing the value of the parameter p. By adjusting the value of p, you can control the sensitivity of the distance measure to different dimensions or features in the dataset.

It's important to note that the choice of distance metric, including the Minkowski distance, depends on the specific problem, data characteristics, and the goals of the analysis. Different distance metrics may be more suitable for certain types of data or specific analysis tasks. Therefore, it is recommended to assess the properties of the dataset and consider the specific requirements of the problem before selecting the appropriate distance measure.

### **but even in multi dimensional datasets why wouldn't distance metrics like euclidean distance still apply? Why use minkowski?**
ChatGPT

You are correct that the Euclidean distance is a commonly used distance metric in multidimensional datasets. The Euclidean distance measures the straight-line distance between two points in Euclidean space and is widely applicable in various domains.

The Minkowski distance is a generalization of the Euclidean distance and provides additional flexibility by introducing the parameter "p". By adjusting the value of "p", the Minkowski distance can behave differently and adapt to different scenarios. Specifically:

When "p" is set to 1, the Minkowski distance becomes the Manhattan distance (L1 norm). The Manhattan distance measures the sum of absolute differences between the coordinates of two points. It is suitable for situations where movement is restricted to grid-like paths or when the importance of different dimensions varies.

When "p" is set to 2, the Minkowski distance reduces to the Euclidean distance (L2 norm). The Euclidean distance represents the straight-line distance between two points in Euclidean space. It is widely used and appropriate when all dimensions are equally important.

When "p" is set to higher values, the Minkowski distance places greater emphasis on larger differences in coordinates. This can be useful in scenarios where outliers or extreme values in certain dimensions have a significant impact on the overall distance calculation.

In summary, while the Euclidean distance is a widely used and effective distance metric, the Minkowski distance provides additional flexibility by allowing you to adjust the value of "p" and adapt the distance measure to different scenarios. It allows for different notions of distance, such as emphasizing certain dimensions or accommodating specific data characteristics. The choice between the Euclidean distance and the Minkowski distance with a specific "p" value depends on the specific problem, the data, and the desired behavior of the distance metric.


### **Dataset:**
1. E-Commerce.csv - From git repo https://github.com/MauricioLetelier/E-commerce-Clustering.git
2. e-comm-data-1.csv - From kaggle https://www.kaggle.com/datasets/mervemenekse/ecommerce-dataset
About Dataset
Introduction
Analyzing the purchases of our customers for 1 year in America E-commerce dataset. How are their customer's online buying habits?

Columns name and meanings:
Order_Date: The date the product was ordered.

Aging: The time from the day the product is ordered to the day it is delivered.

Customer_id: Unique id created for each customer.

Gender: Gender of customer.

Device_Type: The device the customer uses to actualize the transaction (Web/Mobile).

Customer_Login_Type: The type the customer logged in. Such as Member, Guest etc.

Product_Category: Product category

Product: Product

Sales: Total sales amount

Quantity: Unit amount of product

Discount: Percent discount rate

Profit: Profit

Shipping_cost: Shipping cost

Order_Priority: Order priority. Such as critical, high etc.

Payment_method: Payment method

Here is the some question that you can start with;
-What devices do my customers use to reach me?
-Who is the customer base?
-What product categories am I selling?
-Which product categories do I sell to whom? (Gender Distribution by Category or Product?)
-Which login type do my customers prefer when shopping?
-How does the date and time affect my sales? (Total sales by month, the days of week or time arrival)
-From which product do I earn the most profit per unit?
-How is my delivery speed and order priority?(Delivery Time distribution of order priority by months)

3. e-comm-data-2.csv - From kaggle https://www.kaggle.com/datasets/carrie1/ecommerce-data
About Dataset
Context
Typically e-commerce datasets are proprietary and consequently hard to find among publicly available data. However, The UCI Machine Learning Repository has made this dataset containing actual transactions from 2010 and 2011. The dataset is maintained on their site, where it can be found by the title "Online Retail".

Content
"This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers."

Acknowledgements
Per the UCI Machine Learning Repository, this data was made available by Dr Daqing Chen, Director: Public Analytics group. chend '@' lsbu.ac.uk, School of Engineering, London South Bank University, London SE1 0AA, UK.

Image from stocksnap.io.

Inspiration
Analyses for this dataset could include time series, clustering, classification and more.


### **Exploratory Data Analysis**
1. What feature sets are relevant in such a way that it forms clusters when visualized?
2. What insights could be derived from these clusters?
3. Are the features of the selected relevant feature sets correlated to each other in some regard?
4. ID could be assumed as the product ID the user of the online platform has interacted with
5. profile_information could be assumed as the ID designated to the user interacting with a specific item
6. cluster 1 has customers that have high amount discount and high amount spent which may imply that the more a customer of this kind purchases products the more he/she is granted discount


### **References:**
1. https://towardsdatascience.com/log-book-guide-to-distance-measuring-approaches-for-k-means-clustering-f137807e8e21
2. https://www.researchgate.net/publication/353057640_New_K-means_Clustering_Method_Using_Minkowski's_Distance_as_its_Metric


