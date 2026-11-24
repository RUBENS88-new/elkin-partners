# Сайт для партнёров «Господина Ёлкина»

Замена справочника на Gitbook (задача Д-06, `~/dev/gospodin-elkin/counterparties/clients/dropshipping-tickets-2026.md`).
Одна статичная страница: `src/page.html` — исходник, `python3 build.py` собирает `site/index.html`, фото в `site/img/`
(ужаты из «/06 ИП Господин Елкин/Фото_Господин_Елкин/»). Кнопки ведут в бот @elki_drop_bot (`~/dev/elkin-os/nodes/dropship`);
адрес сайта в стартовый набор бота ставится командой Антона `/site <адрес>`.

Цены. Страница при открытии читает лист «Цены» таблицы «Прайс дропшиппинг 2026» и показывает их; если таблица не открыта
по ссылке или недоступна, показывает снимок `SNAPSHOT` в `src/page.html` (от 17.11.2026). Пока таблица закрыта — после
смены цен обновить снимок и пересобрать.

Хостинг: GitHub Pages, https://rubens88-new.github.io/elkin-partners/ (репозиторий RUBENS88-new/elkin-partners, ветка main).
Каждый push в main сам собирает и выкладывает сайт (.github/workflows/pages.yml).
