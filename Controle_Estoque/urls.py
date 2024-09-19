"""
URL configuration for Controle_Estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import HttpResponse

def page_home(request):
    return HttpResponse("Pagina Home!!!")

def page_sobre(request):
    return HttpResponse('''
    <h1>Sobre Nós</h1>

    <div>
        <p> Site focado no controle de estoque, que facilita a entrada e saída de materiais, além de permitir o acompanhamento do histórico de cada item.</p>
    </div>
   <div>
        <h2>Visão</h2>
        <p>Ser referência em soluções de controle de estoque, reconhecida pela inovação e qualidade de nossos serviços, contribuindo para o crescimento de nossos clientes.</p>
    </div>

    <div>
        <h2>Valores</h2>
        <ul>
            <li><strong>Inovação:</strong> Buscamos constantemente novas maneiras de melhorar nossos produtos.</li>
            <li><strong>Compromisso:</strong> Estamos sempre comprometidos com o sucesso dos nossos clientes.</li>
            <li><strong>Transparência:</strong> Agimos de forma clara e objetiva em todas as nossas ações.</li>
            <li><strong>Qualidade:</strong> Garantimos produtos e serviços de alto padrão.</li>
        </ul>
    </div>
    ''')

def page_perfil_usuario(request, userName):
    return HttpResponse(f'''
    <h1>Perfil do Usuário</h1>

    <div>
        <h2>Informações Pessoais</h2>
        <p><strong>Nome:</strong> {userName} </p>
        <p><strong>Email:</strong> {userName}@exemplo.com</p>
        <p><strong>Telefone:</strong> (35) 98765-4321</p>
        <p><strong>Endereço:</strong> Rua dos Exemplos, 456 - Bairro Fictício, Itajubá - MG</p>
    </div>

    <div>
        <h2>Detalhes da Conta</h2>
        <p><strong>Usuário:</strong> {userName} </p>
        <p><strong>Data de Criação:</strong> 10/02/2023</p>
        <p><strong>Status:</strong> Ativo</p>
    </div>

    <div>
        <h2>Preferências</h2>
        <p><strong>Idioma Preferido:</strong> Português</p>
        <p><strong>Notificações:</strong> Ativadas</p>
        <p><strong>Assinatura:</strong> Premium</p>
    </div>

    <div>
        <h2>Histórico de Ações</h2>
        <ul>
            <li>Login realizado em 15/09/2024 às 10:30</li>
            <li>Alteração de senha em 10/08/2024 às 14:45</li>
            <li>Atualização de endereço em 05/07/2024 às 16:20</li>
        </ul>
    </div>
    ''')

def page_contato(request):
    return HttpResponse('''
    <div>
        <h1>Contato</h1>
        
        <div>
            <h2>Equipe de Suporte</h2>
            <p>Se você tiver alguma dúvida ou precisar de suporte, entre em contato conosco pelos canais abaixo:</p>
            
            <div>
                <h3>Email:</h3>
                <p>suporte@controleestoque.com.br</p>
            </div>
            
            <div>
                <h3>Telefone:</h3>
                <p>(11) 4002-8922</p>
            </div>
        </div>
        
        <div>
            <h2>Endereço</h2>
            <p>Avenida Exemplo, 1234 - Bairro Avenida</p>
            <p>Itajubá - MG</p>
        </div>
        
        <div>
            <h2>Horário de Atendimento</h2>
            <p>Segunda a Sexta: 08h00 às 18h00</p>
            <p>Sábado: 09h00 às 13h00</p>
        </div>
    </div>
''')


urlpatterns = [
    path('', page_home),
    path('sobre/', page_sobre),
    path('user/<str:userName>', page_perfil_usuario),
    path('contato/', page_contato)
]
