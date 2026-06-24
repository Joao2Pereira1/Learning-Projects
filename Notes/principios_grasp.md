# 📚 Princípios GRASP

**GRASP** (*General Responsibility Assignment Software Patterns*) — são diretrizes para decidir **quem** (qual classe/objeto) deve ter **qual responsabilidade** no design de software orientado a objetos.

---

## 1. **Creator**
**Ideia:** Define quem deve criar uma instância de uma classe.  
**Regra:** Uma classe `A` deve criar objetos de classe `B` se:
- `A` **contém** `B`.
- `A` **usa** `B` fortemente.
- `A` tem os **dados necessários** para inicializar `B`.

💡 **Exemplo:**  
Em um sistema de pedidos, a classe `Pedido` cria objetos `ItemPedido` porque ela contém esses itens e tem os dados para criá-los.

---

## 2. **Information Expert** (*Especialista em Informação*)
**Ideia:** Atribuir responsabilidades a quem tem a **informação necessária** para cumpri-las.  
**Benefício:** Evita espalhar dados por várias classes e reduz dependências.

💡 **Exemplo:**  
Se precisamos calcular o preço total de um pedido, quem deve fazer isso é a classe `Pedido`, pois ela conhece os `ItemPedido` e seus preços.

---

## 3. **Low Coupling** (*Baixo Acoplamento*)
**Ideia:** Projetar para que classes tenham **poucas dependências** entre si.  
**Benefício:** Mudanças em uma classe afetam menos o resto do sistema, facilitando manutenção e testes.

💡 **Exemplo:**  
Em vez de a `UI` falar diretamente com o `BancoDeDados`, ela fala com um `Serviço`, que cuida do acesso.

---

## 4. **High Cohesion** (*Alta Coesão*)
**Ideia:** Cada classe ou módulo deve ter um **foco claro e único**.  
**Benefício:** Facilita entendimento, manutenção e reutilização.

💡 **Exemplo:**  
Uma classe `RelatorioPDF` só gera relatórios PDF, e não também envia emails ou calcula impostos.

---

## 5. **Controller**
**Ideia:** Criar um **objeto intermediário** para receber entradas externas (ex.: de UI ou rede) e coordenar a execução.  
**Benefício:** Evita que a camada de interface ou a lógica de negócio fiquem sobrecarregadas.

💡 **Exemplo:**  
Uma classe `PedidoController` recebe a ação “confirmar compra” da UI e coordena chamadas para `PedidoService`, `PagamentoService` e `EstoqueService`.

---

## 6. **Polymorphism** (*Polimorfismo*)
**Ideia:** Usar **interfaces** ou **classes abstratas** para lidar com variações de comportamento de forma uniforme.  
**Benefício:** Evita múltiplos `if/else` espalhados pelo código e facilita extensões.

💡 **Exemplo:**  
Um método `processarPagamento()` pode receber tanto `CartaoCredito` quanto `Pix` sem precisar saber o tipo exato — cada classe implementa seu próprio comportamento.

---

## 7. **Pure Fabrication** (*Fabricação Pura*)
**Ideia:** Criar uma **classe artificial** (que não representa algo do domínio) para cumprir responsabilidades que não se encaixam bem em nenhuma entidade.  
**Benefício:** Ajuda a manter **alta coesão** e **baixo acoplamento**.

💡 **Exemplo:**  
Uma classe `RepositorioUsuario` só para salvar e buscar usuários no banco, em vez de encher a classe `Usuario` de código de persistência.

---

## 8. **Indirection** (*Indireção*)
**Ideia:** Inserir um **objeto intermediário** para desacoplar duas classes.  
**Benefício:** Facilita mudanças e substituições.

💡 **Exemplo:**  
Usar um `Service Locator` ou `Message Broker` para que produtores e consumidores de mensagens não se conheçam diretamente.

---

## 9. **Protected Variations** (*Variações Protegidas*)
**Ideia:** **Proteger** partes do sistema de mudanças em outras partes, encapsulando pontos de variação.  
**Benefício:** Reduz impacto de alterações e facilita evolução.

💡 **Exemplo:**  
Acessar banco de dados através de uma interface `Repositorio` — se trocar MySQL por MongoDB, só a implementação muda, o resto do código continua igual.
