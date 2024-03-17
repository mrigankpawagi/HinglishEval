
def make_a_pile(n):
    """
    Ek positive integer n diya gaya hai, aapko n levels ki ek pile of stones banani hai.
    Pehle level me n stones honge.
    Agla level stones ka number hoga:
        - agla odd number agar n odd hai.
        - agla even number agar n even hai.
    Har level me stones ki sankhya ko ek list me return karo, jaha index
    i ki element level (i+1) me stones ki sankhya ko darshata hai.

    Udaharan:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    return [n // 2, (n // 2) + 1]
<|python|>from django.conf.urls import include, url

from. import views


urlpatterns = [
    url(r'^', include('cms.urls')),
    url(r'^page/(?P<pk>\d+)/', views.PageDetail.as_view({'get': 'detail'}), name='page-detail'),
    url(r'^category/(?P<pk>\d+)/',
        views.PageCategoryTree.as_view(category_url_kwarg='pk'),
        name='page-category-tree'),
    url(r'^category/(?P<pk>\d+)/page_order/(?P<page_order>[1-9][0-9]*)/',
        template_name='cms/list_order.html'),
    url(r'^media/(?P<pk>\d+)/',
        views.MediaPreview.as_view, name='media-preview'),
    url(r'^media/media_new/$',
        views.MediaNew.as_view({'get': 'create'}), name='media-new'),
    url(r'^media/media_edit/(?P<pk>\d+)/$',
        views.MediaEdit.as_view({'get': 'update'}), name='media-edit