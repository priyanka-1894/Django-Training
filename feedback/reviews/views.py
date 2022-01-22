from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def review(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if (first_name == '' ) or (last_name == '') or (len(first_name) >= 100) or (len(last_name) >=100):
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        
        print(f"{ first_name } { last_name }")
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")
