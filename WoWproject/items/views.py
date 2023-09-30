from django.http import JsonResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def search_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_name = data['item_name']
        items = Item.objects.filter(name__icontains=item_name).distinct()
        results = []
        for item in items:
            item_info = {
                'name': item.name,
                'price': item.price,
                'quantity': item.quantity,
                'datetime': item.datetime,
                'server': item.server,
            }
            results.append(item_info)
        return JsonResponse({'results': results})

