import requests
import json

# URL
url = "https://jsonplaceholder.typicode.com/posts"

class http_and_web(object):
    def get_data():

        myResponse = requests.get(url)

        print ("Response code is " + str (myResponse.status_code))
        # For successful API call, response code will be 200 (OK)


        if(myResponse.ok):
            jData = json.loads(myResponse.content)
            print("The response contains {0} properties".format(len(jData)))
            print("\n")
            count = 1

            for item in jData:
                if (count > 5):
                    break
                #print(item)
                
                #with a little formatting
                print('{} {}'.format(item['id'], item['title']))

                count += 1
        else:
            # If response code is not ok (200), print the resulting http error code with description
           myResponse.raise_for_status()


    def post_data(post_url, id, title, body,userId=10 ):

        post_data = {
            'title': title,
            'body': body,
            'userId': userId
            }
        r = requests.post(post_url, data=post_data)
        myResponse = requests.post(url)
        print ("Response code is " + str (myResponse.status_code))
        
    post_data('https://jsonplaceholder.typicode.com/posts', 100, 'test1', 'body1')