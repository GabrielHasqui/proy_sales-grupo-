from django.urls import path
from core import views
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
   #Login y resgiter
   path('signup/', views.signup, name="signup"),
   path('signout/', views.signout, name='signout'),
   path('signin/', views.signin, name='signin'),

   # urls de vistas
   path('product_list/', views.product_List,name='product_list'),
   path('product_create/', views.product_create,name='product_create'),
   path('product_update/<int:id>/', views.product_update,name='product_update'),
   path('product_delete/<int:id>/', views.product_delete,name='product_delete'),
  
    # urls de marcas
   path('brands_list/', views.brand_List,name='brands_list'),
   path('brands_create/', views.brands_create, name='brands_create'),
   path('brands_update/<int:id>/', views.brands_update, name='brands_update'),
   path('brands_delete/<int:id>/', views.brands_delete, name='brands_delete'),

   # urls de proveedores
   path('suppliers_list/', views.supplier_List, name='suppliers_list'),
   path('suppliers_create/', views.suppliers_create, name='suppliers_create'),
   path('suppliers_update/<int:id>/', views.suppliers_update, name='suppliers_update'),
   path('suppliers_delete/<int:id>/', views.suppliers_delete, name='suppliers_delete'),

   #urls de category
   path('category_list/', views.category_list, name='category_list'),
   path('category_create/', views.category_create, name='category_create'),
   path('category_update/<int:id>/', views.category_update, name='category_update'),
   path('category_delete/<int:id>/', views.category_delete, name='category_delete')
]