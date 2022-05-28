import requests
from pythonTimer import Timer


def main():
    t = Timer()
    t.start()
    r = requests.get("https://api.github.com/users/Obuya-Nyang")
    t.stop()
    print(r.url)


# async def trive():


if __name__ == "__main__":
    main()
