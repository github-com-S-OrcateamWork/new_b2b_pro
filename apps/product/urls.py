from django.urls import include, path
from rest_framework import routers
from .views import CompanyViewSet, ProductViewSet, ProductRatingViewSet, CategoryViewSet, SubCategoryViewSet, ApplicationViewSet, QuestionViewSet
from .views import GetCSRFToken

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-ratings', ProductRatingViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-csrf-token/', GetCSRFToken.as_view(), name='get-csrf-token'), 

]
