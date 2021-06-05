from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name='HTML'
    dest1.desc='Pythonframework that helpsto make web pages dynamic and make database loading easy'
    dest1.prices='Rs. 500'
    dest1.img='logo_html.png'
    

    dest2 = Destination()
    dest2.name='Angular'
    dest2.desc='Framework for frontend'
    dest2.prices='Rs. 550'
    dest2.img='logo_css.png'
    dest2.offer= True
     
    dest3 = Destination()
    dest3.name='Django'
    dest3.desc='Framework '
    dest3.prices='Rs. 660'
    dest3.img='logo_brush.png'
    dest3.offer= False

    dests=[dest2,dest3]

    destss=Destination.objects.all()

    return render(request,'index.html',{'dests':dests,'dest1':dest1,'destss':destss})