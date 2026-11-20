# News Store (news.lifepharm.com)

- Blog store, 0 products. Redesign on Dawn, branch `news`, connected to unpublished theme "Lifepharm/news" 190930518311. Older API-uploaded draft 190930321703 still exists. `news-dawn` is history.
- Design: `lpn-*` sections (header, footer, home hero/latest/topics/topic-rail/newsletter, blog, article, search), `assets/lp-news.css`, `snippets/lpn-card.liquid`, the same `lp-lang-switch` as UK.
- Dawn root is 62.5% (1rem = 10px): scale new rem values by 1.6. Section `{% stylesheet %}` only loads where the section renders, so shared styles live in `lp-news.css` (L-016).
- Bloggle: 240 of 246 articles use `article.bloggle-custom`, blogs use `blog.bloggle`. Its content carries CSS targeting `#bloggy--article` (needs the id to override), empty `<p><br></p>` spacers and inline colours. Keep the "NEVER DELETE - Theme for Bloggle app" theme.
- Merchant data issues seen (not edited): one article summary holds another article's text; menu order is alphabetical.
- Health (140 of 246 articles) is the only blog still publishing.
