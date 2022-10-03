from django.shortcuts import render, redirect
from .models import Review


def index(request):
    reviews = Review.objects.all()

    return render(
        request,
        "reviews/index.html",
        {
            "reviews": reviews,
        },
    )


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)

    return redirect("reviews:index")


def new(request):
    return render(request, "reviews/new.html")


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    return render(
        request,
        "reviews/edit.html",
        {
            "review": review,
        },
    )


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    return render(
        request,
        "reviews/detail.html",
        {
            "review": review,
        },
    )


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")


def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content
    review.save()

    return redirect("reviews:detail", review.pk)
