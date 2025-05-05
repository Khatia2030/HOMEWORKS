import unittest
from module import process_orders

class TestProcessOrders(unittest.TestCase):

    def test_product_not_in_inventory(self):
        orders = [{"product": "banana", "quantity": 3}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)

        self.assertIn("Product 'banana' not found in inventory", str(context.exception))

    def test_not_enough_stock(self):
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"apple": 2}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)

        self.assertIn("Not enough stock for 'apple'", str(context.exception))

    def test_successful_order_and_inventory_update(self):
        orders = [{"product": "apple", "quantity": 3}]
        inventory = {"apple": 5}

        result = process_orders(orders, inventory)

        self.assertEqual(result, orders)
        self.assertEqual(inventory["apple"], 2)  # 5 - 3 = 2

if __name__ == '__main__':
    unittest.main()