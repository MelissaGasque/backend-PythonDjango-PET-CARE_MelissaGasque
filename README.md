# PetCare
A linguagem utilizada é o Python e o framework Django. O Banco de dados utilizado é o sqlite3.  
Essa API permite a empresa PetCare ter maior controle e organização dos dados dos animais.  

| Endpoint                  | Verbo HTTP | Objetivo                                          |
|---------------------------|------------|---------------------------------------------------|
| /api/pets/                | POST       | Cadastrar pet                                     |
| /api/pets/                | GET        | Listar pet                                       |
| /api/pets/?trait=nome_da_trait ou /api/pets?trait=nome_da_trait | GET        | Filtragem de pets que possuem a trait passada por query param |
| /api/pets/<pet_id>/       | GET        | Busca de pet                                     |
| /api/pets/<pet_id>/       | PATCH      | Atualização de pet                               |
| /api/pets/<pet_id>/       | DELETE     | Deleção de pet                                   |
 
## Configuração do Ambiente Virtual (Opcional, mas recomendado)
### Crie um ambiente virtual
```
    python -m venv venv
```

### Ative o ambiente virtual
#### No Windows
```venv\Scripts\activate```
#### No Linux/Mac
```source venv/bin/activate```


## Instalar o Django:
```pip install django```

## Instalação das Dependencias
```pip install -r requirements.txt```

## Migrações e Aplicações
### Execute as migrações
```python manage.py makemigrations```
```python manage.py migrate```

### Inicie o servidor de desenvolvimento
```python manage.py runserver```




## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```
3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```

## Execução dos testes:

Tarefa 1:


```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

Tarefa 4

```shell
pytest --testdox -vvs tests/tarefas/tarefa_4/
```

<hr>

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_can_list_pets_with_pagination".

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/test_views.py::PetViewsTest::test_can_list_pets_with_pagination
```
--- 

Para executar todos os testes:
```shell
pytest --testdox -vvs
```
--- 
## Observação
Não existem testes isolados para a tarefa 2. As funcionalidades que devem ser testadas desta tarefa estão presentes nos testes da tarefa 3.