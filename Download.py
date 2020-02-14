import requests


def fromdrive():
    url = "https://drive.google.com/uc?export=download"
    file_id = '1fotL78NZaH_w6kTQvqWbFz9r3whDeQw_'

    session = requests.Session()
    response = session.get(url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    with open('db.csv', "wb") as f:
        for chunk in response.iter_content(10000):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def updatecheck(currentversion):
    url = "https://drive.google.com/uc?export=download"
    file_id = '1LCw-lcczPSOI64KGIkQV4G8KjiaB0G28'

    session = requests.Session()
    response = session.get(url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    latestversion = response.text
    if latestversion != currentversion:
        print('A new version of autoTRAX is available. Go to bit.ly/skyautotrax to get it!')
