# optdens

## About

`optdens.py` is a python script that takes a list of experimental optical
densities as a `.csv` file and generates a statistics `.csv` output file and
plots a histogram of optical densities in a `.png` file.

## Dependencies

```matplotlib```

## Usage

The script can be called from the command line using:

```
optdens.py input_file.csv
```

The statistics file, histogram file and number of histogram bins can be
specified with the following arguments:

```
optdens.py inputfile.csv -s statistics.csv -p historgram.png -n 10
```

A list of arguments can be accessed by adding the `-h` flag.

## File formats

The input file must be a `.csv` file containing 3 comma-separated columns: the
index, the optical density and the sequence. Note that a header line is
expected.

The statistics file is a `.csv` file containing 4 comma-separated columns: the
sequence, the mean optical density, the maximum optical density and the minimum
optical density. A header with the column names is also added.

## Testing

The unit tests can be run using `python3 TestOpticalDensity.py`
