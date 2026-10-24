# Plus

Static links page for the Plus brands. No build step, no dependencies.

## Files
- `index.html`: the page. Each brand is one `<section class="card">` block.
- `css/style.css`: colors (variables at the top), fonts, spacing.
- `images/`: brand logos.

## Edit
- Change a link: edit the `href` in `index.html`.
- Add a brand: copy a `<section class="card">` block, change its logo and links, and put the logo in `images/`.

## Publish on GitHub Pages
1. Create a repository on GitHub and upload these files (keep `index.html` at the root).
2. Repository **Settings > Pages > Build and deployment > Source: Deploy from a branch**.
3. Choose branch `main` and folder `/ (root)`, then Save.
4. Your site will be at `https://<username>.github.io/<repository>/` after about a minute.

---

## بالعربي
- `index.html` هو الصفحة، وكل علامة تجارية عبارة عن كتلة `<section class="card">`.
- لتعديل رابط: غيّر قيمة `href` في `index.html`.
- لإضافة علامة جديدة: انسخ كتلة `card` كاملة، غيّر اللوجو والروابط، وحط صورة اللوجو في مجلد `images`.
- للنشر على GitHub Pages: ارفع الملفات على مستودع جديد (مع بقاء `index.html` في الجذر)، ثم من Settings > Pages اختر Deploy from a branch ثم `main` و `/ (root)`.
