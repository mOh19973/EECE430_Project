from behave import given, when, then
from test.factories.user import UserFactory


@given('an anonymous user')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')

    u.save()


@when('I submit a valid login page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/accounts/login/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('submit').click()


@then('I am redirected to the login success page')
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/accounts/profile/foo')
    br.find_element_by_name('logout').click()


@when('I submit an invalid login page')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/accounts/login/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar-is-invalid')
    br.find_element_by_name('submit').click()


@then('I am redirected to the login fail page')
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/accounts/login/')
