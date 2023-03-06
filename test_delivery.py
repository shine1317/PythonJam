import unittest

from datetime import datetime, timedelta

from delivery_date import (
    is_holiday,
    is_sunday,
    calculate_delivery_date
)

class TestDeliveryDate(unittest.TestCase):
 
    def setUp(self):
        self.purchase_date = datetime.now()
 
    def test_purchase_date(self):
        self.assertTrue(self.purchase_date)
    
 
    def test__delivery_date_after_three_holidays_and_a_sunday__is_7_days_after_purchase_date(self):
        purchase_date = datetime(2023, 2, 1)
        # holiday   feb 2
        # holiday   feb 4
        # sunday    feb 5
        # holiday   feb 6
        expected_delivery_date = datetime(2023, 2, 8)
        actual_delivery_date = calculate_delivery_date(purchase_date)
 
        self.assertEqual(expected_delivery_date, actual_delivery_date)
 
if __name__ == '__main__':
    unittest.main()  # pragma: no cover