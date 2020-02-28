from io import StringIO

import requests
import pandas as pd
from bs4 import BeautifulSoup

SUMMARY_URL = "https://www.ebi.ac.uk/Tools/hmmer/results/90350804-59A2-11EA-899E-10AFF75AEC3D/score"
DOWNLOAD_URL_FORMAT = "https://www.ebi.ac.uk/Tools/hmmer/download/90350804-59A2-11EA-899E-10AFF75AEC3D.{rownum}/score?format=tsv"
RESULT_CSV = "data/hmmer_data.csv"


def process_tsv(text):
    # ebi unite some row in table, so we should split them by ourself
    data = text.split("\n")
    result = []
    tab = "\t"
    for i, d in enumerate(data):
        row = d.split("\t")
        for i in range(1, len(row), 12):
            result.append(f"{row[0]}\t{tab.join(row[i: i + 12])}")
    return "\n".join(result)


def merge_results(names):
    result = pd.DataFrame()
    for rownum, name in enumerate(names, 1):
        print(name)
        data = requests.get(DOWNLOAD_URL_FORMAT.format(rownum=rownum))
        if data.status_code == 200:  # server returns 500 for no match
            data = process_tsv(data.text)
            tsv = StringIO(data)
            data = pd.read_csv(tsv, sep="\t")
            data["query_name"] = name
            result = result.append(data)
    result.reset_index(inplace=True)
    result.to_csv(RESULT_CSV)


def get_query_names():
    result = []
    data = requests.get(SUMMARY_URL)
    data = BeautifulSoup(data.text, features="html.parser")
    for tr in data.body.table.tbody.find_all("tr"):
        name = tr.find_all("td")[1].text
        result.append(name)
    return result


if __name__ == '__main__':
    names = get_query_names()
    merge_results(names)
