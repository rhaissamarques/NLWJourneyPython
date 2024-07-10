Essa aplicação foi desenvolvida no evento NLW Journey da Rocketseat, com o intuito de desenvolver as minhas habilidades em Python.
O projeto é um sistema para organizar viagens à trabalho ou lazer. O usuário pode criar uma viagem com nome, data de início e data de fim. Dentro da viagem, o usuário pode planejar suas atividades de cada dia.

O projeto conta com 5 tabelas, sendo elas:
1. trips
2. participants
3. links
4. emails_to_invite
5. activities

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/e9e37f77-dd2f-4929-a61f-4202f0cae636" alt="Tabelas no DBeaver">

Como o intuito é desenvolver o backend da aplicação, não foi criado uma página web com o formulário, mas fique livre para desenvolver se esse for seu intuito. Por hora, para alimentarmos as tabelas, usaremos o postman.

 * Criando uma viagem
Para criar uma viagem precisamos de um método POST contento:
1. destination
2. start_date
3. end_date
4. owner_name
5. owner_email
6. emails_to_invite

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/17e27d57-941e-418e-8e53-f740d3b44c39" alt="Simulacao de dados no postman">

Feito isso, a tabela será populada com os dados dessa viagem.

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/17658115-5abe-4f08-823b-c44289afc1cc" alt="Tabela populada com dados ficticios no DBeaver">

  * Encontrando uma viagem usando o tripId

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/49079b14-9618-41d0-8c59-bde476ef3cd7" alt="Busca de viagem no postman">

E com isso temos no retorno todos os dados da nossa viagem

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/74f17124-8d59-42c1-b1f1-984140ba0f24" alt="Retorno da busca de viagem no postman">

  * Confirmando uma viagem
Com o mesmo tripId da viagem criada, podemos confirmá-la com o tripId/confirm

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/7a4e6aac-1310-494b-bb30-e8adc30f2e5b" alt="Confirmando a viagem anterior no postman">

Essa requisição não nos retorna nada, porém, viagens que foram confirmadas apresentam o número 1 no campo status. Podemos checar isso tanto no DBeaver quando no próprio postman repetindo o passo anterior e checando o campo status.

  * Criando links da viagem.
Usando o tripId da nossa viagem, podemos inserir nela links de coisas que queremos fazer, locais que queremos visitar, hotéis que queremos nos hospedar. Para isso no body da requisição enviamos:
1. url
2. title
<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/b2d71f02-3bad-4a91-a574-7d148e5b48eb" alt="Inserindo links na viagem no postman">

  * Encontrando os links de viagem salvos anteriormente.
Para buscarmos os links de viagem salvos no tripId, tudo o que precisamos é uma requisição do tipo GET como na imagem abaixo.

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/9ff4c665-ea4a-40c8-99d5-5eae3512ba05" alt="Encontrando links na viagem no postman">

E o retorno dessa requisição é:

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/effa32cb-4b94-48d7-8252-4b557b1c7b5f" alt="Retorno dos links na viagem no postman">

  * Convidando pessoas para a viagem
Podemos fazer convites para nossos amigos, precisamos de duas informações:
1. email
2. nome

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/b790dbb7-fece-4b6c-9652-0bfd66d9737f" alt="Convidando amigos para viagem no postman">

O retorno dessa requisição é um participant_id
<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/fdb35779-8d9f-4393-8779-27ad6a9ed6ac" alt="Retorno do convite de amigos para viagem no postman">

  * Criando atividades para fazer na viagem
Novamente utilizando o tripId, podemos incluir atividades para realizar-mos na nossa viagem.
Precisamos passar:
1. occurs_at
2. title

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/f05e4423-d9ff-4fa3-bdbf-466946f441a6" alt="Criando atividades para a viagem no postman">

E o retorno dessa requisição é uma activityId

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/7ebaa35e-4c52-4cac-8333-6f513c2f1cc3" alt="Criando atividades para a viagem no postman">

  * Encontrando atividades pelo tripId
Se quisermos saber quais atividades estão marcadas para a nossa viagem, tudo o que precisamos fazer é buscar pelo tripId

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/a4a6ed1a-2d26-4f63-8eae-96bd021ea463" alt="Encontrando atividades para a viagem no postman">

E o retorno dessa requisição é:

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/d680a769-431d-40a7-aeae-e93d726ecc7c" alt="Retorno das atividades para a viagem no postman">

  * Ebcontrando os participantes da nossa viagem
Para ver as pessoas convidadas para nossa viagem podemos utilizar o tripId com o método GET da seguinte forma:

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/c3aacfb3-1772-4093-bd1e-8d8e6ea6c88f" alt="Encontrando participantes da viagem no postman">

E como retorno temos:

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/8f5caeea-2b34-41f7-a3d4-5ffe4113ae43" alt="Retorno dos participantes para a viagem no postman">

  * Confirmando os participantes da viagem
Para confirmar um participante que foi convidado para nossa viagem, precisamos do participantId

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/708ff11e-c4c0-47a3-9b0d-825b14e73617" alt="Confirmando os participantes para a viagem no postman">

Essa requisição não retorna nada, porém para checarmos se foi bem sucedida, podemos checar no método anterior que o campo is_confirmed estará marcado com o número 1.

  * Enviando um email com o id da viagem
Um email é enviado para o endereço de email cadastrado contendo um link com o id da viagem. Idealmente seria um botão para que a pessoa clique e com isso confirme a viagem, mas por enquanto o simples ato do usuário copiar o link e colar em seu navegador é o suficiente para que a viagem seja confirmada.

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/27ec4f1e-ca09-4b9a-a935-9cd54b80beb7" alt="Email ficticio contendo o link de confirmação da viagem">

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/32bd95ad-8a3e-4b5e-9bd4-a174518c7523" alt="Email ficticio aberto contendo o link de confirmação da viagem">

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/358c6321-a46e-4db8-90c6-a089c1accfe3" alt="Colando o link no navegador">

Nenhuma confirmação aparece no navegador por enquanto, mas no banco de dados a viagem referente ao id aceito é marcada como 1 no status. Ficando assim confirmada.

<img src="https://github.com/rhaissamarques/NLWJourneyPython/assets/85033834/64e905aa-ec25-4a94-bdfb-bc7eff5cc9c1" alt="Confirmação da viagem no DBeaver">



Essa é a nossa aplicação, espero que gostem, vários conceitos foram aprendidos e com certeza serão exercitados a partir de agora nessa jornada de Back-end com Python.
Obrigada pela visita.
