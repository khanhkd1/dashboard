from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='davur:login')
def index(request):
    return render(request,'davur/index.html')

@login_required(login_url='davur:login')
def page_analytics(request):
    return render(request,'davur/page-analytics.html')

@login_required(login_url='davur:login')
def page_review(request):
    return render(request,'davur/page-review.html')

@login_required(login_url='davur:login')
def page_order(request):
    return render(request,'davur/page-order.html')

@login_required(login_url='davur:login')
def page_order_list(request):
    return render(request,'davur/page-order-list.html')

@login_required(login_url='davur:login')
def page_general_customers(request):
    return render(request,'davur/page-general-customers.html')

@login_required(login_url='davur:login')
def app_profile(request):
    return render(request,'davur/apps/app-profile.html')

@login_required(login_url='davur:login')
def post_details(request):
    return render(request,'davur/apps/post-details.html')

@login_required(login_url='davur:login')
def email_compose(request):
    return render(request,'davur/apps/email/email-compose.html')

@login_required(login_url='davur:login')
def email_inbox(request):
    return render(request,'davur/apps/email/email-inbox.html')

@login_required(login_url='davur:login')
def email_read(request):
    return render(request,'davur/apps/email/email-read.html')

@login_required(login_url='davur:login')
def app_calender(request):
    return render(request,'davur/apps/app-calender.html')

@login_required(login_url='davur:login')
def ecom_product_grid(request):
    return render(request,'davur/apps/shop/ecom-product-grid.html')

@login_required(login_url='davur:login')
def ecom_product_list(request):
    return render(request,'davur/apps/shop/ecom-product-list.html')

@login_required(login_url='davur:login')
def ecom_product_detail(request):
    return render(request,'davur/apps/shop/ecom-product-detail.html')

@login_required(login_url='davur:login')
def ecom_product_order(request):
    return render(request,'davur/apps/shop/ecom-product-order.html')

@login_required(login_url='davur:login')
def ecom_checkout(request):
    return render(request,'davur/apps/shop/ecom-checkout.html')

@login_required(login_url='davur:login')
def ecom_invoice(request):
    return render(request,'davur/apps/shop/ecom-invoice.html')

@login_required(login_url='davur:login')
def ecom_customers(request):
    return render(request,'davur/apps/shop/ecom-customers.html')

@login_required(login_url='davur:login')
def chart_flot(request):
    return render(request,'davur/charts/chart-flot.html')

@login_required(login_url='davur:login')
def chart_morris(request):
    return render(request,'davur/charts/chart-morris.html')

@login_required(login_url='davur:login')
def chart_chartjs(request):
    return render(request,'davur/charts/chart-chartjs.html')

@login_required(login_url='davur:login')
def chart_chartist(request):
    return render(request,'davur/charts/chart-chartist.html')

@login_required(login_url='davur:login')
def chart_sparkline(request):
    return render(request,'davur/charts/chart-sparkline.html')

@login_required(login_url='davur:login')
def chart_peity(request):
    return render(request,'davur/charts/chart-peity.html')

@login_required(login_url='davur:login')
def ui_accordion(request):
    return render(request,'davur/bootstrap/ui-accordion.html')

@login_required(login_url='davur:login')
def ui_alert(request):
    return render(request,'davur/bootstrap/ui-alert.html')

@login_required(login_url='davur:login')
def ui_badge(request):
    return render(request,'davur/bootstrap/ui-badge.html')

@login_required(login_url='davur:login')
def ui_button(request):
    return render(request,'davur/bootstrap/ui-button.html')

@login_required(login_url='davur:login')
def ui_modal(request):
    return render(request,'davur/bootstrap/ui-modal.html')

@login_required(login_url='davur:login')
def ui_button_group(request):
    return render(request,'davur/bootstrap/ui-button-group.html')

@login_required(login_url='davur:login')
def ui_list_group(request):
    return render(request,'davur/bootstrap/ui-list-group.html')

@login_required(login_url='davur:login')
def ui_media_object(request):
    return render(request,'davur/bootstrap/ui-media-object.html')

@login_required(login_url='davur:login')
def ui_card(request):
    return render(request,'davur/bootstrap/ui-card.html')

@login_required(login_url='davur:login')
def ui_carousel(request):
    return render(request,'davur/bootstrap/ui-carousel.html')

@login_required(login_url='davur:login')
def ui_dropdown(request):
    return render(request,'davur/bootstrap/ui-dropdown.html')

@login_required(login_url='davur:login')
def ui_popover(request):
    return render(request,'davur/bootstrap/ui-popover.html')

@login_required(login_url='davur:login')
def ui_progressbar(request):
    return render(request,'davur/bootstrap/ui-progressbar.html')

@login_required(login_url='davur:login')
def ui_tab(request):
    return render(request,'davur/bootstrap/ui-tab.html')

@login_required(login_url='davur:login')
def ui_typography(request):
    return render(request,'davur/bootstrap/ui-typography.html')

@login_required(login_url='davur:login')
def ui_pagination(request):
    return render(request,'davur/bootstrap/ui-pagination.html')

@login_required(login_url='davur:login')
def ui_grid(request):
    return render(request,'davur/bootstrap/ui-grid.html')

@login_required(login_url='davur:login')
def uc_select2(request):
    return render(request,'davur/plugins/uc-select2.html')

@login_required(login_url='davur:login')
def uc_nestable(request):
    return render(request,'davur/plugins/uc-nestable.html')

@login_required(login_url='davur:login')
def uc_noui_slider(request):
    return render(request,'davur/plugins/uc-noui-slider.html')

@login_required(login_url='davur:login')
def uc_sweetalert(request):
    return render(request,'davur/plugins/uc-sweetalert.html')

@login_required(login_url='davur:login')
def uc_sweetalert(request):
    return render(request,'davur/plugins/uc-sweetalert.html')

@login_required(login_url='davur:login')
def uc_toastr(request):
    return render(request,'davur/plugins/uc-toastr.html')

@login_required(login_url='davur:login')
def map_jqvmap(request):
    return render(request,'davur/plugins/map-jqvmap.html')

@login_required(login_url='davur:login')
def uc_lightgallery(request):
    return render(request,'davur/plugins/uc-lightgallery.html')

@login_required(login_url='davur:login')
def widget_basic(request):
    return render(request,'davur/widget-basic.html')

@login_required(login_url='davur:login')
def form_element(request):
    return render(request,'davur/forms/form-element.html')

@login_required(login_url='davur:login')
def form_wizard(request):
    return render(request,'davur/forms/form-wizard.html')

@login_required(login_url='davur:login')
def form_ckeditor(request):
    return render(request,'davur/forms/form-ckeditor.html')

@login_required(login_url='davur:login')
def form_pickers(request):
    return render(request,'davur/forms/form-pickers.html')

@login_required(login_url='davur:login')
def form_validation_jquery(request):
    return render(request,'davur/forms/form-validation-jquery.html')

@login_required(login_url='davur:login')
def table_bootstrap_basic(request):
    return render(request,'davur/table/table-bootstrap-basic.html')

@login_required(login_url='davur:login')
def table_datatable_basic(request):
    return render(request,'davur/table/table-datatable-basic.html')


def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')


def page_lock_screen(request):
    return render(request,'davur/pages/page-lock-screen.html')

