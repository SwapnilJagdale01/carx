from import_export import resources
from carx_drf.models import Tyre

class TyreResource(resources.ModelResource):
    class Meta:
        model = Tyre
        fields = ('name','brand', 'product_type', 'normalsectionwidth', 'normalaspectratio', 'constructiontype', 'rimdiamter',
        'loadindex','speedsymbol','category__name','pattern','description','warranty','warranty_summery',
        'mrp','construction_type_R','vehicle__name')
        exclude=['left_image','right_image','front_image','back_image']