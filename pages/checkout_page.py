from selene import have
from selene.support.shared.jquery_style import s


class CheckOutPage:

    def _agree_terms(self):
        s("#uniform-cgv").click()

    def _proceed_summary_step(self):
        s("a[class*='btn-default standard-checkout']").click()

    def _proceed_address_step(self):
        s("button[name='processAddress']").click()

    def _complete_shipping_step(self):
        self._agree_terms()
        s("button[name='processCarrier']").click()

    def _confirm_order(self):
        s("#cart_navigation > button[type='submit']").click()

    def proceed_checkout_steps(self):
        self._proceed_summary_step()
        self._proceed_address_step()
        self._complete_shipping_step()
        return self

    def bank_wire_status(self):
        return s("[class='cheque-indent']")

    def pay_check_status(self):
        return s("[class='alert alert-success']")

    def confirm_with_bank_wire(self):
        s(".bankwire").click()
        self._confirm_order()
        return self

    def confirm_with_pay_check(self):
        s(".cheque").click()
        self._confirm_order()
        return self





