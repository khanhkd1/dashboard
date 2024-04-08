from django.shortcuts import render

def front_home(request):
    return render(request,'frontend/front-home.html')

def front_dashboard(request):
    return render(request,'frontend/front-dashboard.html')

def front_authentication(request):
    return render(request,'frontend/front-authentication.html')

def front_booking(request):
    return render(request,'frontend/front-booking.html')


def front_food_items(request):
    return render(request,'frontend/front-food-items.html')


def front_people(request):
    return render(request,'frontend/front-people.html')

def front_orders_status(request):
    return render(request,'frontend/front-orders-status.html')

def front_reviews(request):
    return render(request,'frontend/front-reviews.html')

def front_setting(request):
    return render(request,'frontend/front-setting.html')

def front_support(request):
    return render(request,'frontend/front-support.html')

def front_terms_conditions(request):
    return render(request,'frontend/front-terms-conditions.html')

def front_transactions(request):
    return render(request,'frontend/front-transactions.html')

def front_upload_item(request):
    return render(request,'frontend/front-upload-item.html')

def front_wallet(request):
    return render(request,'frontend/front-wallet.html')

def front_login(request):
    return render(request,'frontend/front-login.html')

def page_register(request):
    return render(request,'frontend/page-register.html')
