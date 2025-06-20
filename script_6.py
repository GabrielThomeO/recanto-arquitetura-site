# 7. Lista simples de nomes das imagens
nomes_imagens_txt = """LISTA DE NOMES DAS 35 IMAGENS NECESSÁRIAS
===========================================

LOGOS (3 arquivos):
- logo_recanto_header.png
- recanto_home_logo.png
- logo_recanto_footer.png

SOBRE (2 arquivos):
- foto_socio1.png
- foto_socio2.png

MÉTODO (5 arquivos):
- metodo_estudo.png
- metodo_anteprojeto.png
- metodo_executivo.png
- metodo_detalhamento.png
- metodo_execucao.png

PROJETOS GRID (6 arquivos):
- projeto1.png
- projeto2.png
- projeto3.png
- projeto4.png
- projeto5.png
- projeto6.png

PROJETO 1 MODAL (4 arquivos):
- projeto1_foto1.png
- projeto1_foto2.png
- projeto1_foto3.png
- projeto1_foto4.png

PROJETO 2 MODAL (4 arquivos):
- projeto2_foto1.png
- projeto2_foto2.png
- projeto2_foto3.png
- projeto2_foto4.png

PROJETO 3 MODAL (4 arquivos):
- projeto3_foto1.png
- projeto3_foto2.png
- projeto3_foto3.png
- projeto3_foto4.png

PROJETO 4 MODAL (4 arquivos):
- projeto4_foto1.png
- projeto4_foto2.png
- projeto4_foto3.png
- projeto4_foto4.png

PROJETO 5 MODAL (4 arquivos):
- projeto5_foto1.png
- projeto5_foto2.png
- projeto5_foto3.png
- projeto5_foto4.png

PROJETO 6 MODAL (4 arquivos):
- projeto6_foto1.png
- projeto6_foto2.png
- projeto6_foto3.png
- projeto6_foto4.png

TOTAL: 35 IMAGENS
Todas devem estar na pasta: images/"""

# Salvar lista simples
with open('NOMES_IMAGENS.txt', 'w', encoding='utf-8') as f:
    f.write(nomes_imagens_txt)

print("✅ Lista simples de nomes criada com sucesso!")