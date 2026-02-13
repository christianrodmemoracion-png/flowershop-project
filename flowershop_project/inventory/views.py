from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .models import Flower, Supplier
from .forms import FlowerForm, SupplierForm

@login_required
def flower_list(request):
    flowers = Flower.objects.all().order_by('name')
    # Use F() expression for the database query
    low_stock = Flower.objects.filter(quantity_in_stock__lte=F('reorder_level'))
    return render(request, 'inventory/flower_list.html', {
        'flowers': flowers,
        'low_stock': low_stock
    })

@login_required
def flower_create(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flower added successfully!')
            return redirect('flower_list')
    else:
        form = FlowerForm()
    return render(request, 'inventory/flower_form.html', {'form': form, 'title': 'Add Flower'})

@login_required
def flower_update(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        form = FlowerForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flower updated successfully!')
            return redirect('flower_list')
    else:
        form = FlowerForm(instance=flower)
    return render(request, 'inventory/flower_form.html', {'form': form, 'title': 'Edit Flower'})

@login_required
def flower_delete(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        flower.delete()
        messages.success(request, 'Flower deleted successfully!')
        return redirect('flower_list')
    return render(request, 'inventory/flower_confirm_delete.html', {'flower': flower})

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all().order_by('name')
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier added successfully!')
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/supplier_form.html', {'form': form, 'title': 'Add Supplier'})

@login_required
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated successfully!')
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/supplier_form.html', {'form': form, 'title': 'Edit Supplier'})

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Supplier deleted successfully!')
        return redirect('supplier_list')
    return render(request, 'inventory/supplier_confirm_delete.html', {'supplier': supplier})