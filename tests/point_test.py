import unittest

from project.point import Point


class TestPoint(unittest.TestCase):

    def test_point_should_have_0_0_cords(self):
        point = Point()
        self.assertEqual(point._x_axis, 0)
        self.assertEqual(point._x_axis, 0)
    def test_point_should_have_1_1_cords_after_given_cords(self):
        point = Point(1,1)
        self.assertEqual(point._x_axis, 1)
        self.assertEqual(point._y_axis, 1)
    def test_point_should_raise_type_error_during_init_with_str_type(self):
        self.assertRaises(TypeError, Point, "jeden","czternascie")
        self.assertRaises(TypeError, Point, 1, "czternascie")
        self.assertRaises(TypeError, Point, "jeden", 14)
    def test_point_should_raise_value_error_during_init_with_wrong_xcord(self):
        self.assertRaises(ValueError, Point, -1, 10)
        self.assertRaises(ValueError, Point, 21, 10)
    def test_point_should_raise_value_error_during_init_with_wrong_ycord(self):
        self.assertRaises(ValueError, Point, 1, -1)
        self.assertRaises(ValueError, Point, 1, 16)