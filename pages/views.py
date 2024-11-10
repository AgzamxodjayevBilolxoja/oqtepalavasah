from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import CategoryModel, ProductModel, BranchesModel, CartModel, LikeModel,OrderModel
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.templatetags.static import static

def home_view(request):
    categories = CategoryModel.objects.all()
    category = request.GET.get('category')
    try:
        cart = CartModel.objects.filter(user=request.user, status=True).values_list('product_id', flat=True)
        like = LikeModel.objects.filter(user=request.user, status=True).values_list('product_id', flat=True)
    except:
        cart = []
        like = []
    
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    
    search = request.GET.get('search')
    if search:
        if request.session.get('lang') == "uz":
            products = ProductModel.objects.filter(title_uz__icontains=search).all()
        elif request.session.get('lang') == "ru":
            products = ProductModel.objects.filter(title_ru__icontains=search).all()
        elif request.session.get('lang') == "en":
            products = ProductModel.objects.filter(title_en__icontains=search).all()
    else:
        if category:
            request.session['category'] = category
            products = ProductModel.objects.filter(category__en=category).all()
        else:
            category = "Promos"
            request.session['category'] = category
            products = ProductModel.objects.filter(category__en=category).all()
    
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
    
    context = {
        "categories": categories,
        "active_category": request.session['category'],
        "products": products,
        "lang": request.session['lang'],
        "cart": cart,
        "like": like,
        "region": request.session['region'],
    }
    return render(request, "menu.html", context)


def about_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
        
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
        
    context = {
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    
    return render(request, "about_us.html", context)


def branches_view(request):
    branches = BranchesModel.objects.all()

    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
    context = {
        "branches": branches,
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "branches.html", context)


def contacts_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
    context = {
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "contacts.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')

        user = authenticate(request, username=username, email=email)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            if request.session['lang'] == "uz":
                messages.error(request, "Ism yoki email noto'g'ri. Iltimos, qaytadan kiriting.")
            elif request.session['lang'] == "ru":
                messages.error(request, "Имя пользователя или адрес электронной почты неверны. Пожалуйста, войдите еще раз.")
            elif request.session['lang'] == "en":
                messages.error(request, "Username or email address is incorrect. Please login again.")
        
    context = {
        "lang": request.session['lang']
    }
    return render(request, 'login.html', context)


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User.objects.filter(username=name).first()
        if user:
            if request.session['lang'] == "uz":
                messages.error(request, "Bunday foydalanuvchi bor!")
            elif request.session['lang'] == "ru":
                messages.error(request, "Есть такой пользователь!")
            elif request.session['lang'] == "en":
                messages.error(request, "There is such a user!")
        else:
            user = User.objects.filter(email=email).first()
            if user:
                if request.session['lang'] == "uz":
                    messages.error(request, "Bunday foydalanuvchi bor!")
                elif request.session['lang'] == "ru":
                    messages.error(request, "Есть такой пользователь!")
                elif request.session['lang'] == "en":
                    messages.error(request, "There is such a user!")
            else:
                User.objects.create(
                    username=name,
                    email=email)

                return redirect('login')
    context = {
        "lang": request.session['lang']
    }
    return render(request, "register.html", context)


def logout_view(request):
    lang = request.session['lang']
    logout(request)
    request.session['lang'] = lang
    return redirect("home")


@csrf_exempt
def add_to_cart_view(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Siz tizimga kirishingiz kerak!"})

    if request.method == "POST":
        try:
            # CartModel'dan mahsulotni topish
            product = CartModel.objects.get(user=request.user, product_id=pk)

            # Mahsulotni olib tashlash (statusni False qilish va countni 0 qilish)
            if product.status:
                product.status = False
                product.count = 0
                message = "Savatdan olib tashlandi!"
            else:
                # Mahsulotni qo'shish (statusni True qilish va countni 1 qilish)
                product.status = True
                product.count = 1
                message = "Savatga qo'shildi!"
            
            product.save()  # O'zgartirishlarni saqlash
            return JsonResponse({"status": "success", "message": message})

        except CartModel.DoesNotExist:
            # Agar mahsulot savatda yo'q bo'lsa, uni yaratish
            CartModel.objects.create(user=request.user, product_id=pk, status=True, count=1)
            return JsonResponse({"status": "success", "message": "Savatga qo'shildi!"})

    return JsonResponse({"status": "error", "message": "POST so'rov talab qilinadi."})


def add_to_cart3_view(request, pk):
    product = CartModel.objects.filter(product_id=pk)
    try:
        product = CartModel.objects.get(user=request.user, product_id=pk)
        product.status = not product.status
        product.count = 1
        product.save()
    except:
        CartModel.objects.create(user=request.user, product_id=pk, status=True)
    
    return redirect("cart")

@csrf_exempt
def add_like_view(request, pk):
    if request.method == 'POST':
        user = request.user  # Foydalanuvchi
        # Mahsulotga like qo'shish yoki olib tashlash
        like_item, created = LikeModel.objects.get_or_create(user=user, product_id=pk)
        
        # Holatini o'zgartirish
        like_item.status = not like_item.status
        like_item.save()

        # Javobda yangi holat va yangi ikonani yuborish
        new_icon = static('image/icons/icon11.svg' if like_item.status else 'image/icons/icon10.svg')
        
        return JsonResponse({"status": "success", "new_status": like_item.status, "new_icon": new_icon})

    return JsonResponse({"status": "error"}, status=400)

def add_like2_view(request, pk):
    product = LikeModel.objects.filter(product_id=pk)
    try:
        product = LikeModel.objects.get(user=request.user, product_id=pk)
        product.status = not product.status
        product.save()
    except:
        LikeModel.objects.create(user=request.user, product_id=pk, status=True)
    
    return redirect("likes")

def likes_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    try:
        cart = CartModel.objects.filter(user=request.user, status=True).values_list('product_id', flat=True)
        like = LikeModel.objects.filter(user=request.user, status=True).values_list('product_id', flat=True)
        products = []
        for id in like:
            products.append(ProductModel.objects.filter(id=id).first())
    except:
        cart = []
        like = []
        products = []
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
        
    context = {
        "cart": cart,
        "like": like,
        "products": products,
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "like.html", context)

def cart_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    try:
        cart = CartModel.objects.filter(user=request.user, status=True).values_list('product_id', flat=True)
        count = CartModel.objects.filter(user=request.user, status=True).all()
        products = []
        for id in cart:
            products.append(ProductModel.objects.filter(id=id).first())
        
    except:
        cart = []
        products = []
        count = []
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
        
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
        
    context = {
        "cart": cart,
        "count": count,
        "products": products,
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "cart.html", context)

def plus_count_view(request, pk):
    product = CartModel.objects.get(user=request.user, product_id=pk)
    product.count = product.count + 1
    product.save()
    return redirect('cart')

def minus_count_view(request, pk):
    product = CartModel.objects.get(user=request.user, product_id=pk)
    product.count = product.count - 1
    if product.count == 0:
        CartModel.objects.filter(user=request.user, product_id=pk).update(status=False)
    else:
        product.save()
    return redirect('cart')

def choose_branch_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    branch_id = request.session.get('branch_id')
    if request.method == "POST":
        delivery = request.POST.get('delivery')
        branch = BranchesModel.objects.filter(id=branch_id).first()
        cart = CartModel.objects.filter(user=request.user, status=True)
        if delivery:
            for product in cart:
                OrderModel.objects.create(
                    product=ProductModel.objects.filter(id=product.product_id).first(),
                    count=product.count,
                    address=delivery,
                    user=request.user
                )
                product.status = not product.status
                product.save()
        elif branch:
            for product in cart:
                OrderModel.objects.create(
                    product=ProductModel.objects.filter(id=product.product_id).first(),
                    count=product.count,
                    branch=branch,
                    user=request.user
                )
                product.status = not product.status
                product.save()
            
        return redirect('home')
    search_b = request.GET.get('search_b')
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
    if search_b:
        if request.session['region'] == "tashkent":
            branches = BranchesModel.objects.filter(name_uz__icontains=search_b, region="TASHKENT").all()
            if not branches:
                branches = BranchesModel.objects.filter(name_ru__icontains=search_b, region="TASHKENT").all()
            if not branches:
                branches = BranchesModel.objects.filter(name_en__icontains=search_b, region="TASHKENT").all()
        elif request.session['region'] == "samarkand":
            branches = BranchesModel.objects.filter(name_uz__icontains=search_b, region="SAMARKAND").all()
            if not branches:
                branches = BranchesModel.objects.filter(name_ru__icontains=search_b, region="SAMARKAND").all()
            if not branches:
                branches = BranchesModel.objects.filter(name_en__icontains=search_b, region="SAMARKAND").all()
    else:
        if request.session['region'] == "tashkent":
            branches = BranchesModel.objects.filter(region="TASHKENT").all()
        elif request.session['region'] == "samarkand":
            branches = BranchesModel.objects.filter(region="SAMARKAND").all()
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
        
    context = {
        "branches": branches,
        "branch_id": branch_id,
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "choose_b.html", context)

def branch2_view(request, pk):
    request.session["branch_id"] = pk
    return redirect('choose_branch')

def orders_view(request):
    search = request.GET.get('search')
    if search:
        return redirect(f'{reverse("home")}?search={search}')
    orders = OrderModel.objects.filter(user=request.user).order_by("-created_at").all()
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    region = request.GET.get('region')
    if not request.session.get('region'):
        request.session['region'] = 'tashkent'
    elif region == "tashkent":
        request.session['region'] = 'tashkent'
    elif region == "samarkand":
        request.session['region'] = 'samarkand'
    
    context = {
        "orders": orders,
        "region": request.session['region'],
        "lang": request.session['lang']
    }
    return render(request, "orders.html", context)

def product_view(request, pk):
    product = ProductModel.objects.filter(id=pk).first()
    lang = request.GET.get('lang')
    if not request.session.get('lang'):
        request.session['lang'] = "uz"
    elif lang == "ru":
        request.session['lang'] = "ru"
    elif lang == "en":
        request.session['lang'] = "en"
    elif lang == "uz":
        request.session['lang'] = "uz"
    context = {
        "product": product,
        "lang": request.session['lang']
    }
    return render(request, "product.html", context)