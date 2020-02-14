import re

import pandas as pd
import requests

data = pd.read_csv("data/GSE71620.csv")
characteristics = re.compile(r'<tr valign="top"><td nowrap>Characteristics</td>(.*\n.*\n.*)</tr>')
result = pd.DataFrame()
processed = None

for sample_id in data["sample"]:
    if sample_id == processed:
        continue
    metadata = requests.get(f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={sample_id}").text
    metadata = re.findall(characteristics, metadata)
    assert len(metadata) == 1, f"there should be only one characteristics fiels, but {len(metadata)} was found for {sample_id}"
    metadata = metadata[0].split("<br>")
    metadata = dict(d.split(": ") for d in metadata[1: -1])
    metadata["sample"] = sample_id
    result = result.append(metadata, ignore_index=True)
    print(f"processing {sample_id}")
    processed = sample_id

result = pd.merge(data, result, on="sample")
result.to_csv("data/GSE71620.csv")
