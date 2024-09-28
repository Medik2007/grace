from django.shortcuts import render
from django.http import JsonResponse

from .models import Dress, DressColor, DressSize, DressModel
from users.models import Order, Delivery
from datetime import datetime, timedelta, timezone
import json


def get_bucket_cookie(request):
    bucket = request.COOKIES.get('bucket', '{}')
    return json.loads(bucket)

def set_bucket_cookie(response, data):
    bucket = json.dumps(data)
    expires = datetime.now(timezone.utc) + timedelta(days=365)
    response.set_cookie('bucket', bucket, expires=expires)

def bucket_order(request):
    bucket = get_bucket_cookie(request)
    all_orders = []
    for key in bucket:
        ids = key.split(',')
        order = Order(
            dress=Dress.objects.get(id=ids[0]), #type:ignore
            color=DressColor.objects.get(id=ids[1]), #type:ignore
            size=DressSize.objects.get(id=ids[2]), #type:ignore
            model=DressModel.objects.get(id=ids[3]), #type:ignore
            amount=bucket[key],
        )
        all_orders.append(order)
    return all_orders


def bucket_post(request):
    order = f"{request.POST['id']},{request.POST['color']},{request.POST['size']},{request.POST['model']}"
    bucket = get_bucket_cookie(request)

    if request.POST['act'] == 'load':
        if order in bucket:
            return JsonResponse({'count':bucket[order], 'order':order})
        else:
            return JsonResponse({'count':0, 'order':order})
    elif request.POST['act'] == 'plus':
        if not order in bucket: bucket[order] = 0
        bucket[order] = bucket[order] + 1
    elif request.POST['act'] == 'minus':
        if order in bucket:
            bucket[order] = bucket[order] - 1
        else:
            return JsonResponse({'count':0, 'order':order})
    elif request.POST['act'] == 'set':
        bucket[order] = request.POST['amount']

    if bucket[order] < 1:
        del bucket[order]
        response = JsonResponse({'count':0, 'order':order})
    else:
        response = JsonResponse({'count':bucket[order], 'order':order})

    set_bucket_cookie(response, bucket)
    return response


def index(request):
    all_dress = Dress.objects.all() #pyright: ignore
    return render(request, 'dress/index.html', {'all_dress':all_dress})


def view(request, id):
    if request.method == 'GET':
        dress = Dress.objects.get(id=id) #pyright: ignore
        in_bucket = 0
        bucket = get_bucket_cookie(request)
        if id in bucket: in_bucket = bucket[id]
        return render(request, 'dress/view.html', {'dress':dress, 'in_bucket':in_bucket})
    elif request.method == 'POST':
        return bucket_post(request)


def bucket(request):
    if request.method == 'GET':
        all_orders = bucket_order(request)
        return render(request, 'dress/bucket.html', {'all_orders':all_orders})
    elif request.method == 'POST':
        if request.POST['act'] != 'order':
            return bucket_post(request)
        else:
            if request.user.is_authenticated:
                all_orders = bucket_order(request)
                delivery = Delivery(
                    user=request.user,
                    adress=request.POST['adress']
                )
                delivery.save()
                for order in all_orders:
                    order.delivery = delivery
                    order.save()
                response = JsonResponse({'success':True})
                response.delete_cookie('bucket')
                return response
            else:
                return JsonResponse({'success':False})



def service(request):
    return render(request, 'dress/service.html')





