from owlready2 import *

onto = get_ontology("http://www.example.org/teste.owl")

'''
1. **Definir Classes:**
   - Crie classes para representar os principais conceitos, como `Livro`, `Autor` e `Categoria`.

2. **Estabelecer Hierarquia:**
   - Estabeleça uma hierarquia entre as classes, por exemplo, `Livro` pode ser uma subclasse de `Obra`, e `Autor` pode ser uma subclasse de `Pessoa`.   
'''
class Obra(Thing):
   namespace = onto

class Pessoa(Thing):
   namespace = onto

class Categoria(Thing):
   namespace = onto

class Livro(Obra):
   ...

class Autor(Pessoa):
   ...


'''
3. **Definir Propriedades:**
   - Defina propriedades para conectar as classes, como a propriedade `escritoPor` entre `Livro` e `Autor`.
'''

class escritoPor(ObjectProperty):
   namespace = onto
   domain = [Livro]
   range = [Autor]

class ehDaCategoria(ObjectProperty):
   namespace = onto
   domain = [Livro]
   range = [Categoria]

'''
4. **Adicionar Indivíduos:**
   - Adicione alguns indivíduos (instâncias) à ontologia, como alguns livros específicos, autores conhecidos e categorias de livros.
'''

autor1 = Autor("Bob")
livro1 = Livro("Clean_Code")
categoria1 = Categoria("Tecnologia")

livro1.escritoPor.append(autor1)
livro1.ehDaCategoria.append(categoria1)

'''
6. **Salvar e Carregar:**
   - Salve a ontologia em um arquivo e carregue-a novamente para garantir que o processo de serialização e desserialização funcione corretamente.
'''

onto.save("teste.owl", format="rdfxml")

'''
7. **Consulta Dinâmica:**
   - Modifique a ontologia dinamicamente adicionando um novo livro, autor ou categoria e faça consultas para verificar se as alterações foram refletidas corretamente.
'''