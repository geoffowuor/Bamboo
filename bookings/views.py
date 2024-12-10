from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'index.html')






#admin pannel view
def admin(request):
    return render(request, 'admin.html')



#staff views
def staff(request):
    return render(request, 'staff.html')