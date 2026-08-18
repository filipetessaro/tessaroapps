# tessaroapps

Site estático com as páginas de **privacidade, termos de uso e suporte** dos aplicativos.
Publicado por GitHub Pages em **https://apps.tessaroapps.com**.

Repo público de propósito: as lojas exigem que essas URLs abram sem login.
Nada de segredo entra aqui.

## Estrutura

```
index.html            hub com a lista de apps
style.css             estilo compartilhado (claro e escuro)
CNAME                 apps.tessaroapps.com
devocional/
  index.html          página do app + exclusão de conta
  privacidade/        /devocional/privacidade/
  termos/             /devocional/termos/
```

Cada página é uma pasta com `index.html` para a URL ficar sem `.html` — o GitHub Pages
não serve extensão implícita de forma confiável.

## Um repo para todos os apps

Substitui o padrão antigo de um repo por app (`iris-privacy`, `plantscan-ai-legal`,
`coin-value-snap-privacy`, `photoevolve-site`, `garagerank-legal`, `inbloom-app-legal`).
Para migrar um app: criar a pasta, copiar o conteúdo, apontar a loja para a URL nova e
deixar o repo antigo com um redirect até a loja atualizar.

## DNS

O domínio `tessaroapps.com` está na HostGator e a **raiz não é tocada** — só o subdomínio:

| Tipo | Nome | Valor |
|---|---|---|
| CNAME | `apps` | `filipetessaro.github.io` |

Depois, em Settings → Pages do repo: Source = branch `main`, Custom domain =
`apps.tessaroapps.com`, e marcar **Enforce HTTPS** quando o certificado for emitido
(leva alguns minutos após o DNS propagar).

## Pendências antes de submeter o app às lojas

- [ ] Criar a caixa **contato@tessaroapps.com** na HostGator — as duas páginas apontam
      para ela e a LGPD exige canal que responda de verdade.
- [ ] Preencher **razão social e CNPJ** do controlador na Política de Privacidade
      (hoje está só "Tessaro Apps, operada por Filipe Tessaro").
- [ ] Trocar "Devocional Diário" pelo **nome comercial** quando ele for definido.
- [ ] Revisão jurídica. Os textos foram escritos a partir do que o app realmente coleta,
      mas não substituem advogado.
