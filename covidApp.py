## Libraries
from flask import Flask, render_template, request
import os
import requests
import pandas as pd

## Creating Instance
covid_app = Flask(__name__)


## Home Page
@covid_app.route('/', methods=["POST", "GET"])
def covid_home_page():
    global covidinfo
    if request.method == "POST":
        country = request.form["country"]  # Asking for input from user & saving it in country variable
        print("You want covid data for : ", country)

        # Fetching data from covid api and storing it in variable response_json
        url = "https://api.covid19api.com/summary"
        response_json = requests.get(url).json()
        print(response_json)

        total_countries = response_json['Countries']

        # Fetching data of country for which we want data
        for i in range(len(total_countries)):
            if total_countries[i]['Country'] == country:
                country_stats = total_countries[i]
                print(country_stats)

                covid_data = {
                    'TotalConfirmed': country_stats['TotalConfirmed'],
                    'TotalDeaths': country_stats['TotalDeaths']
                }

                return render_template("covid_home.html", covidinfo=covid_data)

            else:
                return render_template("covid_home.html")

    else:
        return render_template("covid_home.html")


# port = int(os.environ.get("PORT",5000))
#
# if __name__ == "__main__":
#     covid_app.run(port=port)

covid_app.run()


