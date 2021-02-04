import requests as rq

try:
    response = rq.get("https://www.google.com/")

    if response.ok:
        print("Internet Access: Yes\nReason: %s" % response.reason)

    else:
        print("Internet Access: No\nReason: %s", response.reason)
except:
    print("No internet connection")

try:
    input("Press enter to exit..")
except ValueError:
    print("Exiting")