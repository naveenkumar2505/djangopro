from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import FeedbackData
import datetime as dt
time=dt.datetime.now()
def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')
            data=FeedbackData(
                name=name,
                rating=rating,
                time=time,
                feedback=feedback
            )
            name=name.title()
            data.save()
            return redirect('/feedback/')
    else:
        fao=FeedbackData.objects.all()
        form=FeedbackForm()
        return render(request,'feedback.html',{'form':form,'fao':fao})