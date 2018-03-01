from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from varys.models import Transaction
from .forms import WithdrawForm

# Create your views here.
@login_required
def saque(request):
    #Se esse view está recebendo um POST, ou seja
    #já foi renderizado e o formulário completado
    if request.method == 'POST':
        #Copia o objeto de transação enviados via método POST
        transaction = Transaction(request.POST)

        #Se os dados foram preenchido corretamente
        if transaction.is_valid():
            return HttpResponseRedirect('/thanks/')
    #Se for a primeira vez que a página é renderizada
    else:
        #Cria uma transação vazia para ser preenchida
        transaction = WithdrawForm()

    return render(request, 'shell/app_shell.html',
                    {'is_withdraw': True,
                     'title': 'Saque',
                     'transaction': transaction})
