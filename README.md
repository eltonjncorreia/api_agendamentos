# API Sistema de Agendamentos

Sistema de agendamentos.


## Como desenvolver?

1.  Clone o repositório.
2.  Crie um virtualenv com Python 3.6.3
3.  Ative o virtualenv.
4.  Instale as dependências.
5.  Execute os testes.

``` console
git clone https://github.com/eltonjncorreia/api_agendamentos.git sdaAPI
cd sdaAPI
python -m venv .sdaAPI
source .sdaAPI/bin/activate
pip install -r requirements.txt
python manage.py test

```

## Como rodar a API Local?

1. Execute as migraçoes
2. Crie uma senha de usuarios, somente super usuarios teram acesso a POST, PUT, DELETE.
3. Rode o servidor local


``` console
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```


# Como acessar a documentação da API

1. Realize o login com o usuario recem criado.
2. Com o servidor local rodando acesse a url da documentação.
3. Outra forma de acessar a documentação.


```console
http://localhost:8000/admin/
http://localhost:8000/docs/
http://localhost:8000/


```

# Acessar localmente a API atraves das seguintes urls
```console
GET     http://localhost:8000/agendamentos/
POST    http://localhost:8000/agendamentos/agendar/
PUT     http://localhost:8000/agendamentos/remarcar/id/
DELETE  http://localhost:8000/agendamentos/cancelar/id/
GET     http://localhost:8000/agendamentos/detalhes/id/

```

