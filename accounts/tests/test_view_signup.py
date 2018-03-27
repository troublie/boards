from django.test import TestCase
from django.urls import reverse_lazy, resolve  # reverse_lazy é o correto, não o reverse do pacote core
from accounts.views import signup  # importa a view signup que criamos e vamos realizar o teste nela
from ..forms import SignUpForm
from django.contrib.auth.models import User
from ..views import signup


# Create your tests here.

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse_lazy('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        # url = reverse_lazy('signup')
        # response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')  # define a URL absoluta que deve ser checada contra
        self.assertEquals(view.func,
                          signup)  # checa se ambas são iguais (a do request e a que será redirecionada, no caso a variavel view

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email,
        password1, password2
        '''
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)



class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse_lazy('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)  # aqui enviamos um POST com as informações, iremos testar um login
        self.home_url = reverse_lazy(
            'home')  # aqui definimos a URL home, pois no nosso caso será utilizada depois do cadastro para redir

    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse_lazy('signup')
        self.response = self.client.post(url, '{}', '{}')  # envia um dictionary vazio

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())

