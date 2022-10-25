from re import M
from django.shortcuts import render, redirect
from .models import Appointment, Box, Material
from .forms import DataForm_v1, DataForm_v2
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")


def appointment_mobile_v1(request):
    """Basic solution"""
    form = DataForm_v1(request.POST)
    if form.is_valid():
        new_appointment = form.save(commit=False)
        new_appointment.box = Box.objects.filter(
            code=form.cleaned_data["get_box"]
        ).first()
        new_appointment.material = Material.objects.filter(
            code=form.cleaned_data["get_material"]
        ).first()
        new_appointment.created_by = request.user
        new_appointment.save()

        return redirect("/")
    return render(request, "form.html", {"form": form})


def appointment_mobile_v2(request):
    """Advanced solution"""
    form = DataForm_v2(request.POST, user=request.user)
    if request.method == "POST":
        if form.is_valid():
            new_appointment = form.save()

            return redirect("/")
    return render(request, "form.html", {"form": form})


def pagelogout(request):
    if request.method == "POST":
        logout(request)

    return redirect("/")
