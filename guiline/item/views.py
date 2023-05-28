from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category


# Browse
def browseItems(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_id:
        items = items.filter(category_id=category_id)
    
    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    }
    
    return render(request, 'item/browse_items.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]
    
    context = {
        'item': item,
        'related_items':related_items
    }
    return render(request, 'item/detail.html', context)

@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            
            return redirect('item:detail', pk=new_item.id)
    else:
        form = NewItemForm()
    
    title = "Add Item"
    context = {
        'form': form,
        'title': title
    }
    
    return render(request, 'item/form.html', context)

# Edit
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    
    title = "Edit Item"
    context = {
        'form': form,
        'title': title
    }
    
    return render(request, 'item/form.html', context)


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')