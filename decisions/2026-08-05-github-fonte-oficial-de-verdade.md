# ADR — GitHub como fonte oficial de verdade

**Data:** 2026-08-05  
**Status:** Aprovado  
**Decisor:** Fabrício Mouzer

## Contexto

Ideias e decisões distribuídas em conversas dificultam pesquisa, continuidade, auditoria e execução profissional.

## Decisão

O repositório PromptLab Operating System será a fonte oficial de verdade da PromptLab.

Toda ideia relevante, decisão, mudança estratégica, produto, agente, automação, processo, experimento e aprendizado deverá ser documentado no GitHub.

## Regras de aplicação

- Conversas iniciam o trabalho, mas não substituem o registro.
- Decisões estruturais terão documento próprio em `decisions/`.
- Documentos afetados deverão ser atualizados.
- Hipóteses serão identificadas como hipóteses.
- Experimentos registrarão critérios, métricas e conclusão.
- Conteúdos substituídos serão preservados quando tiverem valor histórico.

## Alternativas consideradas

### Manter decisões apenas nas conversas

Rejeitada por baixa capacidade de pesquisa, perda de contexto e dependência de memória.

### Centralizar tudo em uma ferramenta de notas

Útil para colaboração, mas inferior ao GitHub para versionamento, histórico técnico e integração com desenvolvimento.

## Consequências positivas

- rastreabilidade;
- pesquisa mais rápida;
- continuidade entre sessões e colaboradores;
- redução de retrabalho;
- maior profissionalismo;
- base confiável para agentes de IA.

## Custos e riscos

- exige disciplina de atualização;
- documentação excessiva pode atrasar decisões simples;
- informações sensíveis exigem tratamento cuidadoso.

## Mitigação

Documentar apenas o nível necessário para permitir execução, pesquisa e governança, sem transformar tarefas simples em burocracia.
