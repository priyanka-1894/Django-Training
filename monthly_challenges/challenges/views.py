from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for atleast 20 minutes everyday!',
    'march': 'Holi Time',
    'april': 'Summer at peak',
    'may': 'Destroy',
    'june': 'Rain',
    'july': 'Strike',
    'august': 'Love',
    'september': 'Hate',
    'october': 'Undercover',
    'november': 'None',
    'december': 'Cut the cake!'
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "all_months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # error_response_data = render_to_string("404.html")
        # return HttpResponseNotFound(error_response_data)