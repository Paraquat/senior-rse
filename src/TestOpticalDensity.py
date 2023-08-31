import unittest
from OpticalDensity import OpticalDensity

class TestOpticalDensityMethods(unittest.TestCase):
    """
    Unit tests for class OpticalDensity
    """

    def test_stats(self):
        input_file= '../example_data/input_data.csv'
        reference_file = '../example_data/output_data.csv'
        opt_dens = OpticalDensity(input_file)
        stats = opt_dens.get_statistics();

        # read the reference output
        with open(reference_file, 'r') as infile:
            next(infile)
            for line in infile:
                sequence, mean, maximum, minimum = line.strip().split(',')
                mean = float(mean)
                maximum = float(maximum)
                minimum = float(minimum)
                self.assertAlmostEqual(mean, stats[sequence][0], delta=0.1)
                self.assertAlmostEqual(maximum, stats[sequence][1], delta=0.1)
                self.assertAlmostEqual(minimum, stats[sequence][2], delta=0.1)


    def test_histogram(self):
        input_file= '../example_data/input_data.csv'
        opt_dens = OpticalDensity(input_file)
        histogram = opt_dens.plot_histogram(10, "dummy", False)[0]
        reference_data = [6, 2, 8, 6, 4, 22, 3, 20, 17, 8]
        for i, count in enumerate(histogram):
            self.assertEqual(reference_data[i], histogram[i])


if __name__ == '__main__':
    unittest.main()
