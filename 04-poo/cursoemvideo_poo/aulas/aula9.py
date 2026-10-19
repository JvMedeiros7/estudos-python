# Encapsulamento 

# Visa manter a integridade do sistema, protegendo o estado interno do objeto contra interferência externa não regulamentada.

# Exemplo: Controle Remoto

# Todo controle remoto tem botões que permitem ao usuário interagir com a TV, mas o usuário não precisa saber como a TV funciona internamente para usá-la. O controle remoto encapsula(= Capsula) a complexidade da TV, fornecendo uma interface simples e intuitiva para o usuário.

# Principais vantagens:

# Segurança e Controle: O encapsulamento permite que você controle o acesso aos dados e métodos de um objeto, garantindo que apenas partes autorizadas do código possam modificar seu estado interno.

# Facilidade de Manutenção: Ao encapsular a lógica interna de um objeto, você pode alterar sua implementação sem afetar o código externo que depende dele. Isso facilita a manutenção e a evolução do sistema.

# Flexibilidade e Reutilização: Objetos encapsulados podem ser reutilizados em diferentes contextos, pois sua interface pública permanece consistente, mesmo que a implementação interna mude.

# Redução de efeitos colaterais: O encapsulamento ajuda a reduzir efeitos colaterais indesejados, pois limita o acesso direto aos dados internos de um objeto, evitando que outras partes do código interfiram de maneira inesperada.

# Para realizar essa proteção, precisamos entender:

# Visibilidade dos atributos e métodos: Em Python, você pode controlar a visibilidade de atributos e métodos usando convenções de nomenclatura. Por exemplo, prefixar um atributo com um único sublinhado (_) indica que ele é "protegido" e não deve ser acessado diretamente fora da classe. Prefixar com dois sublinhados (__) cria um nome de atributo "privado", tornando-o menos acessível.

# Acesso aos dados protegidos: Para acessar atributos protegidos ou privados, você pode fornecer métodos públicos (getters e setters) que permitem ler ou modificar esses atributos de forma controlada.

# Existem 3 tipos de visibilidade:

# Public (+): Atributos e métodos públicos podem ser acessados de qualquer lugar, tanto dentro quanto fora da classe.

# No python quando o atributo for público , ele não terá nenhum sublinhado antes do nome do atributo. Por exemplo, um atributo público chamado "nome" seria declarado como "self.nome".

# Protected (#): Atributos e métodos protegidos são indicados por um único sublinhado ( _ "Em python") e devem ser acessados apenas dentro da classe e suas subclasses. No entanto, ainda podem ser acessados fora da classe, mas é desencorajado.

# Quando o atributo for protegido, ele terá um único sublinhado antes do nome do atributo. Por exemplo, um atributo protegido chamado "idade" seria declarado como "self._idade".

# Private (-): Atributos e métodos privados são indicados por dois sublinhados ( __ "Em python") e não podem ser acessados diretamente fora da classe. Eles são destinados apenas para uso interno da classe.

# Quando o atributo for privado, ele terá dois sublinhados antes do nome do atributo. Por exemplo, um atributo privado chamado "senha" seria declarado como "self.__senha".

# Consenting Adults: Liberdade com Responsabilidade. Em Python, a visibilidade é mais uma convenção do que uma restrição rígida. Os desenvolvedores são incentivados a seguir essas convenções para manter a integridade do código, mas ainda têm a liberdade de acessar atributos e métodos protegidos ou privados se necessário.

# No lugar de criar barreiras de acesso, o Python adota a filosofia de "consenting adults" (adultos consentidos), que significa que os desenvolvedores são responsáveis por seguir as convenções de visibilidade e respeitar a intenção do código, mesmo que tecnicamente possam acessar atributos e métodos protegidos ou privados.


# Parte 2 : 

 # Métodos acessores (Getters e Setters):

# Getters e Setters são métodos que permitem acessar e modificar atributos de um objeto de forma controlada, mantendo o encapsulamento.

