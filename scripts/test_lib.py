import unittest
import lib  # Import the lib module


class TestLibFunctions(unittest.TestCase):
    def setUp(self):
        # Create a sample Polars DataFrame for testing
        data = {
            "2022 Population": [100, 200, 300, 400, 500],
            "Growth Rate": [1.1, 2.2, 3.3, 4.4, 5.5],
            "Area (km²)": [1000, 2000, 3000, 4000, 5000],
        }
        self.df = lib.pl.DataFrame(data)

    def test_readfile(self):
        # Test the readfile function
        data = lib.readfile("test_data.csv")  # Provide a sample CSV file path
        self.assertIsNotNone(data)  # Ensure that data is not None

    def test_descript_stat(self):
        # Test the descript_stat function
        try:
            lib.descript_stat(self.df)
        except Exception as e:
            self.fail(f"descript_stat function raised an exception: {e}")

    def test_histogram(self):
        # Test the histogram function
        try:
            lib.histogram(self.df)
        except Exception as e:
            self.fail(f"histogram function raised an exception: {e}")

    def test_boxplot(self):
        # Test the boxplot function
        try:
            lib.boxplot(self.df)
        except Exception as e:
            self.fail(f"boxplot function raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
