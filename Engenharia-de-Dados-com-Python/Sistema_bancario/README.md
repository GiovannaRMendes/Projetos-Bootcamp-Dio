# Sistema bancário

A atividade visa colocar em prática, mais especificamente, conhecimentos em python com operações em uma conta bancária. Vale ressaltar que, deve-se seguir as seguintes regras:

- Depósito:
    - Apenas valores positivos;
    - Argumentos posicionais como parâmetros e retorna 2 valores.

- Saque:
    - Não pode sacar mais do que há na conta;
    - Há um limite de 3 saques ao dia;
    - Não pode sacar um valor maior que 500 reais;
    - Todos os argumentos passados no parâmetro são nomeados.

- Extrato/Exibir o extrato:
    - Há um formato específico para exibir o extrato, sendo ele: 
    ```f'<Nome da operação>: R$ {<valor>:.2f}\n'```;
    - Recebe o ```saldo``` como argumento posicional e o ```extrato```, nomeado.

- Criar usuário:
    - Recebe, como parâmetro: nome, CPF, data de nascimento e endereço (sendo este com seu formato específico apresentado no código).

- Criar conta:
    - Deve haver o cadastro do usuário antes de vinculá-lo a uma conta;
    - Recebe, como parâmetro: agência, número da conta e o usuário/cliente vinculado.

- Listar contas:
    - Apresentar o titular, a agência e o número da conta.