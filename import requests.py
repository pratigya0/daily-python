import requests
from bs4 import BeautifulSoup

def decode_secret_message(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")

    char_map = {}

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        x_val = cols[0].get_text(strip=True)
        char  = cols[1].get_text(strip=True)
        y_val = cols[2].get_text(strip=True)

        if not x_val.lstrip('-').isdigit() or not y_val.lstrip('-').isdigit():
            continue

        x = int(x_val)
        y = int(y_val)
        char_map[(x, y)] = char

    if not char_map:
        print("No data found.")
        return

    max_x = max(x for x, y in char_map)
    max_y = max(y for x, y in char_map)

    for y in range(max_y + 1):
        row_str = ""
        for x in range(max_x + 1):
            row_str += char_map.get((x, y), " ")
        print(row_str)


# URL goes HERE — outside the function
url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
decode_secret_message(url)