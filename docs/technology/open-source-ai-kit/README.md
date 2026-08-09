# Kit técnico de IA open source — PromptLab

**Data:** 2026-08-09  
**Status:** pronto para testes controlados  
**Responsável de negócio:** Fabrício Mouzer

## Objetivo

Preparar o uso de ferramentas open source sem copiar os projetos completos para o PromptLab Operating System. Este repositório mantém documentação, decisões, contratos de integração e resultados dos testes; o código de terceiros permanece nos repositórios oficiais.

## Componentes prioritários

| Componente | Repositório oficial | Função no negócio | Primeiro teste |
|---|---|---|---|
| Whisper | [openai/whisper](https://github.com/openai/whisper) | Converter áudios em português em briefings, comandos e textos | Transcrever cinco áudios reais e medir erros |
| Dify | [langgenius/dify](https://github.com/langgenius/dify) | Prototipar workflows, agentes e bases de conhecimento | Criar um fluxo que transforme briefing em pacote de conteúdo |
| Crawl4AI | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | Coletar conteúdo de fontes públicas e autorizadas | Converter uma página permitida em Markdown estruturado |

## Regra de instalação

1. Não copiar integralmente o código dos projetos para este repositório.
2. Usar imagens, releases e instruções dos mantenedores oficiais.
3. Fixar a versão testada; não usar `latest` em produção.
4. Ler licença e avisos de segurança antes de cada implantação.
5. Guardar segredos somente em cofre de segredos ou variáveis do ambiente.
6. Nunca gravar tokens, senhas, chaves de API ou dados pessoais no GitHub.

## Fluxos previstos

### Comando por voz

```text
Áudio → Whisper → briefing estruturado → agente/workflow → resultado → revisão
```

### Pesquisa autorizada

```text
Fontes permitidas → Crawl4AI → limpeza → base de conhecimento → agente
```

### Produção de conteúdo

```text
Briefing → Dify/LLM → texto por canal → mídia → validação → publicação
```

## Plano de teste

### Etapa 1 — valor isolado

- Whisper: taxa de palavras incorretas, tempo e necessidade de correção.
- Dify: tempo para configurar, consistência e custo por execução.
- Crawl4AI: qualidade do conteúdo extraído e conformidade da fonte.

### Etapa 2 — integração

- unir áudio, geração do texto e registro do resultado;
- usar dados fictícios ou não sensíveis;
- registrar falhas e tempo economizado.

### Etapa 3 — produção limitada

- executar com aprovação humana;
- definir limite diário e plano de reversão;
- monitorar custos, erros e publicações duplicadas.

## Métricas mínimas

- minutos economizados por publicação;
- percentual de textos aprovados sem alteração;
- erros de transcrição;
- custo total por conteúdo;
- falhas por integração;
- publicações duplicadas ou incorretas;
- cliques, leads e conversões gerados.

## Critérios para manter uma ferramenta

Uma ferramenta permanece na arquitetura somente se demonstrar ganho mensurável, manutenção aceitável, licença compatível, segurança suficiente e possibilidade de substituição.

## Referências

- [Análise original dos repositórios](../../knowledge/open-source-ai-tools/instagram-10-repos-analysis.md)
- [Arquitetura do agente de publicação](../../agents/social-publishing-agent/README.md)

## Aviso

Código disponível gratuitamente não significa operação sem custo. Servidor, armazenamento, modelos, suporte, atualização, domínio e conformidade podem gerar despesas.
