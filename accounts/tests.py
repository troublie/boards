from django.test import TestCase
from django.urls import reverse_lazy, resolve #reverse_lazy é o correto, não o reverse do pacote core
from .views import signup #importa a view signup que criamos e vamos realizar o teste nela

# Create your tests here.

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse_lazy('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/') #define a URL absoluta que deve ser checada contra
        self.assertEquals(view.func, signup) #checa se ambas são iguais (a do request e a que será redirecionada, no caso a variavel view
