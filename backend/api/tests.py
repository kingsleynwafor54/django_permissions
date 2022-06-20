from django.test import TestCase
# import json
# from rest_framework.decorators import api_view
# # Create your tests here.

# @api_view(["GET",'POST'])
# def api_home1(request):
#     body = request.body
#     data={}
#     try:
#         data=json.loads(body)
#     except:
#         pass
#     print(data.keys())
#     data['headers']=request.headers
#     data['content_type']=request.content_type
#     return JsonResponse({"Message":"Hi there, is this is your Django API response!!"})