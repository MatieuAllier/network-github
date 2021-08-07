import requests
import json


if __name__ == '__main__':
    # Extract the color data from linguist repository
    url = "https://raw.github.com/github/linguist/master/lib/linguist/languages.yml"
    r = requests.get(url)
    text = r.text
    # Need to split all line of the data
    text = text.split('---\n')[1]
    list_splits = text.split('\n')
    dict_of_colors = {}
    # Remove an empty string at the end
    list_splits.pop()
    list_array = []
    # To rearrange each language with its paramaters, I loop inside the split 
    # and check if the line is a parameter line (start with a ' ') or line which 
    # define the language
    while list_splits != []:
        array = []
        while (list_splits[-1][0] == ' '):
            array.insert(0, list_splits.pop())
        array.insert(0, list_splits.pop())
        list_array.append(array)
    # One I have all the language and their parameter I extract their color and their extensions  
    for array in list_array:
        try:
            extensions = [_.replace('  - ".', '').replace('"', '') for _ in array if '  - ".' in  _]
            color = [_.replace(' color: ', '') for _ in array if ' color: ' in _][0].replace(' "', '').replace('"', '')
            dict_of_colors.update({extension : color for extension in extensions})
        except Exception:
            pass
    with open('ressources/colors.json', 'w') as fp:
        json.dump(dict_of_colors, fp)