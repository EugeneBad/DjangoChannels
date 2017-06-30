class InMiddle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.go = 'Yeah'
        print(request.go)
        return self.get_response(request)


class OutMiddle:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.go)
        return self.get_response(request)
