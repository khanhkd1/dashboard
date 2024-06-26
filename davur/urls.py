from django.urls import path
from davur import davur_views
from users import users_views
app_name='davur'
urlpatterns = [

	path('users/',users_views.users,name="users"),
	path('user-details/<int:id>/',users_views.user_details,name="user-details"),
	path('add-user/',users_views.add_user,name="add-user"),
	path('edit-user/<int:id>/',users_views.edit_user,name="edit-user"),
	path('delete-user/<int:id>/',users_views.delete_user,name="delete-user"),
	path('delete-multiple-user/',users_views.delete_multiple_user,name="delete-multiple-user"),

	path('login/',users_views.login_user,name="login"),
	path('logout/',users_views.logout_user,name="logout"),
	path('groups/',users_views.groups_list,name="groups"),
	path('group-edit/<int:id>/',users_views.group_edit,name="group-edit"),
	path('group-delete/<int:id>/',users_views.group_delete,name="group-delete"),
	path('group-add/',users_views.group_add,name="group-add"),
	path('permissions/',users_views.permissions,name="permissions"),
	path('edit-permissions/<int:id>/',users_views.edit_permissions,name="edit-permissions"),
	path('delete-permissions/<int:id>/',users_views.delete_permissions,name="delete-permissions"),
	path('assign-permissions-to-user/<int:id>/',users_views.assign_permissions_to_user,name="assign-permissions-to-user"),
	# path('signup/',users_views.signup,name="signup"),
	path('activate/<uidb64>/<token>/',users_views.activate, name='activate'),



















    path('',davur_views.index,name="index"),
    path('index/',davur_views.index,name="index"),
    path('page-analytics/',davur_views.page_analytics,name="page-analytics"),
    path('page-review/',davur_views.page_review,name="page-review"),
    path('page-order/',davur_views.page_order,name="page-order"),
    path('page-order-list/',davur_views.page_order_list,name="page-order-list"),
    path('page-general-customers/',davur_views.page_general_customers,name="page-general-customers"),
    path('app-profile/',davur_views.app_profile,name="app-profile"),
    path('post-details/',davur_views.post_details,name="post-details"),
    path('email-compose/',davur_views.email_compose,name="email-compose"),
    path('email-inbox/',davur_views.email_inbox,name="email-inbox"),
    path('email-read/',davur_views.email_read,name="email-read"),
    path('app-calender/',davur_views.app_calender,name="app-calender"),
    path('ecom-product-grid/',davur_views.ecom_product_grid,name="ecom-product-grid"),
    path('ecom-product-list/',davur_views.ecom_product_list,name="ecom-product-list"),
    path('ecom-product-detail/',davur_views.ecom_product_detail,name="ecom-product-detail"),
    path('ecom-product-order/',davur_views.ecom_product_order,name="ecom-product-order"),
    path('ecom-checkout/',davur_views.ecom_checkout,name="ecom-checkout"),
    path('ecom-invoice/',davur_views.ecom_invoice,name="ecom-invoice"),
    path('ecom-customers/',davur_views.ecom_customers,name="ecom-customers"),
    path('chart-flot/',davur_views.chart_flot,name="chart-flot"),
    path('chart-morris/',davur_views.chart_morris,name="chart-morris"),
    path('chart-chartjs/',davur_views.chart_chartjs,name="chart-chartjs"),
    path('chart-chartist/',davur_views.chart_chartist,name="chart-chartist"),
    path('chart-sparkline/',davur_views.chart_sparkline,name="chart-sparkline"),
    path('chart-peity/',davur_views.chart_peity,name="chart-peity"),
    path('ui-accordion/',davur_views.ui_accordion,name="ui-accordion"),
    path('ui-alert/',davur_views.ui_alert,name="ui-alert"),
    path('ui-badge/',davur_views.ui_badge,name="ui-badge"),
    path('ui-button/',davur_views.ui_button,name="ui-button"),
    path('ui-modal/',davur_views.ui_modal,name="ui-modal"),
    path('ui-button-group/',davur_views.ui_button_group,name="ui-button-group"),
    path('ui-list-group/',davur_views.ui_list_group,name="ui-list-group"),
    path('ui-media-object/',davur_views.ui_media_object,name="ui-media-object"),
    path('ui-card/',davur_views.ui_card,name="ui-card"),
    path('ui-carousel/',davur_views.ui_carousel,name="ui-carousel"),
    path('ui-dropdown/',davur_views.ui_dropdown,name="ui-dropdown"),
    path('ui-popover/',davur_views.ui_popover,name="ui-popover"),
    path('ui-progressbar/',davur_views.ui_progressbar,name="ui-progressbar"),
    path('ui-tab/',davur_views.ui_tab,name="ui-tab"),
    path('ui-typography/',davur_views.ui_typography,name="ui-typography"),
    path('ui-pagination/',davur_views.ui_pagination,name="ui-pagination"),
    path('ui-grid/',davur_views.ui_grid,name="ui-grid"),
    path('uc-select2/',davur_views.uc_select2,name="uc-select2"),
    path('uc-nestable/',davur_views.uc_nestable,name="uc-nestable"),
    path('uc-noui-slider/',davur_views.uc_noui_slider,name="uc-noui-slider"),
    path('uc-sweetalert/',davur_views.uc_sweetalert,name="uc-sweetalert"),
    path('uc-toastr/',davur_views.uc_toastr,name="uc-toastr"),
    path('map-jqvmap/',davur_views.map_jqvmap,name="map-jqvmap"),
    path('uc-lightgallery/',davur_views.uc_lightgallery,name="uc-lightgallery"),
    path('widget-basic/',davur_views.widget_basic,name="widget-basic"),
    path('form-element/',davur_views.form_element,name="form-element"),
    path('form-wizard/',davur_views.form_wizard,name="form-wizard"),
    path('form-ckeditor/',davur_views.form_ckeditor,name="form-ckeditor"),
    path('form-pickers/',davur_views.form_pickers,name="form-pickers"),
    path('form-validation-jquery/',davur_views.form_validation_jquery,name="form-validation-jquery"),
    path('table-bootstrap-basic/',davur_views.table_bootstrap_basic,name="table-bootstrap-basic"),
    path('table-datatable-basic/',davur_views.table_datatable_basic,name="table-datatable-basic"),
    path('page-error-400/',davur_views.page_error_400,name="page-error-400"),
    path('page-error-403/',davur_views.page_error_403,name="page-error-403"),
    path('page-error-404/',davur_views.page_error_404,name="page-error-404"),
    path('page-error-500/',davur_views.page_error_500,name="page-error-500"),
    path('page-error-503/',davur_views.page_error_503,name="page-error-503"),

    path('page-lock-screen/',davur_views.page_lock_screen,name="page-lock-screen"),

    
]