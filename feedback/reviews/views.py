from tempfile import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })
    
#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    # field = "__all__"
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
def update_review(request, id):
    if request.method == 'POST':
        existing_entry = Review.objects.get(pk=id)
        form = ReviewForm(request.POST, instance=existing_entry)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This work!"
        return context

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["all_reviews"] = Review.objects.all()
#         return context

# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["review"] = Review.objects.get(pk=kwargs["id"])
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "all_reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     return base_query.filter(rating__gt=4)

class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review