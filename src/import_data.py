# Your code here

import ssl
import certifi
import urllib.request

context = ssl.create_default_context(cafile=certifi.where())

# Realiza la solicitud usando el contexto SSL personalizado

url = "https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv"
response = urllib.request.urlopen(url,context=context)
data = response.read()
csv_data = data.decode('utf-8')

with open('AB_NYC_2019.csv', 'w', encoding='utf-8') as file: 
    file.write(csv_data) 
print("CSV file has been saved successfully.")