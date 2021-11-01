[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

# API Django REST Framework People Register

API que simula um controlador de registros de pessoas, permitindo ao client:
 * Cadastrar categorias em que uma pessoa poderá ser registrada;
 * Cadastrar e atualizar dados de uma nova pessoa no sistema;
 * Fazer upload de um arquivo de identificação de determinada pessoa cadastrada;
 * Visualizar todas as medias carregadas no sistema ou filtrar esses registros por cada pessoa registrada no sistema;
 * Consultar a auditoria das inclusões e atualizaçõe dos dados de uma pessoa ou a lista de auditoria do sistema;

## Endpoints:
* /admin/ -> administração site
* /type/ -> visualizar e cadastrar as categoria de uma pessoa;
* /mediatype/ -> visualizar os tipos de media de identificação permitidas no sistema;
* /person/ -> cadastrar e visualizar as pessoas registradas no sistema;
* /media/ -> cadastrar e visualizar os arquivos de identificação de cada pessoa;
* /audit/ -> vusualizar todas as auditorias do sistema;
* /listaudit/<int:pk>/ -> listar todas as auditorias para uma determinada pessoa do sistema;
* /listperson/<int:cpf>/ -> listar uma pessoa através do seu cpf;
* /listmedia/<int:pk>/ -> listar todas as medias através da chave ID da pessoa cadastrada;
* /swagger/ -> documentação da API 
* /redoc/ -> documentação da API 

## Funcionamento:
Ao iniciar a aplicação, os dados de PERSON TYPE e MEDIA TYPE serão automaticamente carregados com alguns valores defaut, sendo que o client poderá incluir novas categorias na tabela PERSON TYPE através do comando POST.
Com o sistema carregado, será possível registrar uma nova pessoa no sistema, informando o NAME, CPF, COMPANY e PERSON TYPE como dados obrigatórios e PHONE como dado opcional. 
Após o cadastro é possível visualizar o registro de auditoria no '/audit/' ou '/listaudit/<int:pk>/' através do ID da tabela PERSON, todas as pessoas registradas através da '/person/' ou listar somente os dados de uma pessoa através do '/listperson/<int:cpf>/', informando o CPF desejado. 
Através do comando PACTH, será possível atualizar os dados do registro de uma pessoa. Caso haja atualização do CPF, o mesmo será registrado na auditoria, ou quando houver uma atualização com o registro da pessoa, a base de dado de auditoria também será atualizada.
Com o cadastro de um indivíduo finalizado, será possível incluir uma mídia de identificação (foto ou biometria). O uploada se realiza através da URL '/media/', informando para qual pessoa cadastrada será vinculada a imagem e a aplicação converterá a imagem para a base64. A consulta das mídias poderá ser realizada pela '/listmedia/<int:pk>/' informando o ID da tabela PERSON.

## Estratégias:
* Por motivo de usabilidade, a própria aplicação realiza a conversão para um arquivo de 256kb;
* Para limitar o número de tipos de mídia (MEDIA TYPE), não foi disponibilizado um endpoint para realizar o POST nesta tabela;

## Informações de ambiente:
[requirements.txt](https://github.com/LucasAlbFar/Django_DRF_PeopleRegister/blob/main/api/requirements.txt)

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
