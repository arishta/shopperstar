from django.shortcuts import render
from rest_framework.views import APIView
from cart.models import OrderDetails,Order
from django.http import JsonResponse

class PaymentView(APIView):
	def post(self,request):
		order_id=request.data.get('order_id')
		amount_paid=request.data.get('amount_paid')
		currency=request.data.get('currency')
		total=Order.objects.filter(order_id=order_id).values('total')
		if not total:
			return JsonResponse({"message":"order_id not found"})
		else:
			total=total[0]['total']
			diff=amount_paid-total
			if diff<0:
				return JsonResponse({"message":"payment not complete"})
			else:
				OrderDetails.objects.filter(order_id_id=order_id).update(is_active=False)
				Order.objecs.filter(order_id=order_id).update(is_active=False)
				if diff==0:
					return JsonResponse({"message":"payment successful"})
				else:
					return JsonResponse({"message":"payment successful","change returned":str(diff)+currency})


