# 3. Arquivo JavaScript
js_content = """// Dados dos projetos
const projetos = [
    {
        nome: "Residência Contemporânea",
        cliente: "Maria Silva",
        depoimento: "Transformaram nossa casa em um lar perfeito. A atenção aos detalhes e qualidade do projeto superaram nossas expectativas. Cada ambiente foi pensado com carinho e funcionalidade.",
        imagens: [
            "images/projeto1_foto1.png",
            "images/projeto1_foto2.png", 
            "images/projeto1_foto3.png",
            "images/projeto1_foto4.png"
        ]
    },
    {
        nome: "Loft Urbano",
        cliente: "João Santos", 
        depoimento: "O design moderno e funcional criou um espaço único na cidade. Profissionais excepcionais e resultado incrível que superou todas as nossas expectativas.",
        imagens: [
            "images/projeto2_foto1.png",
            "images/projeto2_foto2.png",
            "images/projeto2_foto3.png", 
            "images/projeto2_foto4.png"
        ]
    },
    {
        nome: "Casa de Campo",
        cliente: "Ana Costa",
        depoimento: "Conseguiram harmonizar perfeitamente nossa necessidade de conforto com a beleza natural do ambiente. O resultado é uma casa que respira tranquilidade.",
        imagens: [
            "images/projeto3_foto1.png",
            "images/projeto3_foto2.png",
            "images/projeto3_foto3.png",
            "images/projeto3_foto4.png"
        ]
    },
    {
        nome: "Escritório Comercial", 
        cliente: "Pedro Oliveira",
        depoimento: "O projeto aumentou significativamente a produtividade da equipe. Ambiente profissional e inspirador que reflete a identidade da nossa empresa.",
        imagens: [
            "images/projeto4_foto1.png",
            "images/projeto4_foto2.png",
            "images/projeto4_foto3.png",
            "images/projeto4_foto4.png"
        ]
    },
    {
        nome: "Reforma Apartamento",
        cliente: "Carla Mendes",
        depoimento: "Renovaram completamente nosso apartamento respeitando nosso orçamento e prazo. Equipe nota 10! Cada detalhe foi executado com perfeição.",
        imagens: [
            "images/projeto5_foto1.png",
            "images/projeto5_foto2.png",
            "images/projeto5_foto3.png",
            "images/projeto5_foto4.png"
        ]
    },
    {
        nome: "Casa Minimalista",
        cliente: "Ricardo Alves",
        depoimento: "O conceito minimalista foi executado com perfeição. Cada espaço tem função definida e beleza atemporal que nos encanta todos os dias.",
        imagens: [
            "images/projeto6_foto1.png",
            "images/projeto6_foto2.png", 
            "images/projeto6_foto3.png",
            "images/projeto6_foto4.png"
        ]
    }
];

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    // Menu mobile
    setupMobileMenu();
    
    // Navegação suave
    setupSmoothNavigation();
    
    // Modal de projetos
    setupProjectModal();
    
    // Formulário de contato
    setupContactForm();
});

// Configurar menu mobile
function setupMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMobile = document.querySelector('.nav-mobile');
    
    menuToggle.addEventListener('click', function() {
        navMobile.classList.toggle('active');
        
        // Animação do botão hamburger
        const spans = menuToggle.querySelectorAll('span');
        if (navMobile.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(7px, 7px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(7px, -7px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
    
    // Fechar menu ao clicar em link
    const navLinks = navMobile.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMobile.classList.remove('active');
            const spans = menuToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        });
    });
}

// Configurar navegação suave
function setupSmoothNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                const headerHeight = 80; // Altura do header fixo
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Highlight da seção ativa na navegação
    window.addEventListener('scroll', function() {
        let current = '';
        const sections = document.querySelectorAll('.section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (pageYOffset >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
}

// Configurar modal de projetos
function setupProjectModal() {
    const modal = document.getElementById('modal');
    const modalClose = document.querySelector('.modal-close');
    const projetoItems = document.querySelectorAll('.projeto-item');
    
    // Abrir modal
    projetoItems.forEach(item => {
        const btnDetalhes = item.querySelector('.btn-detalhes');
        btnDetalhes.addEventListener('click', function(e) {
            e.stopPropagation();
            const projetoIndex = parseInt(item.dataset.projeto);
            openModal(projetoIndex);
        });
    });
    
    // Fechar modal
    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });
    
    // Fechar modal com ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
}

function openModal(projetoIndex) {
    const projeto = projetos[projetoIndex];
    const modal = document.getElementById('modal');
    
    // Preencher dados do modal
    document.getElementById('modal-title').textContent = projeto.nome;
    document.getElementById('modal-cliente').textContent = projeto.cliente;
    document.getElementById('modal-depoimento').textContent = projeto.depoimento;
    
    // Preencher imagens
    for (let i = 1; i <= 4; i++) {
        const img = document.getElementById('modal-img' + i);
        img.src = projeto.imagens[i-1];
        img.alt = projeto.nome + ' - Foto ' + i;
    }
    
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Configurar formulário de contato
function setupContactForm() {
    const form = document.getElementById('contactForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const telefone = document.getElementById('telefone').value;
        const mensagem = document.getElementById('mensagem').value;
        
        // Validação básica
        if (!nome || !email || !telefone) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }
        
        // Validação de email
        const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Por favor, insira um email válido.');
            return;
        }
        
        // Simular envio
        alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
        form.reset();
    });
}

// Efeitos de scroll
window.addEventListener('scroll', function() {
    const header = document.querySelector('.header');
    
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.15)';
    } else {
        header.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
    }
});

// Animações de entrada
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observar elementos para animação
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.projeto-item, .metodo-item, .sobre-content');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});"""

# Criar diretório JS se não existir
os.makedirs('js', exist_ok=True)

# Salvar o arquivo JavaScript
with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Arquivo JavaScript criado com sucesso!")