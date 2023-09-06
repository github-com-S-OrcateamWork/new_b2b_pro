from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import views, viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import F

from .models import (
    Category,
    SubCategory,
    Product,
    Company,
    ProductRating,
    Application,
    Question,
)
from .filters import ProductFilter
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    ProductRetrieveSerializer,
    CompanySerializer,
    ProductRatingSerializer,
    ApplicationSerializer,
    QuestionSerializer,
)


class GetCSRFToken(views.APIView):
    permission_classes = [AllowAny]

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, format=None):
        """
        Get CSRF token for the current user.
        """
        return Response("CSRF token obtained successfully.")


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get", "head", "options"]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing subcategories.
    """

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """

    queryset = Product.objects.all().order_by("-updated_at")
    serializer_class = ProductRetrieveSerializer
    http_method_names = ["get", "head", "options"]
    filterset_class = ProductFilter
    filter_backends = [SearchFilter]
    search_fields = ["translations__name"]
    ordering_fields = ["created_at", "name", "type_product"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductRetrieveSerializer
        return super().get_serializer_class()


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing companies.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ["translations__name"]


class ProductRatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product ratings.
    """

    queryset = ProductRating.objects.all().order_by(F("star").desc())
    serializer_class = ProductRatingSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing applications.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing questions.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
