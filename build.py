"""Собирает site/index.html из src/page.html: добавляет обёртку документа для настоящего хостинга."""
from pathlib import Path

root = Path(__file__).parent
page = (root / "src/page.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Продавайте живые ёлки по своей цене, доставку и установку сделает «Господин Ёлкин». Москва и Петербург.">
<meta property="og:title" content="Господин Ёлкин — партнёрам">
<meta property="og:description" content="Вы находите покупателя, мы привозим и устанавливаем ёлку. Ваш доход — разница цен.">
<meta property="og:image" content="img/nordmann-2.jpg">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}html{scroll-behavior:smooth;scroll-padding-top:4rem}</style>
</head>
<body>
"""
(root / "site/index.html").write_text(head + page + "\n</body>\n</html>\n", encoding="utf-8")
print("site/index.html собран")
