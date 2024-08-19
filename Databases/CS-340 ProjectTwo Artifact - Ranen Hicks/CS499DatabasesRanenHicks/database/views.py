from django.shortcuts import render

# (Mashutin, 2024; Writing Your First Django App, Part 1, n.d.), Renders the first database with button to datatable
def showLink(request):
    return render(request, "templates/homepage.html")

