# Python library for parsing various API's



'''python
Synthesizing 8/10 solutions

=======

class GoogleTrends:
    def __init__(self):
        pass

    def get_trends(self, keyword, start_date, end_date, geo, cat, output):
        url = f'https://trends.google.com/trends/api/widgetdata/multiline/csv?req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22{keyword}%22%2C%22geo%22%3A%22{geo}%22%2C%22time%22%3A%22{start_date}%20{end_date}%22%7D%5D%2C%22category%22%3A{cat}%2C%22property%22%3A%22%22%7D&token=APP6_UEAAAAAXZl5x5d5k5G8eW6aJy9aE9J1fQ8I4Wm1&tz=180'
        r = requests.get(url)
        if output == 'csv':
            return r.text
        elif output == 'json':
            return r.json()

=======

        def __init__(self):
        self.url = 'https://trends.google.com/trends/api/explore'
        self.headers = {
            'authority': 'trends.google.com',
            'method': 'GET',
            'path': '/trends/api/explore',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'NID=204=JcCkKjQ7B5f5U4x6U4Z6M0jKUu8M9k9DfzFyYKo7RzK0QaQxhPwZ3Gq3jK8ZVd9Xyf1S2QKl8H2u4D4mZ6U4V6U4Z6M0jKUu8M9k9DfzFyYKo7RzK0QaQxhPwZ3Gq3jK8ZVd9Xyf1S2QKl8H2u4D4mZ6U4V6U4Z6M0jKUu8M9k9DfzFyYKo7RzK0QaQxhPwZ3Gq3jK8ZVd9Xyf1S2QKl8H2u4D4mZ6U4V6U4Z6M0jKUu8M9k9DfzFyYKo7RzK0QaQxhPwZ3Gq3jK8ZVd9Xyf1S2QKl8H2u4D4mZ6U4V6U4Z6M0jKUu8M9k9DfzFyYKo7RzK0QaQxhPwZ3Gq3jK8ZVd9Xyf1S2QKl8H2u4D4mZ6U4V6U4Z6M0jKUu8M9k9

=======

class GoogleTrends:
    def __init__(self):
        self.url = 'https://trends.google.com/trends/api/explore'
        self.params = {
            'hl': 'en-US',
            'tz': 360,
            'req': {
                'comparisonItem': [
                    {
                        'keyword': 'bitcoin',
                        'geo': 'US',
                        'time': 'today 5-y'
                    }
                ],
                'category': 0,
                'property': ''
            },
            'token': '',
            'tz': 360
        }

    def get_trends(self, keyword, start_date, end_date, geo, cat, output):
        self.params['req']['comparisonItem'][0]['keyword'] = keyword
        self.params['req']['comparisonItem'][0]['geo'] = geo
        self.params['req']['comparisonItem'][0]['time'] = f'{start_date} {end_date}'
        self.params['req']['category'] = cat
        self.params['req']['property'] = ''

        r = requests.get(self.url, params=self.params)
        if output == 'json':
            return r.json()
        elif output == 'csv':
            pass
        else:
            return r.json()

=======

class GoogleTrends:
    def __init__(self):
        self.url = 'https://trends.google.com/trends/api/dailytrends'
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Dest': 'empty',
            'X-Client-Data': 'CI22yQEIo7bJAQjEtskBCKmdygEIqKPKAQi0p8oBCOKoygEI7KjKAQjxqMoBCL2oygEI8ajKAQ==',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://trends.google.com/trends/explore?date=2015-01-01%202022-09-12&geo=US&q=bitcoin',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    def get_trends(self, keyword, start_date, end_date, geo, cat, output):
        params = (
            ('hl', 'en-US'),
            ('tz', '-60'),
            ('req', '{"comparisonItem":[{"keyword":"'+keyword+'","geo":"'+geo+'","time":"'+start_date+' '+end_date+'"},{"keyword":"'+keyword+'","geo":"'+geo+'","time":"today 5-y"}],"category":'+str(cat)+',"property":""}'),
            ('tz', '-60'),
        )

        response = requests.get(self.url, headers=self.headers, params=params)
        if output == 'json':
            return response.json()
        elif output == 'csv':
            return response.content
        else:
            print('invalid output format')

=======

        def __init__(self):
        self.url = 'https://trends.google.com/trends/api/explore'
        self.params = {
            'hl': 'en-US',
            'tz': 360,
            'req': {'comparisonItem': [{'keyword': 'bitcoin', 'geo': 'US', 'time': 'today 5-y'}], 'category': 0, 'property': ''},
            'token': 'TOKEN',
            'tz': 360
        }
        self.headers = {
            'authority': 'trends.google.com',
            'method': 'GET',
            'path': '/trends/api/explore?hl=en-US&tz=360&req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22bitcoin%22%2C%22geo%22%3A%22US%22%2C%22time%22%3A%22today+5-y%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%7D&token=TOKEN&tz=360',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://trends.google.com/trends/explore?date=2015-01-01%202022-09-12&geo=US&q=bitcoin',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'x-client-data': 'CI22yQEIo7bJAQjEtskBCKmdygEIqK

=======

class GoogleTrends:
    def __init__(self):
        self.url = 'https://trends.google.com/trends/api/explore'
        self.payload = {
            'hl': 'en-US',
            'tz': 360,
            'req': {
                'comparisonItem': [
                    {
                        'keyword': '',
                        'geo': '',
                        'time': ''
                    }
                ],
                'category': 0,
                'property': ''
            },
            'token': '',
            'tz': 360
        }
        self.headers = {
            'authority': 'trends.google.com',
            'accept': 'application/json',
            'x-client-data': 'CIi2yQEIorbJAQjBtskBCKmdygEIqKPKAQioo8oBCO6oygEI7qjKAQ==',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://trends.google.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://trends.google.com/trends/explore?date=2015-01-01%202022-09-12&geo=US&q=bitcoin',
            'accept-language': 'en-US,en;q=0.9',
        }

    def get_trends(self, keyword, start_date, end_date, geo, cat, output='json'):
        self.payload['req']['comparisonItem'][0]['keyword'] = keyword
        self.payload['req']['comparisonItem'][0]['geo'] = geo
        self.payload['req']['comparisonItem'][0]['time'] = start_date + ' ' + end_date
        self.payload['req']['category'] = cat
        self.payload['req']['property'] = ''
        response = requests.post(self.url, headers=self.headers, json=self.payload)
        if output == 'json':
            return response.json()
        else:
            return response.content

=======

class GoogleTrends:
    def __init__(self):
        self.url = 'https://trends.google.com/trends/api/explore'
        self.params = {
            'hl':'en-US',
            'tz':360,
            'req':{
                'comparisonItem':[
                    {
                        'keyword':'bitcoin',
                        'geo':'US',
                        'time':'today 5-y'
                    }
                ],
                'category':0,
                'property':''
            }
        }

    def get_trends(self, keyword, start_date, end_date, geo, cat, output):
        self.params['req']['comparisonItem'][0]['keyword'] = keyword
        self.params['req']['comparisonItem'][0]['geo'] = geo
        self.params['req']['comparisonItem'][0]['time'] = f'{start_date} {end_date}'
        self.params['req']['category'] = cat
        r = requests.get(self.url, params=self.params)
        if output == 'json':
            return r.json()
        else:
            return r.text

=======

class GoogleTrends:
    def __init__(self):
        pass

    def get_trends(self, keyword, start_date, end_date, geo, cat, output):
        '''
        keyword: keyword to search for
        start_date: start date of the search
        end_date: end date of the search
        geo: country code
        cat: category
        output: format of the output (json or csv)
        '''
        # url to get the data
        url = 'https://trends.google.com/trends/api/explore'

        # parameters to get the data
        params = {
            'hl': 'en-US',
            'tz': '60',
            'req': {"comparisonItem":[{"keyword":keyword,"geo":geo,"time":start_date+' '+end_date}],"category":cat},
            'tz': '60',
        }

        # request the data
        r = requests.get(url, params=params).json()

        # save the data as csv or json file
        if output == 'csv':
            with open('trends.csv', 'w') as f:
                f.write(r['default']['timelineData'])
        elif output == 'json':
            return r

'''