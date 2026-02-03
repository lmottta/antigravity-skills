# Registro de Alterações (Changelog)

Todas as mudanças notáveis na coleção **Antigravity Awesome Skills** são documentadas neste arquivo.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

---

---

---

## [3.4.0] - 27-01-2026 - "Inteligência de Voz e Categorização"

### Adicionado

- **Nova Skill**: `voice-ai-engine-development` - Kit completo para construção de agentes de voz em tempo real (OpenAI Realtime, Vapi, Deepgram, ElevenLabs).
- **Categorização**: Grande atualização no README apresentando uma tabela de resumo concisa de "Recursos e Categorias".

### Alterado

- **README**: Substituídas as listas de categorias carregadas de texto por uma tabela de resumo de alto nível.
- **Registro**: Sincronizada a contagem de skills genéricas (256) em toda a documentação.

### Colaboradores

- [@sickn33](https://github.com/sickn33) - Voice AI Engine (PR #33)
- [@community](https://github.com/community) - Iniciativa de Categorização (PR #32)

## [3.3.0] - 26-01-2026 - "Notícias e Pesquisa"

### Adicionado

- **Novas Skills**:
  - `last30days`: Pesquise qualquer tópico dos últimos 30 dias no Reddit + X + Web.
  - `daily-news-report`: Gere relatórios diários de notícias de múltiplas fontes.

### Alterado

- **Registro**: Atualizados `skills_index.json` e o registro do `README.md` (Total: 255 skills).

## [3.2.0] - 26-01-2026 - "Clareza e Consistência"

### Alterado

- **Refatoração de Skills**: Revisão significativa de `backend-dev-guidelines`, `frontend-design`, `frontend-dev-guidelines` e `mobile-design`.
  - **Consolidação**: Mesclada documentação fragmentada em arquivos `SKILL.md` únicos e autoritativos.
  - **Leis Finais**: Introduzidas seções de "Final Laws" para fornecer frameworks de decisão rígidos e não negociáveis.
  - **Simplificação**: Removidas dependências de arquivos externos para melhorar a recuperação de contexto para agentes de IA.

### Corrigido

- **Validação**: Corrigidos problemas críticos de formatação de frontmatter YAML em `seo-fundamentals`, `programmatic-seo` e `schema-markup` que bloqueavam a validação rigorosa.
- **Conflitos de Merge**: Resolvidos conflitos de artefatos de texto em skills de SEO.

## [3.1.0] - 26-01-2026 - "Estável e Determinístico"

### Corrigido

- **CI/CD Drift**: Resolvidos erros persistentes de "Mudanças não confirmadas" no CI, tornando o script de geração de índice determinístico (ordenação por nome + ID).
- **Sincronização de Registro**: Sincronizados `README.md` e `skills_index.json` para refletir com precisão todas as 253 skills.

### Adicionado (Restauração de Registro)

As seguintes skills agora estão corretamente indexadas e visíveis no registro:

- **Marketing e Crescimento**: `programmatic-seo`, `schema-markup`, `seo-fundamentals`, `form-cro`, `popup-cro`, `analytics-tracking`.
- **Segurança**: `windows-privilege-escalation`, `wireshark-analysis`, `wordpress-penetration-testing`, `writing-plans`.
- **Desenvolvimento**: `tdd-workflow`, `web-performance-optimization`, `webapp-testing`, `workflow-automation`, `zapier-make-patterns`.
- **Maker Tools**: `telegram-bot-builder`, `telegram-mini-app`, `viral-generator-builder`.

### Alterado

- **Documentação**: Adicionado `docs/CI_DRIFT_FIX.md` como referência canônica para resolver problemas de drift.
- **Orientação**: Atualizadas as contagens do `GETTING_STARTED.md` para corresponder ao registro completo (253+ skills).
- **Manutenção**: Atualizado `MAINTENANCE.md` com protocolos rigorosos para lidar com arquivos gerados.
