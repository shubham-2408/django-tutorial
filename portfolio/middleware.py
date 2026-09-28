class Mycustommiddleware():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("Source of api is ",request.META['HTTP_USER_AGENT'])
        return response 