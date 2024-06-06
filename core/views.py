from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from core.forms import ProductForm, CategoryForm, BrandForm, SupplierForm
from core.models import Product, Category, Brand, Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    products = Product.objects.all()  # Obtenemos todos los productos
    data = {
        "title1": "Home",
        "title2": "Super Mercado Economico",
        "products": products,  # Incluimos los productos en el contexto
    }
    return render(request, 'core/home.html', data)

def signup(request):

    if request.method == "GET":
        return render(request, 'signup.html', {'form':UserCreationForm})
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('core:signin')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'El usuario ya existe'})
        
        return render(request, 'signup.html', {'form':UserCreationForm, 'error': 'Contraseñas no coinciden'})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    
    if request.method == "GET":
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def product_List(request):
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos"
    }
    products = Product.objects.filter(user = request.user) # select * from Product
    data["products"]=products
    return render(request,"core/products/list.html",data)

@login_required
def product_create(request):
    data = {"title1": "Productos","title2": "Ingreso De Productos"}
   
    if request.method == "POST":
        #print(request.POST)
        form = ProductForm(request.POST,request.FILES, user=request.user)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            form.save_m2m()
            return redirect("core:product_list")

    else:
        data["form"] = ProductForm(user=request.user) # controles formulario sin datos

    return render(request, "core/products/form.html", data)

@login_required
def product_update(request,id):
    data = {"title1": "Productos","title2": ">Edicion De Productos"}
    product = Product.objects.get(pk=id)
    if request.method == "POST":
      form = ProductForm(request.POST,request.FILES, user=request.user, instance=product)
      if form.is_valid():
            form.save()
            return redirect("core:product_list")
    else:
        form = ProductForm(user=request.user, instance=product)
        data["form"] = form
    return render(request, "core/products/form.html", data)

@login_required
def product_delete(request,id):
    product = Product.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar Un Producto","product":product}
    if request.method == "POST":
        product.delete()
        return redirect("core:product_list")
 
    return render(request, "core/products/delete.html", data)


# vistas de marcas: Listar marcas
@login_required
def brand_List(request):
    data = {
        'title1': 'Marcas',
        'title2': 'Consulta de marcas'
    }
    brands = Brand.objects.filter(user=request.user) # select * from brand
    data['brands'] = brands
    return render(request, 'core/brands/list.html', data)

#crear una marca
@login_required
def brands_create(request):
    data = {'title1': 'Marcas','title2': 'Ingreso de marcas'}

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect('core:brands_list')
    else:
        data['form'] = BrandForm() # controles formulario sin datos

    return render(request, 'core/brands/form.html', data)

#editar una marca
@login_required
def brands_update(request, id):
    data = {'title1': 'Marcas','title2': 'Edición de marcas'}
    brand = Brand.objects.get(pk=id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('core:brands_list')
    else:
        form = BrandForm(instance=brand)
        data['form'] = form

    return render(request, 'core/brands/form.html', data)

#eliminar una marca
@login_required
def brands_delete(request, id):
    brand = Brand.objects.get(pk=id)
    data = {'title1': 'Marcas','title2': 'Eliminar una marca','brand': brand}
    if request.method == 'POST':
        brand.delete()
        return redirect('core:brands_list')

    return render(request, 'core/brands/delete.html', data)


#vistas de proveedores:create, update, delete
@login_required
def supplier_List(request):
    data = {
        'title1': 'Proveedores',
        'title2': 'Consulta de proveedores'
    }
    suppliers = Supplier.objects.filter(user = request.user) # select * from supplier
    data['suppliers'] = suppliers
    return render(request, 'core/suppliers/list.html', data)
#crear un proveedor
@login_required
def suppliers_create(request):
    data = {'title1': 'Proveedores', 'title2': 'Ingreso de proveedores'}

    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.save()
            messages.success(request, 'Proveedor creado correctamente')
            return redirect('core:suppliers_list')
        else:
            messages.error(request, 'Error al crear el proveedor. Verifique los datos ingresados')
            for field, error in form.errors.items():
                messages.error(request, f'{field}: {error}')
    else:  # Aquí se define form en el caso de una solicitud GET
        form = SupplierForm()

    data['form'] = form  # Se asegura de que form esté definida antes de pasarla a la plantilla
    return render(request, 'core/suppliers/form.html', data)

#editar un proveedor
@login_required
def suppliers_update(request, id):
    data = {'title1': 'Proveedores','title2': 'Edición de proveedores'}
    supplier = Supplier.objects.get(pk=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('core:suppliers_list')
    else:
        form = SupplierForm(instance=supplier)
        data['form'] = form

    return render(request, 'core/suppliers/form.html', data)

#eliminar un proveedor
@login_required
def suppliers_delete(request, id):
    supplier = Supplier.objects.get(pk=id)
    data = {'title1': 'Proveedores','title2': 'Eliminar un proveedor','supplier': supplier}
    if request.method == 'POST':
        supplier.delete()
        return redirect('core:suppliers_list')

    return render(request, 'core/suppliers/delete.html', data)


#vistas de categorias: Listar, crear, editar y eliminar
@login_required
def category_list(request):
    data = {
        "title1": "Categorias",
        "title2": "Consulta De Categorias"
    }
    categories = Category.objects.filter(user = request.user)
    data["categories"] = categories
    return render(request, 'core/category/list.html', data)

#crear una categoria
@login_required
def category_create(request):
    data = {"title1": "Categoria","title2": "Ingreso De Categorias"}
    
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('core:category_list')
    else:
        data['form'] = CategoryForm
        
    return render(request, 'core/category/form.html', data)

#editar una categoria
@login_required
def category_update(request, id):
    data = {"title1": "Categorias","title2": ">Edicion De Categorias"}
    category = Category.objects.get(pk=id)
    if request.method == "POST":
      form = CategoryForm(request.POST,request.FILES, instance=category)
      if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form = CategoryForm(instance=category)
        data["form"]=form
    return render(request, "core/category/form.html", data)

#eliminar una categoria
@login_required
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar Una Categoria","category":category}
    if request.method == "POST":
        category.delete()
        return redirect("core:category_list")
 
    return render(request, "core/category/delete.html", data)