from django.shortcuts import render
from rest_framework import generics, mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .permissions import IsStaffEditorPermission
# Create your views here.

# class ProductMixinView(
#     mixins.ListModelMixin,
#     generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     ):
#     queryset =Product.objects.all()
#     serializer_class=ProductSerializers
#     lookup_field='pk'
#     def get(self,request,*args, **kwargs):
#         pk=kwargs.get('pk')
#         if pk is not None:
#             return self.Retrieve(request,*args,**kwargs)
#         print(f'The args and kwargs {args} {kwargs}')
#         return self.list(request,*args,**kwargs)
#     def post(self, request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#     def perform_create(self,serializer):
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title=serializer.validated_data.get('title')
#         content=serializer.validated_data.get("content")
#         if content is None:
#             content ='This is a single view doing cool stuff'        
#         serializer.save(content=content)
# # product_mixin_view=ProductMixinView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializers
    # permission_classes=[permissions.IsAuthenticated]
    authentication_clases=[authentication.SessionAuthentication,
                           authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    
    
    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get("content")
        if content is None:
            content =title        
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializers
    authentication_clases=[authentication.SessionAuthentication,
                           authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    
    lookup_field ='pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    permission_classes=[permissions.DjangoModelPermissions]
    
    def perform_update(self,serializer):
        instance= serializer.save()
        if not instance.content:
            instance.content=instance.title
            

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    
    def perform_destroy(self,instance):
        #Any thing you want to do with the instance you do here
        super().perform_destory()
  
@api_view(["GET","POST","PUT"]) 
def product_alt_view(request,pk=None, *args, **kwargs):
    method =request.method
    
    if method =='GET':
        if pk is not None:
            #detail view
          obj=get_object_or_404(Product,pk=pk)
          serializer=ProductSerializers(obj,many=False)
          return Response(serializer.data)
    
         #list view  
        # get request-> detail view
        #list view
        queryset = Product.objects.all()
        serializer=ProductSerializers(queryset,many=True)
        return Response(serializer.data)
        
    if method=="POST":
        #create an item
        serializer =ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get("content")
            if content is None:
                content =title        
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)
    if method=="PUT":
        obj=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializers(obj,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if method=="DELETE":
        obj=get_object_or_404(Product,pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
         
# class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializers
#     def get(self,request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)
# product_mixin_view=ProductMixinView.as_view()


"""Session Authentication & Permissions"""  
"""We will create custom user permissions"""
"""User and Group Permissions with DjangoModelPermissions"""