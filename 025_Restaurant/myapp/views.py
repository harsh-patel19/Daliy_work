# restaurant/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import MenuItem, Category, Order, ContactMessage, Review, TeamMember


# ─── HOME ───────────────────────────────────────────────────────────────────

def home(request):
    featured_items   = MenuItem.objects.filter(is_active=True, is_featured=True)[:6]
    weekend_specials = MenuItem.objects.filter(is_active=True, is_special=True)[:4]
    reviews          = Review.objects.filter(is_published=True)[:3]
    context = {
        'featured_items':   featured_items,
        'weekend_specials': weekend_specials,
        'reviews':          reviews,
        'avg_rating':       '4.9',
        'total_menu_items': MenuItem.objects.filter(is_active=True).count(),
        'total_orders':     Order.objects.count(),
    }
    return render(request, 'home.html', context)


# ─── MENU ────────────────────────────────────────────────────────────────────

def menu(request):
    categories    = Category.objects.filter(is_active=True)
    active_cat    = request.GET.get('category', '')
    search_query  = request.GET.get('q', '')
    veg_filter    = request.GET.get('veg', '')

    qs = MenuItem.objects.filter(is_active=True).select_related('category')

    if active_cat:
        qs = qs.filter(category__slug=active_cat)
    if search_query:
        qs = qs.filter(name__icontains=search_query)
    if veg_filter:
        qs = qs.filter(is_veg=True)

    paginator  = Paginator(qs, 12)
    page_num   = request.GET.get('page', 1)
    menu_items = paginator.get_page(page_num)

    context = {
        'categories':    categories,
        'menu_items':    menu_items,
        'active_category': active_cat,
        'search_query':  search_query,
        'veg_filter':    veg_filter,
    }
    return render(request, 'menu.html', context)


def menu_item_detail(request, pk):
    item          = get_object_or_404(MenuItem, pk=pk, is_active=True)
    related_items = MenuItem.objects.filter(
        category=item.category, is_active=True
    ).exclude(pk=pk)[:3]
    context = {
        'item':          item,
        'related_items': related_items,
    }
    return render(request, 'menu_detail.html', context)


# ─── SPECIALS ────────────────────────────────────────────────────────────────

def specials(request):
    specials_qs = MenuItem.objects.filter(is_active=True, is_special=True)
    return render(request, 'specials.html', {'specials': specials_qs})


# ─── ORDER ───────────────────────────────────────────────────────────────────

def order(request):
    menu_items       = MenuItem.objects.filter(is_active=True).order_by('category', 'name')
    preselected_item = None

    item_pk = request.GET.get('item')
    if item_pk:
        preselected_item = MenuItem.objects.filter(pk=item_pk, is_active=True).first()

    context = {
        'menu_items':       menu_items,
        'preselected_item': preselected_item,
        'form':             {},   # replace with OrderForm() when ready
    }
    return render(request, 'order.html', context)


def order_place(request):
    if request.method != 'POST':
        return redirect('order')

    # Basic field extraction — swap this block with OrderForm(request.POST) validation
    order_obj = Order.objects.create(
        first_name     = request.POST.get('first_name', ''),
        last_name      = request.POST.get('last_name', ''),
        phone          = request.POST.get('phone', ''),
        email          = request.POST.get('email', ''),
        order_type     = request.POST.get('order_type', 'delivery'),
        address        = request.POST.get('address', ''),
        payment_method = request.POST.get('payment_method', 'cod'),
        notes          = request.POST.get('notes', ''),
        status         = 'confirmed',
    )

    item_pks = request.POST.getlist('items')
    for pk in item_pks:
        try:
            item = MenuItem.objects.get(pk=pk)
            order_obj.items.add(item)
        except MenuItem.DoesNotExist:
            pass

    messages.success(request, 'Your order has been placed successfully!')
    return redirect('order_confirm', pk=order_obj.pk)


def order_confirm(request, pk):
    order_obj = get_object_or_404(Order, pk=pk)
    return render(request, 'order_confirm.html', {'order': order_obj})


def order_track(request, pk):
    order_obj = get_object_or_404(Order, pk=pk)
    return render(request, 'order_track.html', {'order': order_obj})


# ─── ABOUT ───────────────────────────────────────────────────────────────────

def about(request):
    team = TeamMember.objects.filter(is_active=True).order_by('order')
    return render(request, 'about.html', {'team': team})


# ─── CONTACT ─────────────────────────────────────────────────────────────────

def contact(request):
    context = {'form': {}}   # replace with ContactForm() when ready
    return render(request, 'contact.html', context)


def contact_submit(request):
    if request.method != 'POST':
        return redirect('contact')

    ContactMessage.objects.create(
        first_name        = request.POST.get('first_name', ''),
        last_name         = request.POST.get('last_name', ''),
        email             = request.POST.get('email', ''),
        phone             = request.POST.get('phone', ''),
        subject           = request.POST.get('subject', ''),
        message           = request.POST.get('message', ''),
        reservation_date  = request.POST.get('reservation_date') or None,
        reservation_time  = request.POST.get('reservation_time', ''),
        guests            = request.POST.get('guests', ''),
    )

    messages.success(request, "Thanks for reaching out! We'll get back to you shortly.")
    return redirect('contact')
