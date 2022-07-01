#!/usr/bin/env	python3

import os
import sys
import argparse
import textwrap
from Bio import SeqIO, AlignIO
import pandas

def hello(what):
  print("hello ", str(what))

hello(sys.argv[1])
