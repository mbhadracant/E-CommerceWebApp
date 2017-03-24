from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import User
from .serializer import UserSerializer

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            serializer = UserSerializer(user, many=False)
            request.session['account'] = serializer.data
            return HttpResponseRedirect('/')
        except User.DoesNotExist:
            return HttpResponseRedirect('/account/error')
    else:
        raise Http404


