import json

# Mapeamento completo e manual focado na "ideia" da skill em Português
IDEIA_SKILLS = {
    "2d-games": "Criação de jogos 2D: sprites, física, mapas de tiles e câmeras.",
    "3d-games": "Desenvolvimento de jogos 3D: renderização, shaders e física avançada.",
    "3d-web-experience": "Experiências imersivas em 3D para web usando Three.js e WebGL.",
    "ab-test-setup": "Configuração estratégica de testes A/B com foco em métricas de sucesso.",
    "active-directory-attacks": "Análise de segurança em ambientes Active Directory e vetores de ataque.",
    "address-github-comments": "Gestão eficiente de comentários em Pull Requests via linha de comando.",
    "agent-evaluation": "Benchmarks e testes para medir a confiabilidade de agentes de IA.",
    "agent-manager-skill": "Gerenciamento de múltiplos agentes locais usando tmux e sessões CLI.",
    "agent-memory-mcp": "Sistema de memória persistente e buscável para agentes agênticos.",
    "agent-memory-systems": "Arquitetura de memória para contexto de longo prazo em assistentes de IA.",
    "agent-tool-builder": "Construção de ferramentas eficientes para integração de agentes com sistemas externos.",
    "ai-agents-architect": "Design e arquitetura de agentes IA autônomos e sistemas multi-agente.",
    "ai-product": "Transformação de modelos de IA em produtos escaláveis e prontos para o mercado.",
    "ai-wrapper-product": "Estratégias para criar produtos de valor sobre APIs de IA (OpenAI, Anthropic).",
    "algolia-search": "Implementação e otimização de busca ultra-rápida com Algolia.",
    "algorithmic-art": "Criação de arte generativa e algoritmos visuais usando p5.js.",
    "analytics-tracking": "Design de sistemas de rastreio de dados para decisões baseadas em evidências.",
    "api-documentation-generator": "Automação de documentação técnica para APIs de fácil consumo.",
    "api-fuzzing-bug-bounty": "Testes de fuzzing em APIs para descoberta de vulnerabilidades de segurança.",
    "api-patterns": "Padrões robustos para design de APIs (REST, GraphQL) e tratamento de erros.",
    "api-security-best-practices": "Segurança em APIs: autenticação, throttling e proteção contra ataques.",
    "app-builder": "Orquestrador para criação de aplicações full-stack a partir de prompts.",
    "app-store-optimization": "Otimização de visibilidade e conversão em lojas de aplicativos (ASO).",
    "architecture": "Framework de decisão para arquitetura de software e análise de trade-offs.",
    "autonomous-agent-patterns": "Padrões de design para agentes que codificam e operam de forma autônoma.",
    "autonomous-agents": "Sistemas de IA que planejam, executam ferramentas e corrigem erros sozinhos.",
    "avalonia-layout-zafiro": "Layouts modernos com Avalonia UI usando o padrão Zafiro.",
    "avalonia-viewmodels-zafiro": "Padrões de ViewModel e navegação reativa para apps desktop.",
    "avalonia-zafiro-development": "Diretrizes de desenvolvimento desktop multiplataforma com Avalonia.",
    "aws-penetration-testing": "Testes de intrusão e auditoria de segurança em infraestrutura AWS.",
    "aws-serverless": "Construção de apps sem servidor usando Lambda, API Gateway e S3.",
    "azure-functions": "Desenvolvimento e escala de funções serverless na nuvem Azure.",
    "backend-dev-guidelines": "Padrões rigorosos de backend: arquitetura em camadas e segurança.",
    "bash-linux": "Domínio de terminal Linux, scripts bash e automação de sistemas.",
    "behavioral-modes": "Adaptação de comportamento da IA para diferentes fases do projeto.",
    "blockrun": "Capacidades extras para IA: geração de imagens e dados em tempo real.",
    "brainstorming": "Planejamento e ideação criativa antes do início do desenvolvimento.",
    "brand-guidelines": "Aplicação de identidade visual e tipografia consistente em artefatos.",
    "broken-authentication": "Testes de vulnerabilidades em sessões e fluxos de login.",
    "browser-automation": "Automação de navegadores para testes de UI e raspagem de dados.",
    "browser-extension-builder": "Criação de extensões para Chrome e Firefox com foco em utilidade.",
    "bullmq-specialist": "Gerenciamento de filas de tarefas assíncronas de alta performance.",
    "bun-development": "Uso do runtime Bun para execução de JS/TS ultra-rápida.",
    "burp-suite-testing": "Interceptação e análise de tráfego web para auditoria de segurança.",
    "busybox-on-windows": "Execução de utilitários UNIX em ambientes Windows.",
    "canvas-design": "Geração de documentos visuais (.png, .pdf) via código.",
    "cc-skill-continuous-learning": "Estratégias de aprendizado contínuo para desenvolvedores de IA.",
    "cc-skill-project-guidelines-example": "Exemplos de diretrizes de projeto para consistência de código.",
    "cc-skill-strategic-compact": "Visão estratégica compacta para gerenciamento de código.",
    "claude-code-guide": "Guia mestre para uso eficiente do Claude Code no terminal.",
    "clean-code": "Princípios de código limpo e manutenível para o mundo real.",
    "clerk-auth": "Implementação rápida de autenticação e gestão de usuários com Clerk.",
    "clickhouse-io": "Padrões de banco de dados analítico de alta performance.",
    "cloud-penetration-testing": "Segurança em nuvem: testes de intrusão em AWS, Azure e GCP.",
    "code-review-checklist": "Lista sistemática para revisão de código de alta qualidade.",
    "codex-review": "Revisão de código profissional com geração automática de changelog.",
    "coding-standards": "Padrões universais de codificação para TS/JS e React.",
    "competitor-alternatives": "Estratégia de páginas de comparação para SEO e Growth.",
    "computer-use-agents": "Criação de agentes que operam computadores como seres humanos.",
    "concise-planning": "Geração de checklists atômicos e claros para tarefas de código.",
    "content-creator": "Criação de conteúdo de marketing otimizado para SEO com voz de marca.",
    "context-window-management": "Gestão eficiente do limite de contexto de LLMs para evitar erros.",
    "context7-auto-research": "Busca automática de documentação técnica atualizada.",
    "conversation-memory": "Sistemas de memória para manter o contexto em chats longos.",
    "copy-editing": "Revisão e refinamento técnico de textos de marketing.",
    "copywriting": "Textos persuasivos focados em conversão e gatilhos mentais.",
    "core-components": "Padrões de sistemas de design e bibliotecas de componentes.",
    "crewai": "Orquestração de equipes de agentes IA com papéis definidos.",
    "d3-viz": "Visualização de dados interativa e complexa com d3.js.",
    "daily-news-report": "Relatórios diários automatizados de tecnologia e notícias.",
    "database-design": "Arquitetura de dados resiliente em bancos SQL e NoSQL.",
    "deployment-procedures": "Procedimentos seguros para deploy e rollback em produção.",
    "design-orchestration": "Fluxos de design que conectam ideação e execução técnica.",
    "discord-bot-architect": "Arquitetura de bots profissionais para Discord.",
    "dispatching-parallel-agents": "Execução paralela de agentes para tarefas independentes.",
    "doc-coauthoring": "Fluxo estruturado para co-autoria de documentação técnica.",
    "docker-expert": "Conteinerização profissional e otimização de imagens Docker.",
    "documentation-templates": "Templates para READMEs e documentação amigável para IA.",
    "docx": "Manipulação profissional de documentos do Word via código.",
    "email-sequence": "Criação de fluxos de e-mails automatizados e lucrativos.",
    "email-systems": "Configuração de infraestrutura de e-mail de alta entregabilidade.",
    "environment-setup-guide": "Onboarding técnico e configuração de ambiente de desenvolvimento.",
    "ethical-hacking-methodology": "Abordagem sistemática para hacking ético e segurança.",
    "exa-search": "Busca semântica avançada e descoberta de conteúdo via API.",
    "executing-plans": "Execução guiada de planos de implementação com pontos de revisão.",
    "file-organizer": "Organização inteligente de arquivos e estrutura de diretórios.",
    "file-path-traversal": "Detecção de falhas de segurança em caminhos de arquivos.",
    "file-uploads": "Gestão profissional de uploads e armazenamento em nuvem (S3, R2).",
    "finishing-a-development-branch": "Encerramento de tasks: merge, PR e limpeza de branch.",
    "firebase": "Backend rápido e escalável com foco em tempo real.",
    "firecrawl-scraper": "Conversão de sites inteiros em dados estruturados para IA.",
    "form-cro": "Otimização de taxas de conversão em formulários de leads.",
    "free-tool-strategy": "Estratégia de ferramentas gratuitas para aquisição de usuários.",
    "frontend-design": "Interfaces modernas com estética refinada e alta qualidade técnica.",
    "frontend-dev-guidelines": "Guia de desenvolvimento frontend: React, performance e tipos.",
    "frontend-patterns": "Padrões de design de interfaces e gerenciamento de estado.",
    "game-art": "Criação e pipeline de arte visual para jogos.",
    "game-audio": "Design de som e integração de áudio adaptativo para jogos.",
    "game-design": "Princípios de game design: mecânicas, balanceamento e psicologia.",
    "game-development": "Orquestrador central para desenvolvimento de jogos multiplataforma.",
    "gcp-cloud-run": "Escala de aplicações containerizadas no Google Cloud Run.",
    "geo-fundamentals": "Otimização para mecanismos de busca por IA (Generative Engine Opt).",
    "git-pushing": "Fluxo organizado de commits e publicações no Git.",
    "github-workflow-automation": "Automação total de processos no GitHub via CI/CD e IA.",
    "graphql": "Design de APIs flexíveis e performáticas usando GraphQL.",
    "html-injection-testing": "Vulnerabilidades de injeção de conteúdo em páginas web.",
    "hubspot-integration": "Integração profunda com CRM e APIs do HubSpot.",
    "i18n-localization": "Estratégias para internacionalização e suporte multi-idioma.",
    "idor-testing": "Testes de falhas de controle de acesso a objetos (IDOR).",
    "inngest": "Fluxos de trabalho duráveis e agendamento de tarefas sem servidor.",
    "interactive-portfolio": "Construção de portfólios que convertem visitantes em clientes.",
    "internal-comms": "Criação de comunicados internos profissionais e claros.",
    "javascript-mastery": "Domínio técnico profundo do ecossistema JavaScript.",
    "kaizen": "Cultura de melhoria contínua e refatoração constante de software.",
    "langfuse": "Observabilidade e monitoramento de aplicações baseadas em LLM.",
    "langgraph": "Criação de fluxos complexos e cíclicos com agentes de IA.",
    "last30days": "Pesquisa rápida de tendências recentes em fontes de dados ao vivo.",
    "launch-strategy": "Estratégia de lançamento de produtos e ferramentas digitais.",
    "lint-and-validate": "Controle automático de qualidade e análise estática de código.",
    "linux-privilege-escalation": "Escalação de privilégios e auditoria de sistemas Linux.",
    "linux-shell-scripting": "Automação de servidores com shell script de produção.",
    "llm-app-patterns": "Padrões de arquitetura para apps robustos de inteligência artificial.",
    "loki-mode": "Automação total de desenvolvimento: do PRD ao código pronto.",
    "marketing-ideas": "Growth hacking e ideias de aquisição para SaaS.",
    "marketing-psychology": "Ciência comportamental aplicada a decisões de marketing.",
    "mcp-builder": "Criação de servidores Model Context Protocol para IAs.",
    "metasploit-framework": "Uso profissional do Metasploit para testes de intrusão.",
    "micro-saas-launcher": "Desenvolvimento e escala rápida de pequenos SaaS (Indie Hacker).",
    "mobile-design": "Design e engenharia mobile-first para iOS e Android.",
    "mobile-games": "Criação de jogos mobile focados em performance e bateria.",
    "moodle-external-api-development": "Extensão de APIs e web services para o ecossistema Moodle.",
    "multi-agent-brainstorming": "Revisão coletiva de ideias usando múltiplos agentes especialistas.",
    "multiplayer": "Desenvolvimento de jogos multiplayer e sincronismo de rede.",
    "neon-postgres": "Banco de dados Postgres serverless com suporte a branches.",
    "nestjs-expert": "Especialista no framework NestJS para backends empresariais.",
    "network-101": "Fundamentos de redes para auditoria e configuração de servidores.",
    "nextjs-best-practices": "Domínio do framework Next.js e renderização no servidor.",
    "nextjs-supabase-auth": "Fluxos de autenticação seguros com Next.js e Supabase.",
    "nodejs-best-practices": "Padrões de ouro para desenvolvimento backend com Node.js.",
    "nosql-expert": "Modelagem e performance em bancos NoSQL (DynamoDB, Cassandra).",
    "notebooklm": "Integração do Claude com fontes de dados do Google NotebookLM.",
    "notion-template-business": "Criação e venda de templates Notion como produto digital.",
    "obsidian-clipper-template-creator": "Personalização de captura de conteúdo para o Obsidian.",
    "onboarding-cro": "Otimização do fluxo de boas-vindas para novos usuários.",
    "page-cro": "Análise e otimização de conversão para páginas web específicas.",
    "paid-ads": "Estratégia e criativos para anúncios pagos em redes sociais.",
    "parallel-agents": "Uso de múltiplos agentes em paralelo para tarefas complexas.",
    "paywall-upgrade-cro": "Otimização de paywalls e fluxos de upgrade em apps.",
    "pc-games": "Desenvolvimento de jogos para PC e consoles.",
    "pdf": "Manipulação programática de arquivos PDF (extração e criação).",
    "pentest-checklist": "Lista completa de verificações para testes de intrusão.",
    "pentest-commands": "Referência rápida de comandos para testes de segurança.",
    "performance-profiling": "Identificação e correção de gargalos de performance no código.",
    "personal-tool-builder": "Criação de ferramentas para resolver problemas do dia a dia.",
    "plaid-fintech": "Integração bancária e fluxos financeiros com a API Plaid.",
    "plan-writing": "Planejamento estruturado de tarefas complexas.",
    "planning-with-files": "Gerenciamento de contexto longo via arquivos de plano (.md).",
    "playwright-skill": "Automação total de navegadores com Playwright.",
    "popup-cro": "Uso estratégico de popups para conversão sem ruído.",
    "powershell-windows": "Automação e administração de sistemas Windows com PowerShell.",
    "pptx": "Criação e edição automática de apresentações em PowerPoint.",
    "pricing-strategy": "Design de preços e modelos de monetização para software.",
    "prisma-expert": "Uso avançado do ORM Prisma para gestão de banco de dados.",
    "privilege-escalation-methods": "Segurança ofensiva: métodos de elevação de privilégios.",
    "product-manager-toolkit": "Kit de ferramentas completo para gestão de produtos (PM).",
    "production-code-audit": "Auditoria profunda de código para nível corporativo.",
    "programmatic-seo": "Estratégia de SEO em escala usando dados estruturados.",
    "prompt-caching": "Otimização de custos de IA usando cache de prompts.",
    "prompt-engineer": "Engenharia de prompts para resultados precisos e determinísticos.",
    "prompt-library": "Biblioteca de prompts testados para diversas categorias.",
    "python-patterns": "Padrões de design modernos para aplicações Python.",
    "rag-engineer": "Engenharia de RAG para busca inteligente sobre documentos.",
    "rag-implementation": "Implementação técnica de pipelines RAG e bancos vetoriais.",
    "react-patterns": "Padrões de componentes e hooks para React moderno.",
    "react-ui-patterns": "Interfaces resilientes: estados de carregamento e erro no React.",
    "receiving-code-review": "Melhores práticas para aceitar e implementar revisões de código.",
    "red-team-tactics": "Táticas de ataque simulado para testar defesas de rede.",
    "referral-program": "Growth via indicação: programas de afiliados e convites.",
    "remotion-best-practices": "Criação de vídeos programáticos usando React e Remotion.",
    "requesting-code-review": "Como solicitar revisões de código de forma produtiva.",
    "research-engineer": "Rigor científico aplicado à pesquisa técnica e engenharia.",
    "salesforce-development": "Desenvolvimento profissional no ecossistema Salesforce.",
    "schema-markup": "Dados estruturados para dominar os resultados de busca (Google).",
    "scroll-experience": "Criação de experiências web baseadas em rolagem (parallax).",
    "security-review": "Revisão de segurança em código antes do merge.",
    "segment-cdp": "Gestão de dados de usuários com Segment CDP.",
    "senior-architect": "Diretrizes para arquitetura de sistemas escaláveis e limpos.",
    "senior-fullstack": "Engenharia fullstack completa com foco em entrega profissional.",
    "seo-audit": "Check-up completo de SEO técnico e de conteúdo.",
    "seo-fundamentals": "Os pilares fundamentais para crescer e dominar buscas orgânicas.",
    "server-management": "Gestão e escala de servidores de produção.",
    "shodan-reconnaissance": "Uso do Shodan para reconhecimento de ativos na internet.",
    "shopify-apps": "Desenvolvimento de apps profissionais para Shopify.",
    "shopify-development": "Criação de temas e extensões personalizadas para e-commerce.",
    "signup-flow-cro": "Otimização do registro para reduzir o abandono de usuários.",
    "skill-creator": "Ferramenta para criar e atualizar skills de IA.",
    "skill-developer": "Desenvolvimento de novas capacidades para o Claude Code.",
    "slack-bot-builder": "Automação de processos corporativos via bots de Slack.",
    "slack-gif-creator": "Criação de GIFs personalizados para Slack via código.",
    "smtp-penetration-testing": "Testes de segurança em servidores de e-mail.",
    "social-content": "Estratégia de marketing em redes sociais via IA.",
    "software-architecture": "Design de sistemas focados em qualidade e manutenibilidade.",
    "sql-injection-testing": "Proteção contra ataques de injeção SQL em bancos de dados.",
    "sqlmap-database-pentesting": "Uso automatizado do SQLMap para auditoria de banco.",
    "ssh-penetration-testing": "Segurança em acessos remotos via protocolo SSH.",
    "stripe-integration": "Pagamentos, assinaturas e fluxos financeiros com Stripe.",
    "subagent-driven-development": "Desenvolvimento guiado por sub-agentes especialistas.",
    "supabase-postgres-best-practices": "Performance máxima no banco de dados Supabase.",
    "systematic-debugging": "Depuração inteligente de bugs difíceis.",
    "tailwind-patterns": "UI de alta qualidade usando o framework Tailwind CSS.",
    "tavily-web": "Busca web otimizada para agentes de IA.",
    "tdd-workflow": "Desenvolvimento orientado a testes (TDD) passo a passo.",
    "telegram-bot-builder": "Automação e robôs para a plataforma Telegram.",
    "telegram-mini-app": "Web apps nativos carregados dentro do Telegram.",
    "templates": "Scaffolding completo para novos projetos em segundos.",
    "test-driven-development": "Criação de software robusto através de testes prévios.",
    "test-fixing": "Correção sistemática de testes falhos em pipelines.",
    "testing-patterns": "Padrões de testes: mocks, stubs e testes de integração.",
    "theme-factory": "Criação de temas visuais consistentes para artefatos.",
    "top-web-vulnerabilities": "Referência das 100 maiores vulnerabilidades da web.",
    "trigger-dev": "Tarefas em background e fluxos baseados em eventos.",
    "twilio-communications": "Comunicação via SMS, Voz e WhatsApp usando a API Twilio.",
    "typescript-expert": "Domínio total de tipagem e performance com TypeScript.",
    "ui-ux-pro-max": "Design system e inteligência visual de nível superior.",
    "upstash-qstash": "Mensageria e filas serverless com Upstash.",
    "using-git-worktrees": "Gestão de múltiplas branches simultâneas com worktrees.",
    "using-superpowers": "Guia inicial para encontrar e usar superpoderes IA.",
    "vercel-deployment": "Publicação e escala global de apps na nuvem Vercel.",
    "react-best-practices": "Guia de excelência React: performance e arquitetura.",
    "verification-before-completion": "Checagem rigorosa antes de declarar uma tarefa concluída.",
    "viral-generator-builder": "Ferramentas que geram compartilhamento e viralidade.",
    "voice-agents": "Criação de interfaces de voz naturais com agentes de IA.",
    "voice-ai-development": "Desenvolvimento do motor de voz para aplicações conversacionais.",
    "voice-ai-engine-development": "Arquitetura avançada de voz para agentes em tempo real.",
    "vr-ar": "Princípios de desenvolvimento para Realidade Virtual e Aumentada.",
    "vulnerability-scanner": "Scan avançado de vulnerabilidades em sistemas e dependências.",
    "web-artifacts-builder": "Criação de mini-apps interativos dentro do chat da IA.",
    "web-design-guidelines": "Review de UI focado em acessibilidade e padrões modernos.",
    "web-games": "Jogos para navegador usando WebGPU e frameworks modernos.",
    "web-performance-optimization": "Otimização de Web Vitals e velocidade de carregamento.",
    "webapp-testing": "Testes de ponta a ponta (E2E) em aplicações web.",
    "windows-privilege-escalation": "Segurança ofensiva em sistemas Windows.",
    "wireshark-analysis": "Análise profunda de tráfego de rede com Wireshark.",
    "wordpress-penetration-testing": "Auditoria de segurança em ecossistemas WordPress.",
    "workflow-automation": "Automação de processos complexos e fluxos duráveis.",
    "writing-plans": "Escrita de planos de ação claros para tarefas de engenharia.",
    "writing-skills": "Criação técnica de novos superpoderes e capacidades.",
    "xlsx": "Gestão e análise de planilhas de Excel via código.",
    "zapier-make-patterns": "Automação no-code profissional com Zapier e Make."
}

def translate_name_idea(id, original_name):
    return original_name.replace('-', ' ').title()

def get_idea(id, desc):
    # Se temos a ideia manual, usamos ela. Caso contrário, fazemos uma tradução genérica curta.
    if id in IDEIA_SKILLS:
        return IDEIA_SKILLS[id]
    
    # Fallback para skills n\u00e3o listadas (seguran\u00e7a)
    return desc[:100] + "..." if len(desc) > 100 else desc

def get_category_pt(cat, path):
    cat_map = {
        'game-development': 'Jogos',
        'security': 'Segurança',
        'cybersecurity': 'Segurança',
        'ai-agent': 'Agentes IA',
        'development': 'Programação',
        'marketing': 'Growth',
        'design': 'Design & UX',
        'workflow': 'Produtividade',
        'integrations': 'APIs & Bancos',
        'testing': 'Qualidade',
        'maker': 'Maker',
        'uncategorized': 'Geral',
        'app-builder': 'Construtor'
    }
    
    p = path.lower()
    if 'security' in p or 'pentest' in p or 'vulnerability' in p: return 'Segurança'
    if 'game' in p: return 'Jogos'
    if 'marketing' in p or 'seo' in p or 'cro' in p: return 'Growth'
    if 'ai' in p or 'agent' in p or 'llm' in p or 'prompt' in p: return 'Agentes IA'
    if 'design' in p or 'ui' in p or 'ux' in p or 'css' in p: return 'Design & UX'
    if 'git' in p or 'linux' in p or 'cloud' in p: return 'Infraestrutura'
    if 'react' in p or 'node' in p or 'api' in p or 'dev' in p: return 'Programação'
    
    return cat_map.get(cat, 'Geral')

# Carregar skills
with open('skills_index.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

# Processar todas as skills focando na "Ideia"
processed_skills = []
for s in skills:
    processed_skills.append({
        'id': s['id'],
        'name': s['name'].replace('-', ' ').title(),
        'description': get_idea(s['id'], s['description']),
        'category': get_category_pt(s['category'], s['path']),
        'risk': s.get('risk', 'unknown'),
        'original_name': s['name']
    })

categories = sorted(list(set(s['category'] for s in processed_skills)))

# HTML Premium
html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Antigravity Skills - Superpoderes IA</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #050811;
            --surface: #0c1221;
            --card: #151c2f;
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --text-main: #ffffff;
            --text-sec: #94a3b8;
            --border: rgba(255, 255, 255, 0.08);
            --gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: var(--bg);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 90% 90%, rgba(168, 85, 247, 0.15) 0%, transparent 40%);
            background-attachment: fixed;
        }}

        header {{
            padding: 8rem 2rem 4rem;
            text-align: center;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 1rem;
            letter-spacing: -3px;
            background: linear-gradient(to bottom, #fff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .description {{
            color: var(--text-sec);
            font-size: 1.3rem;
            max-width: 700px;
            margin: 0 auto 3rem;
        }}

        .search-container {{
            max-width: 700px;
            margin: 0 auto;
            position: relative;
        }}

        input {{
            width: 100%;
            background: rgba(26, 32, 44, 0.6);
            border: 1px solid var(--border);
            padding: 1.3rem 2rem 1.3rem 4rem;
            border-radius: 24px;
            color: #fff;
            font-size: 1.2rem;
            backdrop-filter: blur(20px);
            transition: 0.3s;
        }}

        input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 40px rgba(99, 102, 241, 0.3);
            outline: none;
        }}

        .search-icon {{
            position: absolute;
            left: 1.5rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.5rem;
            opacity: 0.4;
        }}

        .filters {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin: 2.5rem auto;
            max-width: 1000px;
        }}

        .filter-chip {{
            padding: 0.6rem 1.4rem;
            border-radius: 12px;
            background: var(--border);
            border: 1px solid transparent;
            cursor: pointer;
            color: var(--text-sec);
            font-weight: 600;
            font-size: 0.9rem;
            transition: 0.3s;
        }}

        .filter-chip:hover {{ color: #fff; background: rgba(255,255,255,0.1); }}
        .filter-chip.active {{
            background: var(--primary);
            color: #fff;
            box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        }}

        .content {{
            max-width: 1500px;
            margin: 0 auto 10rem;
            padding: 0 3rem;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 2.5rem;
        }}

        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 32px;
            padding: 3rem;
            display: flex;
            flex-direction: column;
            transition: 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at top left, rgba(99,102,241,0.1), transparent 70%);
            opacity: 0; transition: 0.4s;
        }}

        .card:hover {{
            transform: translateY(-12px);
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 30px 60px rgba(0,0,0,0.5);
        }}

        .card:hover::before {{ opacity: 1; }}

        .tag {{
            color: var(--primary);
            font-weight: 800;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 1.5rem;
        }}

        .title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1.2rem;
            line-height: 1.1;
        }}

        .idea {{
            color: var(--text-sec);
            font-size: 1.05rem;
            flex-grow: 1;
            margin-bottom: 3rem;
            font-weight: 400;
        }}

        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--border);
            padding-top: 2rem;
        }}

        .id {{
            font-family: monospace;
            color: var(--text-sec);
            font-size: 0.9rem;
            background: rgba(255,255,255,0.03);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s;
            position: relative;
        }}

        .id:hover {{
            background: rgba(99, 102, 241, 0.1);
            color: var(--primary);
        }}

        .toast {{
            position: fixed;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%);
            background: var(--primary);
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            font-weight: 600;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            opacity: 0;
            pointer-events: none;
            transition: 0.3s;
            z-index: 1000;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateX(-50%) translateY(-10px);
        }}

        .risk {{
            width: 12px; height: 12px; border-radius: 50%;
        }}

        .risk-safe {{ background: #10b981; box-shadow: 0 0 10px #10b981; }}
        .risk-risk {{ background: #f43f5e; box-shadow: 0 0 10px #f43f5e; }}
        .risk-official {{ background: #a855f7; box-shadow: 0 0 10px #a855f7; }}
        .risk-unknown {{ background: #475569; }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .card {{ animation: fadeInUp 0.5s ease-out forwards; }}

        @media (max-width: 768px) {{
            h1 {{ font-size: 2.5rem; }}
            .content {{ padding: 0 1.5rem; }}
            .grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>

<header>
    <h1>Antigravity Skills</h1>
    <p class="description">A ideia central de cada um dos {len(processed_skills)} superpoderes disponíveis para seu assistente de IA.</p>
    
    <div class="search-container">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" placeholder="Pesquisar por ideia, nome ou tecnologia...">
    </div>

    <div class="filters" id="filters">
        <div class="filter-chip active" data-cat="Todos">Todos</div>
        {' '.join([f'<div class="filter-chip" data-cat="{c}">{c}</div>' for c in categories])}
    </div>
</header>

<div class="content">
    <div class="grid" id="grid"></div>
</div>
<div id="toast" class="toast">Copiado para a área de transferência!</div>

<script>
    const data = {json.dumps(processed_skills)};
    const grid = document.getElementById('grid');
    const search = document.getElementById('searchInput');
    const filters = document.getElementById('filters');

    let currentCat = 'Todos';
    let currentSearch = '';

    function render() {{
        const filtered = data.filter(s => {{
            const matchesCat = currentCat === 'Todos' || s.category === currentCat;
            const matchesSearch = s.name.toLowerCase().includes(currentSearch.toLowerCase()) || 
                                s.description.toLowerCase().includes(currentSearch.toLowerCase()) ||
                                s.original_name.toLowerCase().includes(currentSearch.toLowerCase());
            return matchesCat && matchesSearch;
        }});

        grid.innerHTML = filtered.map((s, i) => `
            <div class="card" style="animation-delay: ${{i % 12 * 0.05}}s">
                <div class="tag">${{s.category}}</div>
                <div class="title">${{s.original_name}}</div>
                <div class="idea">${{s.description}}</div>
                <div class="footer">
                    <div class="id" onclick="copyToClipboard('@${{s.original_name}}')" title="Clique para copiar">@${{s.original_name}}</div>
                    <div class="risk risk-${{s.risk}}" title="Risco: ${{s.risk}}"></div>
                </div>
            </div>
        `).join('');
    }}

    function copyToClipboard(text) {{
        navigator.clipboard.writeText(text).then(() => {{
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2000);
        }});
    }}

    search.addEventListener('input', e => {{ currentSearch = e.target.value; render(); }});
    filters.addEventListener('click', e => {{
        if(e.target.dataset.cat) {{
            filters.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
            e.target.classList.add('active');
            currentCat = e.target.dataset.cat;
            render();
        }}
    }});

    render();
</script>

</body>
</html>
"""

with open('catalog.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Catálogo 'Ideia' finalizado com sucesso.")
