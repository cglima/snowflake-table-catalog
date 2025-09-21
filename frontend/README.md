# Frontend da Aplicação de Catálogo de Tabelas Snowflake

Este é o frontend da aplicação de catálogo de tabelas Snowflake, desenvolvido com React e TypeScript.

## Arquitetura

O projeto segue os princípios da Clean Architecture para garantir que o código seja organizado, testável e fácil de manter. A estrutura de pastas é a seguinte:

- **`src/domain`**: Contém a lógica de negócio principal da aplicação. Aqui ficam as entidades e as regras de negócio que são independentes de qualquer framework ou biblioteca.
- **`src/application`**: Contém os casos de uso da aplicação. Orquestra o fluxo de dados entre a camada de apresentação e a camada de domínio.
- **`src/infrastructure`**: Contém as implementações concretas das interfaces definidas na camada de aplicação, como chamadas a APIs externas.
- **`src/presentation`**: Contém os componentes React, hooks e tudo relacionado à interface do usuário.

## Como Começar

1.  **Instale as dependências:**
    ```bash
    npm install
    ```

2.  **Inicie o servidor de desenvolvimento:**
    ```bash
    npm start
    ```

    Isso iniciará a aplicação em modo de desenvolvimento e a abrirá em [http://localhost:3000](http://localhost:3000).

## Scripts Disponíveis

- **`npm start`**: Inicia a aplicação em modo de desenvolvimento.
- **`npm run build`**: Compila a aplicação para produção.
- **`npm test`**: Executa os testes.