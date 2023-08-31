import matplotlib.pyplot as plt

class AminoAcid:
    """
    Container for the a row of the input csv file, an indexed sequence with
    an optical density.
    """

    def __init__(self, index, optical_density, sequence):
        """
        Arguments:
        index (str) -- unique ID for the experiment
        optical_density (float) -- The experimentally determined optical density
        sequence (str) -- the sequence of the amino acid
        """

        self.index = index
        self.optical_density = optical_density
        self.sequence = sequence


class OpticalDensity:
    """
    Process a set of experimental results. Read the input csv file, and
    generate an optical density histogram and statistics csv file
    """

    def __init__(self, input_filename):
        """
        Arguments:
        input_filename (str) -- name of the csv file to read.

        .csv format (including header):

        index,optical_density,amino_acid_sequence
        A01,0.8,GFTFSSYF
        A02,1.3,GFTFSNYA
        ...
        """

        self.sequences = []
        with open(input_filename, 'r') as infile:
            next(infile) # skip the header
            for line in infile:
                index, optical_density, sequence = line.split(',')
                self.sequences.append(
                    AminoAcid(index.strip(), float(optical_density.strip()), sequence.strip()))
        # sort the list by sequence
        self.sequences = sorted(self.sequences, key=lambda x: x.sequence)

    def plot_histogram(self, nbins, output_filename, plot=True):
        """
        Plot histogram of optical densities and output to png file.

        Arguments:
        nbins (int) -- number of histogram bins
        output_filename (str) -- name of the output png file
        ...
        """

        data = [amino_acid.optical_density for amino_acid in self.sequences]
        histogram = plt.hist(data, bins=nbins, histtype='step')
        plt.title('Optical density histogram', fontsize=16)
        plt.xlabel('Optical density', fontsize=16)
        plt.ylabel('Frequency', fontsize=16)
        plt.tight_layout()
        if plot:
            plt.savefig(output_filename)
        return histogram

    def get_statistics(self):
        """
        Compute mean, maximum and minimum of optical densities per (non-unique)
        sequence.
        """

        sequence_dict = {}
        for seq in self.sequences:
            if seq.sequence in sequence_dict:
                sequence_dict[seq.sequence].append(seq.optical_density)
            else:
                sequence_dict[seq.sequence] = [seq.optical_density,]

        stats = {}
        for (key, value) in sequence_dict.items():
            minimum = min(value)
            maximum = max(value)
            mean = sum(value) / len(value)
            stats[key] = (mean, maximum, minimum)
        return stats

    def write_statistics(self, output_filename):
        """
        Write statistics from get_statistics to file

        Arguments:
        output_filename (str) -- name of the output csv file

        .csv format (including header)

        amino_acid_sequence,mean_optical_density,max_optical_density,min_optical_density
        GFAFSSYD,1.0,1.2,0.9
        GFAFSSYW,0.8,0.8,0.8
        ...
        """

        with open(output_filename, 'w') as outfile:
            stats = self.get_statistics()
            # write header
            outfile.write(
                "amino_acid_sequence,mean_optical_density,max_optical_density,min_optical_density\n")

            for (key, value) in stats.items():
                outfile.write(f'{key},{value[0]:.1f},{value[1]},{value[2]}\n')


if __name__ == '__main__':
    opt_dens = OpticalDensity("example_data/input_data.csv")
    opt_dens.write_statistics("stats")
    opt_dens.plot_histogram(10, "plot.png")

