
USER_ROLES_SETTINGS = (
    ['guest', 'Гость', '/admin'],
    ['operator', 'Оператор', 'vesovay:start'],
    ['admin', 'Администратор', 'sklad:start'],
    ['kladovschik', 'Кладовщик', 'sklad:start']
)

USER_ROLES_FOR_REDIRECTS_CHOICES = tuple([tuple(role[0:2]) for role in USER_ROLES_SETTINGS])
USER_SUCCESS_LOGIN_REDIRECTS_BY_USER_ROLE = {role[0]: role[2] for role in USER_ROLES_SETTINGS}