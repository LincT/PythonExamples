# demonstrating api calls
import requests
import os


def apiToDictionary(city, state):
    # https://www.zipcodeapi.com/rest/<api_key>/city-zips.<format>/<city>/<state>
    apiKey = str(os.environ['zipApiKey'])  # this works if we're not trying to use environment variables.
    myFormat = "json"
    requestString = "https://www.zipcodeapi.com/rest/" + apiKey + "/city-zips." + myFormat + "/" + city + "/" + state
    response = (requests.get(requestString))
    return dict((response.json()))


def main():
    state = input("what 2 letter state should we look in? ")
    city = input("what city within " + state + " should we look for zip codes? ")
    print("Zip codes for " + city.capitalize() + ", " + state.upper() + ":")
    i = 0
    output = ""
    for line in apiToDictionary(city, state).get("zip_codes", ""):
        i += 1
        output += line + " "
        if i % 6 == 0:
            output += "\n"
    print(output)


main()
