from datetime import datetime
from django.shortcuts import render

# Create your views here.

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Tryannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops"
        ],
        "now": datetime.now(),
    }

    return render(request, name + ".html", data)