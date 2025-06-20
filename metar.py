import urllib.request
def get_metar_data(icao):
  with urllib.request.urlopen(f"https://aviationweather.gov/api/data/metar?ids={icao}&hours=0") as response:
    html = response.read().decode("utf-8")
  remove_new_line=html.replace("\n","")
  remove_first_part=remove_new_line.replace("<html><head><link rel="stylesheet" href="resource://content-accessible/plaintext.css"></head><body><pre>","")
  metar=remove_first_part.replace("</pre></body></html>","")
  return metar
icao=input("ICAO: ")
print(get_metar_data(icao))

