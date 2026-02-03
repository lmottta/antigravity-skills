# ❓ Perguntas Frequentes (FAQ)

**Tem dúvidas?** Você não está sozinho! Aqui estão as respostas para as perguntas mais comuns sobre o Antigravity Awesome Skills.

---

## 🎯 Perguntas Gerais

### O que são "skills" exatamente?

Skills são arquivos de instruções especializados que ensinam os assistentes de IA a lidar com tarefas específicas. Pense neles como módulos de conhecimento especializado que sua IA pode carregar sob demanda.
**Analogia simples:** Assim como você pode consultar diferentes especialistas (um advogado, um médico, um mecânico), essas skills permitem que sua IA se torne especialista em diferentes áreas quando você precisar.

### Preciso instalar todas as mais de 250 skills?

**Não!** Quando você clona o repositório, todas as skills ficam disponíveis, mas sua IA só as carrega quando você as invoca explicitamente com `@nome-da-skill`.
É como ter uma biblioteca - todos os livros estão lá, mas você só lê os que precisa.
**Dica Pro:** Use os [Pacotes Iniciais (Bundles)](docs/BUNDLES.md) para instalar apenas o que combina com o seu papel.

### Quais ferramentas de IA funcionam com estas skills?

- ✅ **Claude Code** (Anthropic CLI)
- ✅ **Gemini CLI** (Google)
- ✅ **Codex CLI** (OpenAI)
- ✅ **Cursor** (AI IDE)
- ✅ **Antigravity IDE**
- ✅ **OpenCode**
- ⚠️ **GitHub Copilot** (suporte parcial via copiar e colar)

### Estas skills são gratuitas para usar?

**Sim!** Este repositório está licenciado sob a Licença MIT.

- ✅ Grátis para uso pessoal
- ✅ Grátis para uso comercial
- ✅ Você pode modificá-las

### As skills funcionam offline?

Os arquivos das skills são armazenados localmente no seu computador, mas seu assistente de IA precisa de uma conexão com a internet para funcionar.

---

## 🔒 Segurança e Confiança (Atualização V3)

### O que significam os Rótulos de Risco?

Classificamos as skills para que você saiba o que está executando:

- ⚪ **Seguro (Branco/Azul)**: Somente leitura, planejamento ou skills benignas.
- 🔴 **Risco (Vermelho)**: Skills que modificam arquivos (excluir), usam scanners de rede ou realizam ações destrutivas. **Use com cautela.**
- 🟣 **Oficial (Roxo)**: Mantido por fornecedores confiáveis (Anthropic, DeepMind, etc.).

### Estas skills podem hackear meu computador?

**Não.** Skills são arquivos de texto. No entanto, elas _instruem_ a IA a executar comandos. Se uma skill disser "exclua todos os arquivos", uma IA complacente pode tentar fazê-lo.
_Sempre verifique o rótulo de Risco e revise o código._

---

## 📦 Instalação e Configuração

### Onde devo instalar as skills?

O caminho universal que funciona com a maioria das ferramentas é `.agent/skills/`:

```bash
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

**Caminhos específicos por ferramenta:**

- Claude Code: `.claude/skills/`
- Gemini CLI: `.gemini/skills/`
- Cursor: `.cursor/skills/` ou raiz do projeto

### Isso funciona no Windows?

**Sim**, mas algumas skills "Oficiais" usam **links simbólicos** que o Windows gerencia mal por padrão.
Execute o git com:

```bash
git clone -c core.symlinks=true https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

Ou ative o "Modo Desenvolvedor" nas Configurações do Windows.
