import requests
import re

URL = r"https://wolfpsort.hgc.jp/results/aKC99f49e81a7e04690c90d3c2176bf8494.html"
DETAILS_FILE = "data/details_urls.csv"


if __name__ == '__main__':
    data = requests.get(URL)
    data = data.text
    with open(DETAILS_FILE, "w") as file:
        file.write("id,details_url,details_id,site,distance,align_url,identity,comments\n")
        for match in re.finditer('(g\\d+\\.t1) <A href="([\\w\\.#]+)"', data):
            id_ = match.group(1)
            link = "https://wolfpsort.hgc.jp/results/" + match.group(2)
            print(id_, link)
            details = requests.get(link).text
            details = details[:details.find('Normalized Feature Values')].split('<TR>')
            maximal_identity = 0.0
            max_elem = None
            for d in details:
                if d.startswith('<TD nowrap>'):
                    for match in re.finditer('<TD nowrap>(.+)<TD nowrap>(.+)</TD><TD nowrap>(.+)</TD>\n'
                                             '<TD nowrap><A.*href="(.*)">(.+)%</A></TD>\n'
                                             '<TD nowrap>(.+)</TD>', d, flags=re.DOTALL):
                        item = match.groups()
                        if float(item[4]) > maximal_identity:
                            maximal_identity = float(item[4])
                            max_elem = item
            row = [id_, link]
            row.extend(max_elem)
            row[5] = r'https://wolfpsort.hgc.jp/results/' + row[5]
            row[-1] = row[-1].replace(",", "\,")
            file.write(','.join(row) + '\n')