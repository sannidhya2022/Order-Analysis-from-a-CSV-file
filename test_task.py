import unittest
import pandas as pd

class TestOrderAnalysis(unittest.TestCase):
    
    def setUp(self):
        self.data = pd.read_csv('orders.csv')
        self.data['order_date'] = pd.to_datetime(self.data['order_date'])
        self.data['month'] = self.data['order_date'].dt.to_period('M')

    def test_monthly_revenue(self):
        monthly_revenue = self.data.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        self.assertTrue(isinstance(monthly_revenue, pd.Series))

    def test_product_revenue(self):
        product_revenue = self.data.groupby('product_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        self.assertTrue(isinstance(product_revenue, pd.Series))
    
    def test_customer_revenue(self):
        customer_revenue = self.data.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        self.assertTrue(isinstance(customer_revenue, pd.Series))
    
    def test_top_10_customers(self):
        customer_revenue = self.data.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        top_10_customers = customer_revenue.sort_values(ascending=False).head(10)
        self.assertEqual(len(top_10_customers), 10)

if __name__ == '__main__':
    unittest.main()
