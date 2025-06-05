# 🚀 Deploy no Vercel - Guia Completo

## 📋 Pré-requisitos

Antes de fazer o deploy, certifique-se de que você tem:

- [ ] Conta no [GitHub](https://github.com) (gratuita)
- [ ] Conta no [Vercel](https://vercel.com) (plano hobby gratuito)
- [ ] Todos os arquivos do site na pasta `recanto-arquitetura/`
- [ ] Todas as 35 imagens na pasta `images/` (ver `LISTA_IMAGENS.md`)

## 🔄 Método 1: Deploy Direto (Mais Simples)

### Passo 1: Preparar os Arquivos
1. **Organize todos os arquivos** em uma pasta chamada `recanto-arquitetura`
2. **Verifique a estrutura**:
   ```
   recanto-arquitetura/
   ├── index.html
   ├── css/style.css
   ├── js/script.js
   ├── images/ (35 imagens)
   ├── package.json
   ├── vercel.json
   └── outros arquivos...
   ```
3. **Teste localmente**: Abra `index.html` no navegador

### Passo 2: Deploy no Vercel
1. **Acesse** [vercel.com](https://vercel.com)
2. **Faça login** ou crie uma conta gratuita
3. **Clique em "Add New"** → **"Project"**
4. **Escolha "Browse All Templates"** → **"Deploy"**
5. **Arraste a pasta** `recanto-arquitetura` para a área de upload
6. **Configure o projeto**:
   - Project Name: `recanto-arquitetura`
   - Framework Preset: `Other`
   - Build Command: deixe vazio
   - Output Directory: deixe vazio
7. **Clique em "Deploy"**

### Passo 3: Verificação
- O Vercel irá processar os arquivos (1-2 minutos)
- Você receberá uma URL temporária (ex: `recanto-arquitetura-xyz.vercel.app`)
- **Teste todas as seções** do site
- **Verifique se as imagens carregam** corretamente

## 📂 Método 2: Via GitHub (Recomendado para Atualizações)

### Passo 1: Subir para o GitHub
1. **Acesse** [github.com](https://github.com) e faça login
2. **Clique em "New repository"**
3. **Configure o repositório**:
   - Repository name: `recanto-arquitetura`
   - Description: `Site institucional Recanto Arquitetura`
   - Público ou Privado (sua escolha)
   - ✅ Add a README file
4. **Clique em "Create repository"**

### Passo 2: Upload dos Arquivos
1. **Na página do repositório**, clique em "uploading an existing file"
2. **Arraste todos os arquivos** da pasta `recanto-arquitetura`
3. **Escreva uma mensagem**: "Upload inicial do site"
4. **Clique em "Commit changes"**

### Passo 3: Conectar com Vercel
1. **No Vercel**, clique em "Add New" → "Project"
2. **Connect Git Repository** → **GitHub**
3. **Autorize o Vercel** a acessar seu GitHub
4. **Selecione o repositório** `recanto-arquitetura`
5. **Configure o projeto**:
   - Framework Preset: `Other`
   - Build Command: deixe vazio
   - Output Directory: deixe vazio
6. **Clique em "Deploy"**

## ⚙️ Configurações Avançadas

### Domínio Personalizado (Opcional)
1. **No dashboard do Vercel**, clique no projeto
2. **Vá em "Settings"** → **"Domains"**
3. **Adicione seu domínio** (ex: `recantoarquitetura.com.br`)
4. **Configure o DNS** conforme instruções do Vercel

### Variáveis de Ambiente (Se Necessário)
- Para este projeto estático, não são necessárias
- Se adicionar funcionalidades futuras, configure em "Settings" → "Environment Variables"

## 🔍 Checklist Pós-Deploy

### Teste Funcional Completo
- [ ] **Home**: Logo, texto e botão funcionando
- [ ] **Sobre**: Fotos dos sócios carregando
- [ ] **Método**: 5 círculos com imagens visíveis
- [ ] **Projetos**: 6 projetos no grid
- [ ] **Modal**: Clique em "Detalhes" abre modal com 4 fotos
- [ ] **Avaliações**: Estrelas e depoimentos aparecem
- [ ] **Contato**: Formulário envia (teste com dados reais)
- [ ] **Menu Mobile**: Hambúrguer funciona em celular
- [ ] **Responsividade**: Teste em desktop, tablet e mobile

### Performance e SEO
- [ ] **Velocidade**: Site carrega em menos de 3 segundos
- [ ] **Imagens**: Todas otimizadas e carregando
- [ ] **Links**: Navegação suave funcionando
- [ ] **Fontes**: Compagnon Medium carregando corretamente

## 🛠️ Resolução de Problemas

### Problema: Imagens não carregam
**Solução**:
- Verifique se todas as 35 imagens estão na pasta `images/`
- Confirme os nomes exatos conforme `LISTA_IMAGENS.md`
- Certifique-se de que não há espaços ou caracteres especiais nos nomes

### Problema: Site não aparece
**Solução**:
- Verifique se o arquivo `index.html` está na raiz do projeto
- Confirme se o `vercel.json` está configurado corretamente
- Aguarde alguns minutos para propagação

### Problema: Menu mobile não funciona
**Solução**:
- Teste em um navegador diferente
- Verifique se o JavaScript está carregando
- Limpe o cache do navegador

### Problema: Formulário não envia
**Solução**:
- Para funcionalidade real, configure um serviço como Netlify Forms
- Atualmente funciona apenas como demonstração

## 🔄 Atualizações Futuras

### Via GitHub (Recomendado)
1. **Edite os arquivos** no GitHub ou localmente
2. **Faça commit** das alterações
3. **O Vercel redeploy** automaticamente

### Via Vercel Dashboard
1. **Acesse o projeto** no dashboard
2. **Clique em "Deployments"**
3. **Upload novos arquivos** se necessário

## 📞 Suporte

Se encontrar problemas:

1. **Documentação Vercel**: [vercel.com/docs](https://vercel.com/docs)
2. **GitHub Help**: [docs.github.com](https://docs.github.com)
3. **Verifique os logs** no dashboard do Vercel
4. **Community Forums**: Vercel e GitHub têm fóruns ativos

---

## 🎉 Parabéns!

Após seguir este guia, seu site estará online e acessível para o mundo todo. O Vercel oferece:

- ✅ **SSL automático** (HTTPS)
- ✅ **CDN global** (carregamento rápido)
- ✅ **Deploy automático** (via GitHub)
- ✅ **Domínio gratuito** (.vercel.app)
- ✅ **Analytics básico** (opcional)

**URL do seu site**: `https://recanto-arquitetura.vercel.app`
(ou o nome que você escolher)

---
**💡 Dica**: Salve a URL e compartilhe com seus clientes para mostrar o trabalho profissional do escritório Recanto!