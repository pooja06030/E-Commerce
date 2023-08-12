from django.shortcuts import redirect       # home.py me esko implement kiya he kibnda login he to hi index mtlab home page dikhega

def auth_Middleware(get_response):                   # ye ek decoratore he decoratore kya he to decoratore function ke under function hota he usko return krta he
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        if not request.session.get('customer'):
            return redirect('login')
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware