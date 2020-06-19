from selene.support.conditions import be

from pages.fragments.navigation_fragment import NavigationFragment


def test_user_can_logout_after_registration(register_user):
    NavigationFragment().click_logout_button()
    NavigationFragment().sign_in_button().should(be.visible)


def test_user_can_login_after_registration(register_user):
    NavigationFragment().click_logout_button() \
        .login_with(*register_user)
    NavigationFragment().logout_button().should(be.visible)
