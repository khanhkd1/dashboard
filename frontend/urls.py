from django.urls import path
from frontend import frontend_views
app_name='frontend'
urlpatterns = [
    path('',frontend_views.front_home,name="front-home"),
    path('front-authentication/',frontend_views.front_authentication,name="front-authentication"),
    path('front-booking/',frontend_views.front_booking,name="front-booking"),
    path('front-food-items/',frontend_views.front_food_items,name="front-food-items"),
    path('front-people/',frontend_views.front_people,name="front-people"),
    path('front-orders-status/',frontend_views.front_orders_status,name="front-orders-status"),
    path('front-setting/',frontend_views.front_setting,name="front-setting"),
    path('front-support/',frontend_views.front_support,name="front-support"),
    path('front-terms-conditions/',frontend_views.front_terms_conditions,name="front-terms-conditions"),
    path('front-transactions/',frontend_views.front_transactions,name="front-transactions"),
    path('front-upload-item/',frontend_views.front_upload_item,name="front-upload-item"),
    path('front-wallet/',frontend_views.front_wallet,name="front-wallet"),
    path('front-login/',frontend_views.front_login,name="front-login"),
    path('page-register/',frontend_views.page_register,name="page-register"),
    

]