#######################################################
#                                                     #
# Author: Shad Hasan                                  #
# Version: 1.0                                        #
# Module: http_api provides api to interact with url  #
#         and performs verification                   #
#                                                     #
#######################################################
import requests
import urlparse
import json

class http_api:

    def __init__(self, base_url):
        '''
        http_api: constructor takes base url which is constant url pointing to an application in a server
        usage: http_api("https://api.punkapi.com/v2/")
        '''
        self.base_url = base_url


    def get_response(self, method, rest_url):
        '''
        get_response: It takes http method and relative
        usage : api.get_reponse("Get", 
        '''
        url = urlparse.urljoin(self.base_url, rest_url)
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url)
        elif method.upper() == "DELETE":
            response = requests.delete(url)
        elif method.upper() == "PUT":
            response = requests.put(url)
        elif method.upper() == "PATCH":
            response = requests.patch(url)
        else:
            response = None
            print("Invalid method")
        return response

    def verify_response(self, response, content_type="raw", verify_as="equal", expected_status_code=200, expected_content=None):
        '''
        verify_response: It verify http response received via get_response. By default it checks on status_code, 200
        and it also takes expected content and type of content

        verify_as: It takes an arguument equal, less, greater, expression, regex and use it to compare
        
        usage: 
        '''
        if type(response) is requests.models.Response:
            if expected_content is not None:
                if content_type == "raw":
                    content = response.content
                elif content_type == "json":
                    content=json.loads(response.content)

                try:
                    if verify_as == "equal":
                        assert content == expected_content, "Failed! Expected content: {}, Found content : {}".format(expected_content, content)
                        print("Verified successfully! Expected content: {}, Found content : {}".format(expected_content, content))
                    elif verify_as == "expression":
                        expression = expected_content.format(content)
                        evaluation = eval(expression)
                        assert evaluation, "Failed! Expression : {}, Evaluation : {}".format(expression, evaluation)
                        print("Verified successfully! Expression : {}, Evaluation : {}".format(expression, evaluation))
                    else:
                        print("Either, verify_as is not implemented or invalid")
                except Exception as e:
                    print("At least content verification failed due to {}".format(e))
            else:
                pass
            
            assert response.status_code == expected_status_code, "By default expected_status_code is 200 else pass argument\
                expected_status_code= , Expected: {}, Found: {}".format(expected_status_code, response.status_code)
            print("Status code verified successfully! Expected: {}, Found: {}".format(expected_status_code, response.status_code))

        else:
            assert type(x) is requests.models.Response,\
            "Type Expected : {}, Got: {}".format(requests.models.Response, type(x))


if __name__ == "__main__":

    httpApi = http_api("https://api.punkapi.com/v2/")
    response = httpApi.get_response("Get", "beers?page=1&per_page=80")
    httpApi.verify_response(response, content_type="json", verify_as="expression", expected_status_code=200, expected_content="len({})==90")

