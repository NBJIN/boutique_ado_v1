from django.shortcuts import render


def view_bag(request):
    """ A view that renders the bag contens page """

    return render(request, 'bag/bag.html')
