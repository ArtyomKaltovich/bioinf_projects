import urllib
import json

import pandas as pd
from bs4 import BeautifulSoup

RESULTS = r"C:\Users\artem\Downloads\Telegram Desktop\result.txt"
GENE_INFO = r"data\results.tsv"
OUTPUT_PATH = r"data\gene_info.csv"


def main(output_path):
    data = read_data()
    data["description"] = data["detail_url"].apply(request_and_parse_data)
    data.to_csv(output_path)


def request_and_parse_data(link):
    f = urllib.request.urlopen(link)
    details = f.read().decode()
    soup = BeautifulSoup(details, 'html.parser')
    text = soup.head.script.text
    text = text[text.find("locusData: ") + 11: text.find(",\n        tabs:")]
    parsed = json.loads(text)
    return parsed["description"]


def read_data():
    data = pd.read_csv(RESULTS, sep="\t").head(50).drop("Unnamed: 0", axis=1)
    data["id"] = data["id"].str[5:]
    gene_info = pd.read_csv(GENE_INFO, sep="\t", header=None)
    gene_info.columns = ["Gene Primary DBID", "id", "Gene Organism Short Name",
                         "Gene Standard Name", "Gene Name"]
    data = pd.merge(data, gene_info, on="id")
    data["detail_url"] = "https://www.yeastgenome.org/locus/" + data["Gene Primary DBID"]
    return data


if __name__ == '__main__':
    main(OUTPUT_PATH)
