'''
Created on 2014-9-20
@author: martin
'''
from decimal import Decimal
from django.contrib.auth.models import Group

if __name__ == '__main__':
    pass

def money_format(money):
    if not money:
        return ""
    return '${:,.2f}'.format(money)

def str_to_decimal(value,decimal_places):
    return round(Decimal(value.replace("$","").replace(",","")),decimal_places)

def is_admin(user):
    users_in_admin_group = Group.objects.get(name="BaptistAdmin").user_set.all()
    return user in users_in_admin_group or user.is_superuser
