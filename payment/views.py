from django.shortcuts import render
from rest_framework.views import APIView
from cart.models import OrderDetails,Order
from django.http import JsonResponse
from .models import Payment
from .serializers import PaymentSerializer

class PaymentView(APIView):
	def post(self,request):
		order_id=request.data.get('order_id')
		amount_paid=request.data.get('amount_paid')
		currency=request.data.get('currency')
		total=Order.objects.filter(id=order_id).values('total')
		Payment.objects.create(order_id=Order.objects.get(id=order_id),amount_paid=amount_paid,currency=currency)
		if not total:
			return JsonResponse({"message":"order_id not found"})
		else:
			total=total[0]['total']
			diff=amount_paid-total
			if diff<0:
				return JsonResponse({"message":"payment not complete"})
			else:
				OrderDetails.objects.filter(order_id_id=order_id).update(is_active=0)
				Order.objects.filter(id=order_id).update(is_active=0)
				qset=Payment.objects.filter(order_id=order_id)
				serializer=PaymentSerializer(qset,many=True)
				return JsonResponse({"payment status":"sucessful","payment details":serializer.data})


