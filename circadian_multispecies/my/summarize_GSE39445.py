import os
import re
import csv
import requests

import pandas as pd

CIRCADIAN_GENES = "ARNTL", "NR1D1", "PER3"
FIELDS = ("sample_id", "sleepprotocol", "hoursawake", "circadianphase") + CIRCADIAN_GENES


def main():
    with open("data/GSE39445.csv", "w") as result:
        result = csv.DictWriter(result, FIELDS)
        result.writeheader()
        dir = r"/run/media/my/New Volume/temp/GSE39445_RAW/"
        os.chdir(dir)
        files = os.listdir(dir)
        files.sort()
        characteristics = re.compile(r'<tr valign="top"><td nowrap>Characteristics</td>(.*\n.*\n.*)</tr>')
        #files = files[:13]
        n = len(files)
        for i, f in enumerate(files, 1):
            fields = get_metadata(characteristics, f)
            fields.update(read_expressions(f))
            result.writerow(fields)
            print(f"{i}/{n}")


def get_metadata(characteristics, f):
    sample_id, patiend, *_ = f.split("_")
    metadata = requests.get(f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={sample_id}").text
    metadata = re.findall(characteristics, metadata)
    assert len(
        metadata) == 1, f"there should be only one characteristics fiels, but {len(metadata)} was found for {sample_id}"
    metadata = metadata[0].split("<br>")
    #print(metadata)
    *_, sleepprotocol = metadata[-6].partition(": ")
    *_, hoursawake = metadata[-4].partition(": ")
    *_, circadianphase = metadata[-2].partition(": ")
    return dict(sample_id=sample_id, sleepprotocol=sleepprotocol, hoursawake=hoursawake, circadianphase=circadianphase)


def read_expressions(path):
    data = pd.read_csv(path, skiprows=9, sep="\t")
    return {gene: data[data["GeneName"] == gene]["gMedianSignal"].sum() for gene in CIRCADIAN_GENES}


if __name__ == '__main__':
    main()
