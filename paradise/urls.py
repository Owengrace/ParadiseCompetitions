from django.urls import path
from paradise.api.views import (
    ProductDetailView,
    ProductListView,
    OrderItemDeleteView,
    Competition_GroupView,
    OrderDetailView,
    EcardListView,
    CompetitionListView,
    CountryListView,
    Competition_GroupDetailView,
    ShippingAddressCreateView,
    ShippingAddressDeleteView,
    ShippingAddressListView,
    ShippingAddressUpdateView,
    CouponCreateView,
    CompetitionDetailView,
    FeaturedCompetitionListView,
    AddCompetitionToCartView,
    RemoveCompetitionFromCartView

)
urlpatterns = [
    path('order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('addresses/', ShippingAddressListView.as_view(), name='address-list'),
    path('addresses/create/', ShippingAddressCreateView.as_view(),
         name='address-create'),
    path('addresses/<pk>/update/',
         ShippingAddressUpdateView.as_view(), name='address-update'),
    path('addresses/<pk>/delete/',
         ShippingAddressDeleteView.as_view(), name='address-delete'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-coupon/', CouponCreateView.as_view(), name='add-coupon'),
    path('group/', Competition_GroupView.as_view(), name='Group'),
    path('group/<pk>/', Competition_GroupDetailView.as_view(), name='Group'),
    path('competition_list/', CompetitionListView.as_view(), name='competition'),
    path('featured_competition_list/',
         FeaturedCompetitionListView.as_view(), name='competition'),
    path('competition/<pk>/', CompetitionDetailView.as_view(), name='competition'),
    path('ecard/', EcardListView.as_view(), name='ecard'),
    path('add-competition-to-cart/',
         AddCompetitionToCartView.as_view(), name='add-to-cart'),

     path('remove-competition-from-cart/', RemoveCompetitionFromCartView.as_view(), name='remove-from-cart')
]
