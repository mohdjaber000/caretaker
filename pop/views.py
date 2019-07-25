from django.shortcuts import render
from django.views import generic,View
from django.http import JsonResponse
from pop.forms import (CreditPurchaseForm,CashPurchaseForm
                       ,CreditPurchaseReturnForm,CashPurchaseReturnForm)
from custom.views import (JSONCreateView,JSONUpdateView,
                            JSONQueryView,JSONCreateMultipleView)
from pop.models import (CreditPurchase,CashPurchase,
                        CreditPurchaseReturn,CashPurchaseReturn)
from custom.invoice import print_invoice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from custom.decorators import access_required
# This view loads in the app
@method_decorator(access_required('cashpop'), name='dispatch')
class AppInitP(generic.base.TemplateView):
    template_name="pop/cashpurchases.html"

@method_decorator(access_required('creditpop'), name='dispatch')
class AppInitPC(generic.base.TemplateView):
    template_name="pop/creditpurchases.html"

@method_decorator(access_required('cashpr'), name='dispatch')
class AppInitR(generic.base.TemplateView):
    template_name="pop/cashreturns.html"

@method_decorator(access_required('creditpr'), name='dispatch')
class AppInitRC(generic.base.TemplateView):
    template_name="pop/creditreturns.html"

# helpers
class SettlePurchase(View):
    pass
#Views for CreditPurchase model
#create view
class CreateCreditPurchase(JSONCreateMultipleView):
    model = CreditPurchase
    form = CreditPurchaseForm
    expected_var = "purchases"
    general_vars = ["supplier","invoice",'supplier_name']
    numbers = ['invoice_number','invoice_time','supplier_name']
    user_required = True

    def print_receipt(self,requestPost):
        data = super().print_receipt(requestPost)

        opts = {
            'rname':'Purchase Invoice',
            'rno':data['invoice_number'],
            'customer':data['supplier_name'],
            'cashier':'ME AM ME',
            'currency':'GH CEDIS',
            'rdate':data['invoice_time'],
        }
        print_invoice(data['items'], opts)
#edit view
class UpdateCreditPurchase(JSONUpdateView):
    model = CreditPurchase
    form = CreditPurchaseForm
    user_required = True
#query view
class CreditPurchases(JSONQueryView):
    model = CreditPurchase

#Views for CashPurchase model
#create view
class CreateCashPurchase(JSONCreateMultipleView):
    model = CashPurchase
    form = CashPurchaseForm
    expected_var = "purchases"
    general_vars = ["supplier","receipt",'cash','system','currency','supplier_name']
    numbers = ['receipt_number','receipt_time','supplier_name']
    user_required = True

    def print_receipt(self,requestPost):
        data = super().print_receipt(requestPost)

        opts = {
            'rname':'Purchase Receipt',
            'rno':data['receipt_number'],
            'customer':data['supplier_name'],
            'cashier':'ME AM ME',
            'currency':'GH CEDIS',
            'rdate':data['receipt_time'],
        }
        print_invoice(data['items'], opts)
#edit view
class UpdateCashPurchase(JSONUpdateView):
    model = CashPurchase
    form = CashPurchaseForm
    user_required = True
#query view
class CashPurchases(JSONQueryView):
    model = CashPurchase

#Views for CreditPurchaseReturn model
#create view
class CreateCreditPurchaseReturn(JSONCreateMultipleView):
    model = CreditPurchaseReturn
    form = CreditPurchaseReturnForm
    expected_var = "purchases_returns"
    general_vars = ["invoice","supplier",'supplier_name']
    numbers = ['invoice_number','invoice_time','supplier_name']
    user_required = True

    def print_receipt(self,requestPost):
        data = super().print_receipt(requestPost)
        opts = {
            'rname':'Debit Note',
            'rno':data['invoice_number'],
            'customer':data['supplier_name'],
            'cashier':'ME AM ME',
            'currency':'GH CEDIS',
            'rdate':data['invoice_time'],
        }
        print_invoice(data['items'], opts)
#edit view
class UpdateCreditPurchaseReturn(JSONUpdateView):
    model = CreditPurchaseReturn
    form = CreditPurchaseReturnForm
    user_required = True
#query view
class CreditPurchaseReturns(JSONQueryView):
    model = CreditPurchaseReturn

#Views for CashPurchaseReturn model
#create view
class CreateCashPurchaseReturn(JSONCreateMultipleView):
    model = CashPurchaseReturn
    form = CashPurchaseReturnForm
    expected_var = "purchases_returns"
    general_vars = ["receipt",'cash','system','currency','supplier','supplier_name']
    numbers = ['receipt_number','receipt_time','supplier_name']
    user_required = True

    def print_receipt(self,requestPost):
        data = super().print_receipt(requestPost)

        opts = {
            'rname':'Cash Purchase Returned',
            'rno':data['receipt_number'],
            'customer':data['supplier_name'],
            'cashier':'ME AM ME',
            'currency':'GH CEDIS',
            'rdate':data['receipt_time'],
        }
        print_invoice(data['items'], opts)
#edit view
class UpdateCashPurchaseReturn(JSONUpdateView):
    model = CashPurchaseReturn
    form = CashPurchaseReturnForm
    user_required = True
#query view
class CashPurchaseReturns(JSONQueryView):
    model = CashPurchaseReturn
