import unittest
from cord1 import Coord, line_length


class TestLineLength(unittest.TestCase):
    def test_ut1(self):
        a1 = Coord(1, 2)
        a2 = Coord(2, 2)
        self.assertEqual(line_length(a1, a2), 5)

    def test_ut2(self):
        a1 = Coord(1, 2)
        a2 = Coord(2, 2)
        self.assertEqual(line_length(a1, a2), 5)

    def test_ut3(self):
        a1 = Coord(2, 2)
        a2 = Coord(-2, 2)
        self.assertEqual(line_length(a1, a2), 4)

    def test_ut4(self):
        a1 = Coord(2, 2)
        a2 = Coord(4, 2)
        self.assertEqual(line_length(a1, a2), 7.211102550927978)


    def test_ut5(self):
        a1 = Coord(2, 2)
        a2 = Coord(0, 2)
        self.assertEqual(line_length(a1, a2), 4.47213595499958)

    def test_ut6(self):
        a1 = Coord(2, 2)
        a2 = Coord(2, 4)
        self.assertEqual(line_length(a1, a2), 7.211102550927978)

    def test_ut7(self):
        a1 = Coord(2, 2)
        a2 = Coord(2, 0)
        self.assertEqual(line_length(a1, a2), 4.47213595499958)


    def test_ut8(self):
        a1 = Coord(2, 2)
        a2 = Coord(3, 4)
        self.assertEqual(line_length(a1, a2), 7.810249675906654)

    def test_ut9(self):
        a1 = Coord(2, 2)
        a2 = Coord(0, 0)
        self.assertEqual(line_length(a1, a2), 2.8284271247461903)

    def test_ut10(self):
        a1 = Coord(2, 2)
        a2 = Coord(-2, 5)
        self.assertEqual(line_length(a1, a2), 7.0)

    def test_ut11(self):
        a1 = Coord(2, 2)
        a2 = Coord(-2, -4)
        self.assertEqual(line_length(a1, a2), 2.0)


    def test_ut12(self):
        a1 = Coord(2, 2)
        a2 = Coord(-4, -4)
        self.assertEqual(line_length(a1, a2), 2.8284271247461903)

    def test_ut13(self):
        a1 = Coord(-3, -3)
        a2 = Coord(-4, -4)
        self.assertEqual(line_length(a1, a2), 9.899494936611665)

    def test_ut14(self):
        a1 = Coord(2, 2)
        a2 = Coord(2, -4)
        self.assertEqual(line_length(a1, a2), 4.47213595499958)

    def test_ut15(self):
        a1 = Coord(2, 2)
        a2 = Coord(2, -4)
        self.assertEqual(line_length(a1, a2), 4.47213595499958)










