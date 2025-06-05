# 8. Criar pasta images e arquivo .gitkeep
import os

# Criar pasta images
os.makedirs('images', exist_ok=True)

# Criar arquivo .gitkeep para manter a pasta no Git
with open('images/.gitkeep', 'w') as f:
    f.write('# Esta pasta contém as 35 imagens necessárias para o site\n# Consulte LISTA_IMAGENS.md para detalhes completos')

print("✅ Pasta images criada com sucesso!")

# Listar todos os arquivos criados
print("\n📁 ESTRUTURA FINAL DO PROJETO:")
print("=" * 50)

import os
for root, dirs, files in os.walk('.'):
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if not file.startswith('.'):
            print(f'{subindent}{file}')

print("\n" + "=" * 50)
print("✅ SITE COMPLETO CRIADO COM SUCESSO!")
print("✅ Total de arquivos: HTML, CSS, JS + documentação")
print("✅ Pronto para adicionar as 35 imagens e fazer deploy!")
print("=" * 50)