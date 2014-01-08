import os
import sys
from pana.hapassoc.records import HapAssocResRec


def filter_assoc_hap(file_name):
    assoc_hap_file = open(file_name)
    sys.stdout.write(assoc_hap_file.readline())
    for line in assoc_hap_file:
        assoc_hap_rec = HapAssocResRec(line.strip().split())
        if assoc_hap_rec.valid_window:
            sys.stdout.write(line)
