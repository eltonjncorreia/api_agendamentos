# API Sistema de Agendamentos

Sistema de agendamentos.

[![Build Status](https://travis-ci.org/eltonjncorreia/eventex.svg?branch=master)](https://travis-ci.org/eltonjncorreia/eventex)

## Como desenvolver?

1.  Clone o repositório.
2.  Crie um virtualenv com Python 3.6.3
3.  Ative o virtualenv.
4.  Instale as dependências.
5.  Configure a instância com o .env
6.  Execute os testes.

``` console
git clone git@github.com:eltonjncorreia/api_agendamentos.git sdaAPI
cd sdaAPI
python -m venv .sdaAPI
source .sdaAPI/bin/activate
pip install -r requirements.txt
python manage.py test


```
## Como rodar a API?

1. Execute o comando python manage.py para migraçoes
2. Crie uma senha de usuarios, somente super usuarios teram acesso a POST, PUT, DELETE.
3. Rode o servidor local


``` console
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

