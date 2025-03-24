# Sistema bancário

A atividade visa colocar em prática, mais especificamente, conhecimentos em python com operações em uma conta bancária. Vale ressaltar que, deve-se seguir as seguintes regras:

- Depósito:
    - Apenas valores positivos.

- Saque:
    - Não pode sacar mais do que há na conta;
    - Há um limite de 3 saques ao dia;
    - Não pode sacar um valor maior que 500 reais.

- Extrato:
    - Há um formato específico para exibir o extrato, sendo ele: 
    ```f'<Nome da operação>: R$ {<valor>:.2f}\n'```