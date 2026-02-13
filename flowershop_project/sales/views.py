from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from .models import Sale, Customer
from .forms import SaleForm, CustomerForm
from inventory.models import Flower

@login_required
def sale_list(request):
    sales = Sale.objects.all().order_by('-sale_date')
    
    # Calculate statistics
    sales_total = sales.aggregate(total=Sum('total_amount'))['total'] or 0
    total_quantity = sales.aggregate(total=Sum('quantity'))['total'] or 0
    average_sale = sales_total / len(sales) if sales else 0
    
    context = {
        'sales': sales,
        'sales_total': sales_total,
        'total_quantity': total_quantity,
        'average_sale': round(average_sale, 2)
    }
    return render(request, 'sales/sale_list.html', context)

@login_required
def sale_create(request):
    # Get only flowers that are in stock
    flowers = Flower.objects.filter(quantity_in_stock__gt=0)
    
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sold_by = request.user
            
            # Calculate total amount
            sale.total_amount = sale.quantity * sale.unit_price
            sale.save()
            
            # Update stock quantity
            flower = sale.flower
            flower.quantity_in_stock -= sale.quantity
            flower.save()
            
            messages.success(request, 'Sale recorded successfully!')
            return redirect('sale_list')
    else:
        form = SaleForm()
    
    return render(request, 'sales/sale_form.html', {
        'form': form,
        'flowers': flowers,
    })

@login_required
def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        # Restore stock before deleting
        sale.flower.quantity_in_stock += sale.quantity
        sale.flower.save()
        sale.delete()
        messages.success(request, 'Sale deleted successfully!')
        return redirect('sale_list')
    return render(request, 'sales/sale_confirm_delete.html', {'sale': sale})

@login_required
def sales_report(request):
    # Today's sales
    today = timezone.now().date()
    today_sales = Sale.objects.filter(sale_date__date=today)
    today_total = today_sales.aggregate(total=Sum('total_amount'))['total'] or 0
    
    # This week's sales
    week_ago = today - timedelta(days=7)
    week_sales = Sale.objects.filter(sale_date__date__gte=week_ago)
    week_total = week_sales.aggregate(total=Sum('total_amount'))['total'] or 0
    
    # Get last 7 days sales data for chart
    last_7_days = []
    for i in range(6, -1, -1):  # Last 7 days including today
        day = today - timedelta(days=i)
        day_sales = Sale.objects.filter(sale_date__date=day)
        day_total = day_sales.aggregate(total=Sum('total_amount'))['total'] or 0
        last_7_days.append({
            'date': day,
            'total_amount': day_total,
            'sales_count': day_sales.count()
        })
    
    # Get day names for chart labels
    day_names = []
    for day_data in last_7_days:
        day_names.append(day_data['date'].strftime('%a'))  # Short day name (Mon, Tue, etc.)
    
    # Top selling flowers
    top_flowers = Sale.objects.values('flower__name').annotate(
        total_sold=Sum('quantity'),
        total_revenue=Sum('total_amount')
    ).order_by('-total_sold')[:5]
    
    # Payment method counts
    payment_methods = Sale.objects.values('payment_method').annotate(
        count=Count('id')
    )
    payment_counts = {pm['payment_method']: pm['count'] for pm in payment_methods}
    
    # Calculate averages
    total_sales_count = Sale.objects.count()
    average_sale = week_total / total_sales_count if total_sales_count > 0 else 0
    
    context = {
        'today_sales': today_sales,
        'today_total': today_total,
        'week_total': week_total,
        'last_7_days_sales': last_7_days,
        'day_names': day_names,
        'top_flowers': top_flowers,
        'payment_methods': payment_counts,
        'total_customers': Customer.objects.count(),
        'average_sale': round(average_sale, 2),
    }
    return render(request, 'sales/sales_report.html', context)