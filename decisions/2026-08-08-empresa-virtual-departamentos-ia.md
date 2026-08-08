# ADR — Empresa virtual por departamentos de IA

**Data:** 2026-08-08  
**Status:** Aprovado para validação  
**Decisor:** Fabrício Mouzer

## Contexto

Um modelo apresentado em conteúdo público organiza uma equipe de IA em departamentos de Marketing, Redes Sociais, Design, Financeiro e Jurídico, com dezenas de skills especializadas.

A PromptLab já possui como direção estratégica evoluir de prompts para Especialistas de IA orientados à execução. A adoção pode aumentar clareza de papéis e repetibilidade, mas a reprodução integral criaria complexidade, custo e manutenção antes da validação.

## Decisão

Adotar uma versão enxuta de empresa virtual com:

- Orquestrador Executivo;
- Produto e IA;
- Marketing e Growth;
- Redes Sociais;
- Vendas e Sucesso;
- Design e Marca;
- Financeiro e Risco;
- Quality Gate e revisão humana.

A definição completa está em `docs/business/modelo-operacional-empresa-virtual-ia-v1.md`.

## Organização das ferramentas

- GitHub permanece como fonte oficial de verdade.
- Notion será a central de execução e acompanhamento.
- Lovable será usado como camada de produto somente após o fluxo principal ser validado.

## Alternativas consideradas

### Copiar todas as skills citadas no conteúdo

Rejeitada. Quantidade não prova utilidade e aumentaria sobreposição, custo e dificuldade de governança.

### Criar imediatamente um novo painel interno no Lovable

Rejeitada neste estágio. O Notion já cobre execução e o GitHub cobre governança. Um novo painel duplicaria dados e exigiria manutenção sem impacto comercial comprovado.

### Manter apenas conversas avulsas

Rejeitada por baixa rastreabilidade e repetibilidade.

## Consequências positivas

- responsabilidades claras;
- processos mensuráveis;
- menor dependência de memória;
- criação de especialistas baseada em demanda real;
- caminho direto entre validação e produto.

## Riscos

- excesso de departamentos;
- respostas inconsistentes;
- automação prematura;
- aparência de estrutura sem receita real;
- confiança excessiva em saídas jurídicas ou financeiras.

## Mitigações

- começar com poucas skills;
- exigir entradas e entregáveis padronizados;
- manter revisão humana;
- medir uso e resultado;
- revisar o modelo após 30 dias ou 10 missões reais.

## Critério de revisão

O modelo será ampliado somente se uma nova skill resolver demanda recorrente e demonstrar ganho mensurável.
