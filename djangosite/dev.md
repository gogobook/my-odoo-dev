```py
from django.contrib.auth import authenticate, login, logout
 
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
    # Return an 'invalid login' error message.
        ...
 
def logout_view(request):
    logout(request)
    # Redirect to a success page.
```
客製登入頁時使用。