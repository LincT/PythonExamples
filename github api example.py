import requests

def wip():
    print()


def apiToDictionary(url, *args):
    request_string = url
    response = (requests.get(request_string))
    json = response.json()
    response.close()
    return dict(json)


def main():
    # docDict = {"text":"592da8d73b39d3e1f54304fedf7456b1", "markdown":"6a4cccf1c66c780e72264a9fbcb9d5fe"}
    # resultDict = apiToDictionary("https://api.github.com/gists/" + docDict.get("markdown"))
    # print(dict(dict(resultDict.get('files')).get('MineCTC: Rules.md')).get('content'))

    # resultDict = apiToDictionary("https://en.wikipedia.org/w/api.php?action=query&titles=Hebrew_alphabet&prop=revisions&rvprop=content&format=json&formatversion=2")
    # print(dict(resultDict["query"]))
    wip()

if __name__ == '__main__':
    main()
