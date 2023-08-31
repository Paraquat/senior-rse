#!/usr/bin/env python3

from OpticalDensity import OpticalDensity
import argparse
import sys

parser = argparse.ArgumentParser(description='Process amino acid optical density data',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('infile', default=None, help='Input file (.csv)')
parser.add_argument('-s', '--statistics', action='store', dest='statfile', default='stats.csv',
                    help='Output statistics file (.csv)')
parser.add_argument('-p', '--plot', action='store', dest='plotfile', default='plot.png',
                    help='Output histogram file (.png)')
parser.add_argument('-n', '--bins', action='store', dest='nbins', default=10,
                    help='Number of histogram bins')

cliopts = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

opt_dens = OpticalDensity(cliopts.infile)
opt_dens.write_statistics(cliopts.statfile)
opt_dens.plot_histogram(cliopts.nbins, cliopts.plotfile)
