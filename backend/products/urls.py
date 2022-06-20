from django.urls import path

from . import views

urlpatterns = [
    path('',views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('detail',views.product_alt_view),
    path('detail/<int:pk>',views.product_alt_view),
    path('update/<int:pk>',views.ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>',views.ProductDeleteAPIView.as_view()),
    # path('<int:pk>/',views.ProductMixinView.as_view()),
    # path('',views.product_mixin_view),
    # path('',views.ProductMixinView.as_view()),
]
