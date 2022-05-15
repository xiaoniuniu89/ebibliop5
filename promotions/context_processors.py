from promotions.models import Promo


def promo(request):
    promo_codes = Promo.objects.all()
    return ({'promo_codes': promo_codes})
