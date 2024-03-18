from django.shortcuts import render,HttpResponse
from home.models import BookTable
# Create your views here.
def home(request):
    return render(request,'index.html')

def bookTable(request):
    if request.method == 'POST':
        print("entering post")
        email=request.POST['email']
        number_guest=request.POST['number_guest']
        time=request.POST['time']
        date=request.POST['date']
        print("printing here",email,number_guest,time,date)
        if email and number_guest and time and date:
            bookTable=BookTable.objects.create(email=email,number_guest=number_guest,time=time,date=date)
            try:
                bookTable.save()
            except:
                print("Please book table again something went wrong")
        return render(request,'bookTable.html')
       