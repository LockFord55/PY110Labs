from django.contrib.auth import get_user
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from logic.services import view_in_wishlist, add_to_wishlist, remove_from_wishlist
from store.models import DATABASE
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login:login_view')
def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]
        if request.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})

        products = []
        # for product_id, quantity in data['products']:
        #     product = DATABASE.get(product_id)
        #     product['quantity'] = quantity
        #     product["price_total"] = f"{quantity * product['price_after']:.2f}"
        #     products.append(product)
        for product_id in data['products']:
            product = DATABASE.get(product_id)
            products.append(product)

        return render(request, 'wishlist/wishlist.html',
                      context={"products": products})


def wishlist_add_json(request, id_product: str):
    """
    Добавление продукта в избранное и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное."},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в избранное."},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def wishlist_del_json(request, id_product: str):
    """
    Удаление продукта из избранного и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из избранного."},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из избранного."},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def wishlist_json(request):
    """
    Просмотр всех продуктов в избранном для пользователя и возвращение этого в JSON
    """
    if request.method == "GET":
        current_user = get_user(request).username  # from django.contrib.auth import get_user
        data = view_in_wishlist(request)[current_user]
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})

        return JsonResponse({"answer": "Пользователь не авторизирован."},
                            status=404)


def wishlist_remove_view(request, id_product):
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)
        if result:
            return redirect("wishlist:wishlist_view")

        return HttpResponseNotFound("Неудачное удаление из корзины.")
