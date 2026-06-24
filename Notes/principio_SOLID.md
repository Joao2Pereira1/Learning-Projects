# Princípios SOLID — Guia Prático

## 1. S — Single Responsibility Principle (Responsabilidade Única)
**Definição:**  
> Uma classe, módulo ou função deve ter apenas um motivo para mudar.  
> Isso significa que cada unidade de código deve fazer **apenas uma coisa**.

**Exemplo ruim (violando SRP):**
```python
class UserManager:
    def create_user(self, name, email):
        # lógica para criar o usuário
        pass

    def send_email(self, email, subject, body):
        # lógica para enviar email
        pass
```
> Aqui, a classe **cria usuários** e **envia e-mails** — duas responsabilidades diferentes.

**Exemplo bom (seguindo SRP):**
```python
class UserManager:
    def create_user(self, name, email):
        pass

class EmailService:
    def send_email(self, email, subject, body):
        pass
```

---

## 2. O — Open/Closed Principle (Aberto para extensão, fechado para modificação)
**Definição:**  
> O código deve estar aberto para **extensão**, mas fechado para **modificação**.  
> É melhor adicionar novos comportamentos estendendo classes ou implementando interfaces, em vez de alterar código já existente.

**Exemplo ruim (violando OCP):**
```python
class PaymentProcessor:
    def process_payment(self, type):
        if type == "credit":
            print("Processando crédito")
        elif type == "pix":
            print("Processando PIX")
```
> Sempre que surgir um novo método de pagamento, você tem que editar a classe.

**Exemplo bom (seguindo OCP):**
```python
class PaymentMethod:
    def pay(self):
        pass

class CreditCard(PaymentMethod):
    def pay(self):
        print("Processando crédito")

class Pix(PaymentMethod):
    def pay(self):
        print("Processando PIX")

def process_payment(payment: PaymentMethod):
    payment.pay()
```
> Agora é só criar uma nova classe para novos métodos de pagamento sem mexer no código existente.

---

## 3. L — Liskov Substitution Principle (Princípio da substituição de Liskov)
**Definição:**  
> Objetos de uma superclasse devem poder ser substituídos por objetos de suas subclasses **sem quebrar o código**.

**Exemplo ruim (violando LSP):**
```python
class Bird:
    def fly(self):
        print("Voando")

class Penguin(Bird):
    def fly(self):
        raise Exception("Pinguins não voam!")
```
> Substituir `Bird` por `Penguin` quebra o código.

**Exemplo bom (seguindo LSP):**
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Voando")

class Penguin(Bird):
    def swim(self):
        print("Nadando")
```
> Agora cada tipo de pássaro só tem comportamentos que realmente executa.

---

## 4. I — Interface Segregation Principle (Segregação de Interfaces)
**Definição:**  
> Uma classe não deve ser forçada a implementar métodos que não vai usar.  
> Prefira várias interfaces específicas em vez de uma única interface genérica gigante.

**Exemplo ruim (violando ISP):**
```python
class Machine:
    def print(self): pass
    def scan(self): pass
    def fax(self): pass

class OldPrinter(Machine):
    def print(self): pass
    def scan(self): pass  # Não faz sentido
    def fax(self): pass   # Não faz sentido
```

**Exemplo bom (seguindo ISP):**
```python
class Printer:
    def print(self): pass

class Scanner:
    def scan(self): pass

class Fax:
    def fax(self): pass

class OldPrinter(Printer):
    def print(self): pass
```

---

## 5. D — Dependency Inversion Principle (Inversão de Dependência)
**Definição:**  
> Módulos de alto nível não devem depender de módulos de baixo nível;  
> ambos devem depender de **abstrações**.  
> Detalhes devem depender de abstrações, não o contrário.

**Exemplo ruim (violando DIP):**
```python
class MySQLDatabase:
    def connect(self):
        pass

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Depende diretamente de MySQL
```

**Exemplo bom (seguindo DIP):**
```python
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        pass

class UserService:
    def __init__(self, db: Database):
        self.db = db
```
> Agora, o `UserService` pode funcionar com MySQL, PostgreSQL ou qualquer outro banco.

---

✅ **Resumo:**
| Princípio | O que evita | Benefício |
|-----------|-------------|-----------|
| SRP | Classes “faz-tudo” | Mais clareza e manutenção |
| OCP | Alterações constantes no código base | Extensibilidade |
| LSP | Subclasses que quebram código | Polimorfismo seguro |
| ISP | Interfaces com métodos inúteis | Flexibilidade |
| DIP | Acoplamento rígido a implementações | Testabilidade e troca fácil de dependências |
