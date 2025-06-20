# Vou criar todos os arquivos necessários para o site Recanto Arquitetura

# 1. Arquivo HTML principal
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recanto - Arquitetura Contemporânea</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Header Fixo -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo-header">
                    <img src="images/logo_recanto_header.png" alt="Recanto Arquitetura" width="60" height="45">
                </div>
                <nav class="nav-desktop">
                    <a href="#home" class="nav-link">HOME</a>
                    <a href="#sobre" class="nav-link">SOBRE</a>
                    <a href="#metodo" class="nav-link">MÉTODO</a>
                    <a href="#projetos" class="nav-link">PROJETOS</a>
                    <a href="#contato" class="nav-link">CONTATO</a>
                </nav>
                <button class="menu-toggle" aria-label="Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
        <nav class="nav-mobile">
            <a href="#home" class="nav-link">HOME</a>
            <a href="#sobre" class="nav-link">SOBRE</a>
            <a href="#metodo" class="nav-link">MÉTODO</a>
            <a href="#projetos" class="nav-link">PROJETOS</a>
            <a href="#contato" class="nav-link">CONTATO</a>
        </nav>
    </header>

    <!-- Seção HOME -->
    <section id="home" class="section section-home">
        <div class="container">
            <div class="home-content">
                <div class="home-logo">
                    <img src="images/recanto_home_logo.png" alt="Recanto Home" class="logo-principal">
                </div>
                <h1 class="titulo-outline">RECANTO</h1>
                <p class="subtitulo">ARQUITETURA CONTEMPORÂNEA</p>
                <p class="home-texto">
                    Acreditamos que a boa arquitetura está acima de estilos ou modismos. Nosso compromisso é criar espaços funcionais, atemporais e que reflitam a personalidade de cada cliente, sempre com atenção aos detalhes e qualidade construtiva que transforma sonhos em realidade.
                </p>
                <button class="btn-cta" onclick="document.getElementById('projetos').scrollIntoView({behavior: 'smooth'})">
                    CONHECER PROJETOS
                </button>
            </div>
        </div>
    </section>

    <!-- Seção SOBRE -->
    <section id="sobre" class="section section-sobre">
        <div class="container">
            <h2 class="section-title">SOBRE</h2>
            <div class="sobre-content">
                <div class="sobre-fotos">
                    <div class="foto-socio">
                        <img src="images/foto_socio1.png" alt="Sócio 1" width="300" height="400">
                    </div>
                    <div class="foto-socio">
                        <img src="images/foto_socio2.png" alt="Sócio 2" width="300" height="400">
                    </div>
                </div>
                <div class="sobre-texto">
                    <p>
                        O escritório Recanto - Arquitetura Contemporânea foi fundado com a missão de criar espaços que transcendem tendências passageiras e se conectam profundamente com as necessidades e sonhos de nossos clientes. Nossa filosofia baseia-se na crença de que a verdadeira arquitetura vai além da estética, integrando funcionalidade, sustentabilidade e emoção em cada projeto.
                    </p>
                    <p>
                        Com uma equipe experiente e apaixonada pela excelência, desenvolvemos soluções arquitetônicas inovadoras que respeitam o contexto urbano e natural, sempre priorizando a qualidade construtiva e o bem-estar dos usuários. Cada projeto é uma oportunidade única de materializar visões e criar ambientes que inspiram e acolhem.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Seção MÉTODO -->
    <section id="metodo" class="section section-metodo">
        <div class="container">
            <h2 class="section-title">MÉTODO</h2>
            <div class="metodo-grid">
                <div class="metodo-item">
                    <div class="metodo-circulo">
                        <img src="images/metodo_estudo.png" alt="Estudo Preliminar" width="400" height="400">
                    </div>
                    <h3 class="metodo-nome">Estudo Preliminar</h3>
                </div>
                <div class="metodo-item">
                    <div class="metodo-circulo">
                        <img src="images/metodo_anteprojeto.png" alt="Anteprojeto" width="400" height="400">
                    </div>
                    <h3 class="metodo-nome">Anteprojeto</h3>
                </div>
                <div class="metodo-item">
                    <div class="metodo-circulo">
                        <img src="images/metodo_executivo.png" alt="Projeto Executivo" width="400" height="400">
                    </div>
                    <h3 class="metodo-nome">Projeto Executivo</h3>
                </div>
                <div class="metodo-item">
                    <div class="metodo-circulo">
                        <img src="images/metodo_detalhamento.png" alt="Detalhamento" width="400" height="400">
                    </div>
                    <h3 class="metodo-nome">Detalhamento</h3>
                </div>
                <div class="metodo-item">
                    <div class="metodo-circulo">
                        <img src="images/metodo_execucao.png" alt="Execução" width="400" height="400">
                    </div>
                    <h3 class="metodo-nome">Execução</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- Seção PROJETOS -->
    <section id="projetos" class="section section-projetos">
        <div class="container">
            <h2 class="section-title">PROJETOS</h2>
            <div class="projetos-grid">
                <div class="projeto-item" data-projeto="0">
                    <img src="images/projeto1.png" alt="Residência Contemporânea" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Residência Contemporânea</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
                <div class="projeto-item" data-projeto="1">
                    <img src="images/projeto2.png" alt="Loft Urbano" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Loft Urbano</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
                <div class="projeto-item" data-projeto="2">
                    <img src="images/projeto3.png" alt="Casa de Campo" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Casa de Campo</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
                <div class="projeto-item" data-projeto="3">
                    <img src="images/projeto4.png" alt="Escritório Comercial" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Escritório Comercial</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
                <div class="projeto-item" data-projeto="4">
                    <img src="images/projeto5.png" alt="Reforma Apartamento" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Reforma Apartamento</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
                <div class="projeto-item" data-projeto="5">
                    <img src="images/projeto6.png" alt="Casa Minimalista" width="600" height="400">
                    <div class="projeto-info">
                        <h3>Casa Minimalista</h3>
                        <button class="btn-detalhes">DETALHES</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Seção CONTATO -->
    <section id="contato" class="section section-contato">
        <div class="container">
            <h2 class="section-title">CONTATO</h2>
            <div class="contato-content">
                <div class="contato-form">
                    <form id="contactForm">
                        <div class="form-group">
                            <input type="text" id="nome" name="nome" placeholder="Nome" required>
                        </div>
                        <div class="form-group">
                            <input type="email" id="email" name="email" placeholder="Email" required>
                        </div>
                        <div class="form-group">
                            <input type="tel" id="telefone" name="telefone" placeholder="Telefone" required>
                        </div>
                        <div class="form-group">
                            <textarea id="mensagem" name="mensagem" placeholder="Mensagem" rows="5"></textarea>
                        </div>
                        <button type="submit" class="btn-enviar">ENVIAR MENSAGEM</button>
                    </form>
                </div>
                <div class="contato-info">
                    <div class="info-item">
                        <h3 class="info-label">WHATSAPP</h3>
                        <p class="info-data">12996462826</p>
                    </div>
                    <div class="info-item">
                        <h3 class="info-label">EMAIL</h3>
                        <p class="info-data">recantomineiroarquitetura@gmail.com</p>
                    </div>
                    <div class="info-item">
                        <h3 class="info-label">ENDEREÇO</h3>
                        <p class="info-data">Av. João Pinheiro, 607</p>
                    </div>
                    <div class="info-item">
                        <h3 class="info-label">INSTAGRAM</h3>
                        <p class="info-data">@recanto_arq</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Rodapé -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">
                    <img src="images/logo_recanto_footer.png" alt="Recanto Arquitetura" width="40" height="30">
                </div>
                <div class="footer-text">
                    <p>© 2025 Recanto Arquitetura Ltda.</p>
                    <p>Entre em contato para transformar seu sonho em realidade</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Modal de Projetos -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <button class="modal-close">&times;</button>
            <div class="modal-body">
                <h3 id="modal-title"></h3>
                <div class="modal-images">
                    <img id="modal-img1" src="" alt="" width="800" height="600">
                    <img id="modal-img2" src="" alt="" width="800" height="600">
                    <img id="modal-img3" src="" alt="" width="800" height="600">
                    <img id="modal-img4" src="" alt="" width="800" height="600">
                </div>
                <div class="modal-avaliacao">
                    <div class="estrelas">
                        <span>★★★★★</span>
                    </div>
                    <div class="cliente-info">
                        <h4 id="modal-cliente"></h4>
                        <p id="modal-depoimento"></p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="js/script.js"></script>
</body>
</html>"""

# Salvar o arquivo HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Arquivo index.html criado com sucesso!")