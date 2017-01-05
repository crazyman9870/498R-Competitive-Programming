# -----FIRST-----
# Type the following into your command line after installing pip
# pip install --upgrade pip
# pip install requests

from requests import get
#   -- or --
# import requests


def main():
    """Example for using an external library from PyPI, install using pip
    """

    with open("index.html", "w+") as file:
        response = get("http://www.google.com")
        #   -- or --
        # response = requests.get("http://www.google.com")

        # Encode unicode response to uft-8 and write to new file
        file.write(response.text.encode('utf-8'))


if __name__ == "__main__":
    main()
