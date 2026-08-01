import streamlit as st

# 1. Configuração da página (Deve ser o primeiro comando Streamlit)
st.set_page_config(
    page_title="Processamento de Dados & Automação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Personalizado para Design Minimalista e Limpo
st.markdown("""
    <style>
    /* Ocultar elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fontes e espaçamento geral */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1F2937;
    }
    
    /* Estilo dos títulos */
    .title-main {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        color: #1E3A8A;
    }
    
    .subtitle-main {
        font-size: 1.2rem;
        text-align: center;
        color: #4B5563;
        margin-bottom: 2.5rem;
    }
    
    /* Cartões de Serviços */
    .service-card {
        background-color: #F9FAFB;
        border: 1px solid #E5E7EB;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    /* Centralizar chamadas de contato */
    .contact-section {
        background-color: #F3F4F6;
        padding: 2rem;
        border-radius: 8px;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho (Hero Section)
st.markdown('<h1 class="title-main">Soluções em Processamento de Dados & Automação</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-main">Transformamos dados brutos em decisões inteligentes para a sua empresa.</p>', unsafe_allow_html=True)

st.divider()

# 4. Seção Nossos Serviços (Com as 2 Imagens)
st.markdown("### Nossos Serviços")
st.write("Ajudamos pequenas empresas a eliminarem tarefas manuais e otimizarem a tomada de decisão com dados precisos.")

col1, col2 = st.columns(2)

with col1:
    # Espaço para a Imagem 1
    # Substitua 'https://via.placeholder.com/600x400' pelo caminho local da sua imagem ex: 'imagens/servico1.jpg'
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80", 
        caption="Automação e Integração de Dados",
        use_container_width=True
    )
    st.markdown("""
    <div class="service-card">
        <h4>1. Automação de Processos</h4>
        <p>Elimine rotinas repetitivas no Excel ou sistemas internos. Criamos fluxos automáticos de coleta, validação e estruturação de dados.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Espaço para a Imagem 2
    # Substitua pela sua imagem ex: 'imagens/servico2.jpg'
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80", 
        caption="Dashboards e Relatórios Estratégicos",
        use_container_width=True
    )
    st.markdown("""
    <div class="service-card">
        <h4>2. Tratamento e Análise de Dados</h4>
        <p>Limpeza, organização e consolidação das suas bases de dados para relatórios gerenciais claros e orientados a resultados.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. Seção Por Que Escolher Nossa Empresa
st.markdown("### Por que automatizar seus dados conosco?")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**⚡ Agilidade**\n\nRedução drástica no tempo de execução de relatórios.")
with c2:
    st.markdown("**🎯 Precisão**\n\nEliminação de erros manuais de digitação e cálculo.")
with c3:
    st.markdown("**🔒 Segurança**\n\nProcessamento confiável e sigilo absoluto sobre os dados.")

# 6. Seção de Contato (Ideal para converter visitantes do Google Meu Negócio)
st.markdown("""
<div class="contact-section">
    <h2>Fale Conosco</h2>
    <p>Pronto para simplificar a gestão de dados da sua empresa?</p>
    <p>📧 <strong>E-mail:</strong> contato@suaempresa.com.br</p>
    <p>📱 <strong>WhatsApp:</strong> (00) 99999-9999</p>
    <p>📍 Atendemos presencialmente e online.</p>
</div>
""", unsafe_allow_html=True)