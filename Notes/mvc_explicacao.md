# Padrão de Arquitetura **Model-View-Controller (MVC)**

O **Model-View-Controller (MVC)** é um padrão de arquitetura de software usado para organizar código separando responsabilidades em três camadas principais.

---

## 1. **Model** (Modelo)
- **Função**: Lida com os **dados** e a **lógica de negócio**.
- **Responsabilidades**:
  - Armazenar informações (por exemplo, dados de um banco de dados).
  - Processar regras de negócio (como cálculos ou validações).
- **Não** se preocupa com *como* os dados são exibidos.
- **Exemplo**:
  ```java
  public class Produto {
      private String nome;
      private double preco;

      public Produto(String nome, double preco) {
          this.nome = nome;
          this.preco = preco;
      }

      public double calcularDesconto(double percentual) {
          return preco - (preco * percentual / 100);
      }
  }
  ```

---

## 2. **View** (Visão)
- **Função**: É a **interface com o usuário**.
- **Responsabilidades**:
  - Mostrar os dados do *Model*.
  - Receber entrada do usuário (ex.: cliques, digitação).
- **Não** processa lógica de negócio — só mostra e coleta informações.
- **Exemplo**: Uma página HTML, uma tela JavaFX ou um formulário PyQt.

```html
<!-- Exemplo de View em HTML -->
<h1>Cadastro de Produto</h1>
<form>
    Nome: <input type="text" name="nome">
    Preço: <input type="number" name="preco">
    <button>Salvar</button>
</form>
```

---

## 3. **Controller** (Controlador)
- **Função**: Faz a **ponte** entre a *View* e o *Model*.
- **Responsabilidades**:
  - Receber comandos do usuário via View.
  - Decidir o que fazer e qual método do Model chamar.
  - Atualizar a View com novos dados.
- **Exemplo**:
  ```java
  public class ProdutoController {
      private Produto produto;

      public void salvarProduto(String nome, double preco) {
          produto = new Produto(nome, preco);
          System.out.println("Produto salvo: " + nome);
      }
  }
  ```

---

## **Fluxo de funcionamento do MVC**
1. O **usuário** interage com a **View** (ex.: clica num botão).
2. A **View** repassa o evento ao **Controller**.
3. O **Controller** atualiza o **Model** ou pede dados a ele.
4. O **Model** envia os dados atualizados.
5. A **View** mostra a nova informação ao usuário.

---

## **Vantagens do MVC**
- Separação clara de responsabilidades → código mais organizado e fácil de manter.
- Facilita testes e manutenção.
- Possibilita trocar a interface (*View*) sem alterar a lógica (*Model*).
