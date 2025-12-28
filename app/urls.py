from django.urls import path 
from . import views

urlpatterns = [
    
  path("",views.Home.as_view(),name="home"),
  path("detail/<int:pk>/",views.Detail.as_view(),name="detail"),
  path("detail/<int:pk>/",views.FoodOrder.as_view(),name="order"),
  path("breakfast/",views.Breakfast.as_view(),name="breakfast"),
  path("lunch/",views.LunchBase.as_view(),name="lunch"),
  path("fast-food/",views.FastFoodLunch.as_view(),name="fast-food"),
  path("persian/",views.PersianLunch.as_view(),name="persian"),
  path("drinks/",views.Drink.as_view(),name="drinks"),
  path("about/",views.AboutUs.as_view(),name="about_us") ,
  path("contact-us/",views.contact_us,name="contact_us"),
 
    
]
