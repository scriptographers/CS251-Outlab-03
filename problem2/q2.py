import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input",  "-in", type=str, required=True)
parser.add_argument("--output", "-out", type=str, required=True)

args = parser.parse_args()
infile  = args.input
outfile = args.output

with open(infile, 'r') as inpf:
    inpath  = inpf.readline()
    outpath = os.path.realpath(inpath)
    with open(outfile, 'w') as outf:
        outf.write(outpath)

