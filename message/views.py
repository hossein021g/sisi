from django.views.generic import ListView
from .models import message
#def messageviews(request):
  #  return render(request, 'home.html')

class Messageview(ListView):
    model = message
    template_name ='home.html'
