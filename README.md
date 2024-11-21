# TocLoc

### Crie um Ambiente Virtual para isolar as bibliotecas e dependências do projeto

- python -m venv venv
- 
>Nota: Só vai ser necessário rodar esse comando acima na primeira vez, quando a pasta venv já tiver criada, mantenha ativa com o comando abaixo.

#### Para ativar o ambiente virtual 
- venv\Scripts\activate
  
#### Para desativar o ambiente virtual 
- deactivate

### Faz a instalação das bibioltecas utilizadas no projeto
 - pip install -r requirements.txt 

### Verificar alterações nos Models do Django
 - python manage.py makemigrations 

### Aplica as migrações criadas no Banco de dados
- python manage.py migrate

### Inicia o servidor de desenvolvimento do Django
- python manage.py runserver

