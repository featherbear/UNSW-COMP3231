from bs4 import BeautifulSoup
import os

_, _, files = next(os.walk("."))
files = list(filter(lambda f: f.lower().endswith('html'), files))
files = sorted(files, key=lambda f: int(f[17:-12].strip()))

fragments = []

for f in files:
    with open(f, "r") as file:
        print(f"Parsing {f}...")
        soup = BeautifulSoup(file.read(), features="html.parser")
        z = soup.find('div', class_="formulation")
        clearElem  =z.find('div', class_="qtype_multichoice_clearchoice")
        if clearElem is not None:
            clearElem.decompose()
        for i in z.find_all('input'):
            i['disabled'] = 'true'
        fragments.append(str(z) + "<hr>")

with open("output.htm", "w") as file:
    file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="./assets/all.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saved Questions</title>
</head>
<body>{chr(10).join(fragments)}</body>
</html>
    """)