from selenium import webdriver


def before_all(context):
    context.browser=webdriver.Chrome()
    context.browser.implicitly_wait(1)
    context.server_url='http://127.0.0.1:8000/accounts/login/'


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
