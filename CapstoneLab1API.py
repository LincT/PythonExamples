# demonstrating api calls
import requests


def apiToDictionary(city, state):
    # https://www.zipcodeapi.com/rest/<api_key>/city-zips.<format>/<city>/<state>
    apiKey = "vY3eONi98Zyz4fxk6WVlw97V36UqtakcuOcY0RDvrAZykq9Jq5bgJeEKubFx6v8n"
    myFormat = "json"
    requestString = "https://www.zipcodeapi.com/rest/" + apiKey + "/city-zips." + myFormat + "/" + city + "/" + state
    # requests.get(requestString)
    response = (requests.get(requestString))
    return dict(response.json())


def main():
    state = input("what 2 letter state should we look in? ")
    city = input("what city within " + state + " should we look for zip codes? ")
    print("Zip codes for " + city.capitalize() + ", " + state.upper() + ":")
    i = 0
    output = ""
    for line in apiToDictionary(city, state).get("zip_codes", ""):
        i += 1
        output += line + " "
        if i % 5 == 0:
            output += "\n"
    print(output)


main()
