from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q #For Search
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    #Reset search(query), categories and filters
    query = None 
    categories = None
    sort = None
    direction = None

    #Query for search
    if request.GET:

        #Query for Filters
        if 'sort' in request.GET:
                    sortkey = request.GET['sort']
                    sort = sortkey
                    if sortkey == 'name':
                        sortkey = 'lower_name'
                        products = products.annotate(lower_name=Lower('name'))

                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        if direction == 'desc':
                            sortkey = f'-{sortkey}'
                    products = products.order_by(sortkey)
              
        #Query for Quategory
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        #Query for Search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
                
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)