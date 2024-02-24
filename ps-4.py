import json
import pandas
import requests 

def get_capital(country):  
    url = "https://countriesnow.space/api/v0.1/countries/capital"

    payload = json.dumps({
    "country": country
    })

    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

def process_excel(filename):
    dataframe = pandas.read_excel(filename)
    countries = dataframe["Country (or dependent territory)"]
    cap_cntry = {}
    for idx, country in enumerate(countries):
        if isinstance(country, str):
            capital = get_capital(country)
            if not capital.get("error", True):
                capital = capital.get("data", {}).get("capital", "")
                print(str(idx) + ' - ' + country + '-' + capital)
                cap_cntry.update({country : capital})
            else:
                cap_cntry.update({country: ""})
        else:
            cap_cntry.update({country: ""})
                    
    dataframe['Capital'] = [cap_cntry.get(country) for country in dataframe["Country (or dependent territory)"]]
    return dataframe

def df_to_excel(df, new_excel_path):
    return df.to_excel(new_excel_path, index=False)

df = process_excel("src\q4_country_list.xlsx")
excel = df_to_excel(df, "src\q4_country_list.xlsx")