# PromptLab.AI — Comprador / Analista de Suprimentos

- **Data:** 2026-08-16
- **Horário:** 06:00
- **Tema:** Comparação inteligente de cotações e preparação da decisão de compra
- **Profissão:** Comprador / Analista de Suprimentos
- **Formato do Reel:** SEM AVATAR + VOZ EM OFF NATURAL PT-BR
- **Ferramentas:** ChatGPT + HeyGen + Canva

## Problema resolvido

Cotações de fornecedores chegam em formatos diferentes, com preços, prazos, fretes, impostos, condições de pagamento, garantias e escopos nem sempre comparáveis. O comprador perde tempo reorganizando informações antes de conseguir enxergar lacunas, riscos e pontos que precisam de confirmação.

## Benefício esperado

Transformar requisição de compra + propostas recebidas em uma matriz comparativa rastreável, com critérios equivalentes, informações faltantes, custo conhecido, prazo informado, condições comerciais, riscos, perguntas para fornecedores, próximos passos e resumo para aprovação humana.

## Prompt principal

```text
Você será meu Assistente Sênior de Compras e Suprimentos.

Sua missão é transformar uma requisição de compra e as propostas recebidas de fornecedores em uma ANÁLISE COMPARATIVA CLARA, RASTREÁVEL E ACIONÁVEL para apoiar o processo de compra.

REGRAS IMPORTANTES

- Não invente preço, quantidade, imposto, frete, prazo, disponibilidade, garantia, condição de pagamento, especificação, marca, contrato ou fornecedor.
- Não escolha automaticamente um fornecedor e não aprove nenhuma compra.
- Diferencie claramente:
  FATO INFORMADO
  INFORMAÇÃO FALTANTE
  CONDIÇÃO A CONFIRMAR
  RISCO
  HIPÓTESE DE NEGOCIAÇÃO
- Não trate propostas com escopos diferentes como diretamente equivalentes sem destacar a diferença.
- Quando preço final não puder ser calculado com os dados fornecidos, escreva:
  “CUSTO TOTAL PRECISA SER CONFIRMADO”.
- Quando imposto, frete, seguro, instalação, treinamento ou outro componente não estiver claro, marque como pendência.
- Não invente economia percentual.
- Não trate o menor preço como melhor opção automaticamente.
- Preserve dados comerciais confidenciais.
- Não exponha informações de um fornecedor para outro em mensagens de negociação.
- Não sugira pagamento indevido, favorecimento, presente, vantagem pessoal ou prática incompatível com políticas de integridade.
- Quando houver exigência de homologação, contrato, compliance ou aprovação interna, marque:
  “VALIDAR COM POLÍTICA / RESPONSÁVEL INTERNO”.
- Priorize comparabilidade, custo conhecido, prazo, aderência técnica, risco, rastreabilidade e próximos passos.

DADOS DA REQUISIÇÃO

Item / serviço:
[preencher]

Quantidade:
[preencher]

Especificação técnica:
[preencher]

Requisitos obrigatórios:
[preencher]

Requisitos desejáveis:
[preencher]

Local de entrega:
[preencher]

Data necessária:
[preencher]

Centro de custo / projeto, se aplicável:
[preencher]

Orçamento aprovado, se informado:
[preencher]

Critérios internos de compra:
[preencher]

FORNECEDOR 1

Nome / identificador:
[preencher]

Preço informado:
[preencher]

Frete:
[preencher]

Impostos / taxas:
[preencher]

Prazo de entrega:
[preencher]

Condição de pagamento:
[preencher]

Validade da proposta:
[preencher]

Garantia:
[preencher]

Escopo incluído:
[preencher]

Exclusões:
[preencher]

Observações:
[preencher]

FORNECEDOR 2

[repita os mesmos campos]

FORNECEDOR 3

[repita os mesmos campos]

INFORMAÇÕES ADICIONAIS

Histórico conhecido dos fornecedores:
[preencher]

Mensagens e observações:
[cole aqui]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO EXECUTIVO

Resuma em até 8 pontos:
- item/serviço solicitado;
- quantidade;
- prazo necessário;
- quantidade de propostas analisadas;
- principal diferença entre as propostas;
- maior informação faltante;
- principal risco identificado;
- próximo passo mais importante.

2. MATRIZ COMPARATIVA

Crie uma tabela com uma coluna para cada fornecedor e linhas para:
- preço informado;
- frete;
- impostos/taxas;
- custo total conhecido;
- prazo de entrega;
- condição de pagamento;
- validade da proposta;
- garantia;
- aderência aos requisitos obrigatórios;
- escopo incluído;
- exclusões;
- pendências de confirmação.

Quando os dados não permitirem comparação equivalente, destaque:
“PROPOSTAS NÃO TOTALMENTE COMPARÁVEIS”.

3. ADERÊNCIA À REQUISIÇÃO

Para cada requisito obrigatório, informe por fornecedor:
- ATENDE — somente quando houver evidência clara;
- NÃO EVIDENCIADO;
- PRECISA CONFIRMAR.

Não presuma conformidade.

4. INFORMAÇÕES FALTANTES

Liste separadamente por fornecedor tudo que precisa ser confirmado antes de uma decisão confiável.

5. CUSTO TOTAL CONHECIDO

Organize somente os componentes informados:
- preço base;
- frete;
- impostos/taxas informados;
- instalação, se informada;
- treinamento, se informado;
- outros custos declarados.

Se algum componente relevante estiver ausente, não apresente o valor como custo final.

6. PRAZO E DISPONIBILIDADE

Crie uma tabela contendo:
- fornecedor;
- prazo informado;
- disponibilidade informada;
- validade da informação;
- risco para a data necessária;
- ponto a confirmar.

Não invente data de entrega.

7. CONDIÇÕES COMERCIAIS

Compare:
- pagamento;
- validade da proposta;
- garantia;
- frete;
- devolução/cancelamento, somente se informado;
- condições especiais.

8. RISCOS E ALERTAS

Liste somente riscos sustentados pelos dados, como:
- especificação incompleta;
- escopo diferente;
- prazo incompatível;
- custo adicional não esclarecido;
- condição comercial ausente;
- fornecedor ainda não homologado;
- dependência de aprovação;
- proposta perto de vencer.

9. TOP 5 PERGUNTAS PARA OS FORNECEDORES

Crie perguntas objetivas para fechar as lacunas da análise.

Não revele preço ou condição de concorrentes.

10. OPORTUNIDADES DE NEGOCIAÇÃO

Com base somente nas informações fornecidas, sugira pontos que o comprador pode AVALIAR negociar, como:
- prazo;
- pagamento;
- frete;
- garantia;
- validade;
- quantidade;
- escopo.

Não invente meta de desconto e não presuma poder de barganha.

11. MENSAGEM DE FOLLOW-UP PARA FORNECEDOR

Crie um rascunho curto e profissional contendo:
- agradecimento pela proposta;
- itens que precisam de esclarecimento;
- pedido de confirmação;
- prazo de retorno somente se informado internamente.

Nunca mencione condições comerciais de outros fornecedores.

12. RESUMO PARA APROVAÇÃO INTERNA

Crie um resumo executivo de até 12 linhas contendo:
- necessidade da compra;
- propostas recebidas;
- principais diferenças;
- pontos ainda pendentes;
- riscos;
- decisão ou aprovação que precisa ser feita por responsável humano.

Não recomende aprovação automática.

13. PRÓXIMOS PASSOS

Separe em:
- confirmar com fornecedor;
- validar internamente;
- revisar especificação;
- negociar;
- aguardar aprovação;
- documentar.

14. CHECKLIST PRÉ-COMPRA

Confirme:
- especificação validada;
- quantidade confirmada;
- fornecedores comparados em bases equivalentes;
- custos adicionais esclarecidos;
- prazo confirmado;
- pagamento confirmado;
- garantia confirmada;
- homologação/compliance revisados quando aplicável;
- aprovação interna registrada;
- evidências arquivadas.

15. INFORMAÇÕES QUE AINDA PRECISO CONFIRMAR

Liste todos os dados ausentes que possam mudar custo, prazo, risco ou decisão.
```

## Modo de usar

Cole a requisição de compra e os dados de cada proposta exatamente como recebidos. Se uma informação não existir, deixe em branco. Use a saída para preparar a comparação e o follow-up, mas mantenha aprovação, negociação final, homologação e emissão do pedido sob responsabilidade humana e das políticas internas da empresa.

## Reel — HeyGen

**Formato:** SEM AVATAR + VOZ EM OFF NATURAL PT-BR  
**Proporção:** 9:16  
**Duração:** 40–45 segundos

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

IMPORTANTE:

NÃO utilizar avatar.
NÃO utilizar apresentador falando para a câmera.

Usar:
- voz em off natural em português do Brasil;
- B-roll de escritório de compras;
- e-mails e propostas genéricas;
- planilhas comparativas;
- caixas, fornecedores e logística em cenas ilustrativas;
- checklist;
- interface genérica de IA;
- motion graphics;
- legendas dinâmicas.

Nunca mostrar nomes reais de fornecedores, preços reais, contratos, e-mails, dados bancários ou informações confidenciais.

IDENTIDADE VISUAL

- azul-marinho/preto;
- detalhes verde-limão;
- estética tecnológica e corporativa;
- legendas grandes embutidas;
- cortes a cada 1,5–3 segundos;
- trilha moderna e discreta abaixo da narração.

0–3s — GANCHO

B-roll:
Três propostas diferentes surgindo rapidamente na tela.

VOZ:
“Comprador: três fornecedores mandaram propostas... e nenhuma parece falar a mesma língua?”

TEXTO NA TELA:
3 COTAÇÕES
3 FORMATOS
1 DECISÃO

3–10s

B-roll:
Preço, prazo, frete e condição de pagamento aparecendo em documentos diferentes.

VOZ:
“Preço, frete, prazo, garantia e escopo chegam espalhados e nem sempre são comparáveis.”

10–20s

B-roll:
As propostas entram em uma interface genérica de IA e viram uma matriz estruturada.

VOZ:
“Com um único prompt, a inteligência artificial transforma tudo isso em uma matriz de comparação clara.”

TEXTO:
PREÇO
PRAZO
ESCOPO
PENDÊNCIAS

20–31s

B-roll:
Checklist, tabela comparativa e perguntas para fornecedor.

VOZ:
“Ela identifica diferenças, informações faltantes, riscos, pontos de negociação e ainda prepara o follow-up.”

31–38s

B-roll:
Profissional revisando a matriz no notebook, sem rosto em destaque.

VOZ:
“A IA não escolhe o fornecedor por você. Ela organiza a informação para você decidir com mais método.”

TEXTO:
MENOS RETRABALHO.
MAIS COMPARABILIDADE.

38–45s — CTA

Tela PromptLab.AI.

VOZ:
“Salve este vídeo e comente COTAÇÃO para receber o prompt completo.”

TEXTO FINAL:
COMENTE: COTAÇÃO
SALVE • TESTE • COMPARTILHE

CAPA DO REEL:
COMPRADOR / SUPRIMENTOS

COMPARE COTAÇÕES
SEM SE PERDER

COM IA
```

## Capa do post — Canva

**Formato:** 1080 × 1350

**Headline:** COMPRADOR / SUPRIMENTOS

**Título:** COMPARE COTAÇÕES SEM SE PERDER COM IA

**Linha de apoio:** Preço • Prazo • Escopo • Riscos • Pendências

**CTA:** SALVE ESTE POST E USE O PROMPT

Direção visual: fundo azul-marinho/preto, detalhes verde-limão, três propostas genéricas à esquerda e uma matriz comparativa limpa à direita.

## Legenda — Instagram

🛒 **Comprador: quantas vezes você recebe três cotações e precisa primeiro reorganizar tudo antes de conseguir comparar?**

Preço, frete, prazo, pagamento, garantia e escopo chegam em formatos diferentes — e o menor preço nem sempre significa a proposta mais adequada.

O prompt de hoje transforma **requisição + propostas de fornecedores** em:

✅ matriz comparativa  
✅ aderência aos requisitos  
✅ informações faltantes  
✅ custo conhecido  
✅ prazos e condições  
✅ riscos e alertas  
✅ perguntas para fornecedores  
✅ resumo para aprovação

A IA não escolhe o fornecedor.

**Ela organiza a informação para você comparar com mais clareza e reduzir retrabalho.**

📌 Salve este post.  
💬 Comente **COTAÇÃO**.  
🚀 Siga a **PromptLab.AI**.

## Legenda — TikTok

🛒 Comprador / Suprimentos: transforme **requisição + cotações + condições comerciais** em uma matriz comparativa usando um único prompt.

**Menos planilha manual. Mais clareza para comparar.**

📌 Salve.  
💬 Comente **COTAÇÃO**.

## Stories — Canva

### Story 1 — Enquete

**VOCÊ JÁ RECEBEU 3 COTAÇÕES QUE PARECIAM IMPOSSÍVEIS DE COMPARAR?**

Enquete:
- Toda semana 😵‍💫
- Meu processo já é padronizado ✅

### Story 2 — Valor

**UM BOM PROMPT VIRA UMA MATRIZ DE COMPRAS.**

Preço  
Prazo  
Escopo  
Condições  
Riscos  
Pendências

### Story 3 — Interação

**O QUE MAIS DÁ TRABALHO NA HORA DE COMPARAR FORNECEDORES?**

Caixa de perguntas:

**Preço final? Frete? Prazo? Escopo? Pagamento? Outro?**

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

# COTAÇÃO

**Menos retrabalho.  
Mais comparabilidade.  
Mais método na decisão.**

## Comentário fixado

**PROMPT DO DIA: COMPRADORES E SUPRIMENTOS 🛒**

Comente **COTAÇÃO** se você quer o comando completo para transformar propostas de fornecedores em uma matriz comparativa com prazos, condições, pendências e próximos passos.

## Hashtags

`#PromptLabAI #Compras #Suprimentos #Procurement #Comprador #SupplyChain #Cotacao #Fornecedores #InteligenciaArtificial #ChatGPT #Produtividade #Prompts`

## CTAs

- Comentário principal: **COTAÇÃO**
- Salvar o post
- Compartilhar com equipe de compras/suprimentos
- Seguir a PromptLab.AI

## Oportunidade de monetização

### Kit IA para Compras e Suprimentos

Pode reunir prompts para:
- requisição de compra;
- comparação de cotações;
- follow-up com fornecedores;
- preparação de negociação;
- análise de pendências;
- onboarding/homologação documental;
- handover de compras;
- resumo para aprovação;
- acompanhamento de pedidos;
- avaliação pós-fornecimento baseada em critérios definidos pela empresa.

### Funil recomendado

**Reel/Post → comentário COTAÇÃO → prompt gratuito → mini-kit → Kit IA para Compras e Suprimentos → assinatura PromptLab.AI**

### Proposta de valor

**menos retrabalho na consolidação + comparação mais padronizada + melhor rastreabilidade + mais tempo para negociação e gestão de fornecedores.**

## Ferramentas escolhidas

- **ChatGPT:** estruturação do prompt, análise textual e copy.
- **HeyGen:** Reel SEM AVATAR + VOZ EM OFF NATURAL PT-BR, com B-roll e motion graphics.
- **Canva:** capa e Stories, mantendo consistência visual e reaproveitamento de templates.
