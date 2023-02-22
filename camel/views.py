from django.shortcuts import render

def home(request,):

    if request.method == 'POST':

        tok = request.POST.get("tok", False)
        sa = request.POST.get("sa", False)
        did = request.POST.get("did", False)
        tagging = request.POST.get("tagging", False)
        morphological = request.POST.get("morphological", False)
        main = request.POST.get("main", None)
        result = request.POST.get("result", None)

    else:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'home.html', context)