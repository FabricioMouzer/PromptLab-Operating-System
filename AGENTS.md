# AGENTS.md — Governança dos Agentes PromptLab

## Escopo

Estas regras se aplicam a qualquer agente, automação, assistente ou colaborador que utilize este repositório.

## Fonte oficial de verdade

Antes de executar uma tarefa relevante, o agente deve consultar a documentação aplicável. Quando houver conflito entre conversa informal e documento aprovado, o documento vigente prevalece até que uma nova decisão seja registrada.

## Regras obrigatórias

1. Não inventar produtos, preços, políticas, integrações, resultados ou capacidades.
2. Distinguir claramente fatos, hipóteses, decisões e experimentos.
3. Registrar decisões importantes em `decisions/`.
4. Atualizar os documentos afetados quando uma decisão alterar o funcionamento da empresa.
5. Preservar privacidade, segurança e confidencialidade.
6. Solicitar intervenção humana em casos sensíveis, ambíguos, jurídicos, financeiros, de segurança, reclamações graves ou risco reputacional.
7. Priorizar clareza, utilidade, rastreabilidade e resultado mensurável.
8. Evitar complexidade sem evidência de necessidade.

## Padrão de documentação

Todo documento deve, quando aplicável, conter:

- objetivo;
- escopo;
- contexto;
- regras;
- responsáveis;
- métricas;
- riscos;
- critérios de aceitação;
- data ou histórico de revisão.

## Mudanças

Mudanças estruturais devem ser acompanhadas por um registro em `decisions/` explicando contexto, decisão, alternativas, consequências e critérios de revisão.

## Agentes comerciais

Agentes comerciais devem ajudar o cliente a tomar uma decisão adequada, sem pressão indevida, manipulação, promessas falsas ou ocultação de limitações.

## Segurança operacional

Segredos, tokens, chaves de API, senhas e dados pessoais nunca devem ser armazenados diretamente no repositório.
