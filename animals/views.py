from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from animals.models import Animal


class AnimalView(View):
    @staticmethod
    def get(request):
        animals = Animal.objects.all()
        return render(request, "animals/base.html", {"animals": animals})

    @staticmethod
    def post(request):
        pk = request.POST.get("id")
        name = request.POST.get("name")
        species = request.POST.get("species")
        action = request.POST.get("action", "EDIT")

        if pk is not None:
            try:
                pk = int(pk)
            except ValueError:
                raise Exception

            try:
                animal = Animal.objects.get(id=pk)
            except Animal.DoesNotExist:
                messages.warning(request, f"Animal with ID [{pk}] not found.")
                return redirect("animals")

            if action == "DELETE":
                animal.delete()
            else:
                animal.name = name
                animal.save()

            return redirect("animals")

        if not all([name, species]):
            raise Exception("Name and species are required.")

        Animal.objects.create(name=name, species=species)
        return redirect("animals")
