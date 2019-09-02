import requests

def getUrl(url):
    req = requests.get(url)

    print("URL:", req.url)
    print("Encoding:", req.encoding)
    
    reqCode = req.status_code
    print("Status code:", reqCode)

    if reqCode == requests.codes.ok:
        reqHead = req.headers
        print("\nHeaders:")
        print(reqHead)

        print("\nHeaders again:")
        for item in reqHead:
            print(" ", item, ":", reqHead[item])
        
        print("\nText:")
        print(req.text)

        reqJson = req.json()
        print("\njson() :")
        print(reqJson)

        print("\nJSON again:")
        for item in reqJson:
            print(" ", item, ":", reqJson[item])

##        print("\nKeys:")
##        for key in reqJson.keys():
##            print(key)
##
##        print("\nValues:")
##        for value in reqJson.values():
##            print(value)


url = "https://my-json-server.typicode.com/goncerz/rep-json/db"
getUrl(url)
