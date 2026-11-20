"""Génère toutes les pages du site statique.

Usage :  python _build/build.py
Les réglages (marque, WhatsApp, e-mail) sont dans SITE ci-dessous ; les pages
sont réécrites à chaque exécution, donc modifiez ce fichier plutôt que le HTML.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent

SITE = {
    "brand": "Sunday IPTV",        # nom de marque
    "brand_a": "Sunday",           # partie rouge du logo
    "brand_b": "IPTV",             # partie blanche du logo
    "email": "contact@sundayiptv.com",
    "whatsapp": "212727866871",    # format international, chiffres uniquement
    "year": "2026",
    # domaine personnalisé ; laissez vide pour servir le site sur tiaboussama-cpu.github.io/itv-tst-/
    "domain": "sundayiptv.com",
    # balise de validation Google Search Console (laisser vide pour la retirer)
    "google_verification": "6YEZ3rljmLphqxpY0IRQoS5vIjbv-8T_cDWH_3QAwfA",
}

# ---------------------------------------------------------------- icônes
ICONS = {
    "rocket": '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2m6-11a2 2 0 1 0 0 .01M14 4c3-1 6-1 6-1s0 3-1 6l-6 6-5-5 6-6Zm-5 6-3 0-2 2 4 1m6 5 0 3-2 2-1-4"/>',
    "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
    "ban": '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>',
    "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2V3Z"/><path d="M9 8h6M9 12h6M9 16h4"/>',
    "calx": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4m-6.5 7 5 5m0-5-5 5"/>',
    "diamond": '<path d="M6 3h12l3 6-9 12L3 9l3-6Z"/><path d="M3 9h18"/>',
    "tv": '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8"/>',
    "film": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 3v18M17 3v18M3 8h4M3 16h4M17 8h4M17 16h4"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
    "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3Z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "box": '<rect x="3" y="8" width="18" height="10" rx="2"/><path d="M7 13h.01M11 13h6"/>',
    "stick": '<rect x="9" y="2" width="6" height="16" rx="2"/><path d="M12 18v4"/>',
    "android": '<path d="M6 11h12v7a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-7Z"/><path d="M6 11a6 6 0 0 1 12 0"/><path d="m8 4 1.5 2.5M16 4l-1.5 2.5M9.5 8.5h.01M14.5 8.5h.01"/>',
    "apple": '<path d="M16 3c0 2-1.5 3.5-3.5 3.5C12.5 4.5 14 3 16 3Z"/><path d="M12 8c-1-.6-2-1-3-1-3 0-5 2.5-5 6 0 4 3 8 5 8 1 0 2-.5 3-.5s2 .5 3 .5c1.6 0 3.4-2.6 4.4-5-2-.8-3.2-2.6-3.2-4.6 0-1.7.9-3.1 2.2-4C17.5 6.5 16.2 7 15 7c-1 0-2 .4-3 1Z"/>',
    "laptop": '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5 2.5-2.5Z"/>',
    "chat": '<path d="M4 5h16v11H8l-4 4V5Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><path d="M12 19.5h.01"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="m10 8 6 4-6 4V8Z"/>',
    "book": '<path d="M4 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4V4ZM20 4h-4a3 3 0 0 0-3 3"/><path d="M20 4v14h-6"/>',
}

def ico(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>')

# ---------------------------------------------------------------- logos de paiement (SVG)
PAY_VISA = ('<svg class="pay-logo" viewBox="0 0 60 38" role="img" aria-label="Visa">'
            '<rect width="60" height="38" rx="5" fill="#fff" stroke="#d9d9d9"/>'
            '<text x="30" y="25.5" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" '
            'font-style="italic" font-size="15" letter-spacing="-.5" fill="#1a1f71">VISA</text>'
            '<path d="M8 30h44" stroke="#f7b600" stroke-width="2.4" stroke-linecap="round"/></svg>')
PAY_MC = ('<svg class="pay-logo" viewBox="0 0 60 38" role="img" aria-label="Mastercard">'
          '<rect width="60" height="38" rx="5" fill="#fff" stroke="#d9d9d9"/>'
          '<circle cx="24" cy="19" r="10.5" fill="#eb001b"/><circle cx="36" cy="19" r="10.5" fill="#f79e1b"/>'
          '<path d="M30 10.4a10.5 10.5 0 0 1 0 17.2 10.5 10.5 0 0 1 0-17.2Z" fill="#ff5f00"/></svg>')
PAY_STRIPE = ('<svg class="pay-logo" viewBox="0 0 60 38" role="img" aria-label="Stripe">'
              '<rect width="60" height="38" rx="5" fill="#635bff"/>'
              '<text x="30" y="24.5" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" '
              'font-size="14" letter-spacing="-.3" fill="#fff">stripe</text></svg>')
# taille fixée dans le SVG lui-même pour rester petit même si le CSS n'est pas chargé
PAY_LOGOS = "".join(s.replace('<svg class="pay-logo"', '<svg class="pay-logo" width="34" height="22"', 1)
                    for s in (PAY_VISA, PAY_MC, PAY_STRIPE))

# ---------------------------------------------------------------- données partagées
PLANS = [
    ("Essentiel", "1 mois", "12", "12,00 € / mois", None),
    ("Populaire", "3 mois", "25", "≈ 8,33 € / mois", "−31 %"),
    ("Standard", "6 mois", "30", "5,00 € / mois", "−58 %"),
    ("Meilleur prix", "12 mois", "60", "≈ 5,00 € / mois", "Le plus choisi"),
]
PLAN_FEATURES = [
    ("diamond", "4K, Full HD et HD"),
    ("tv", "32 000+ chaînes en direct"),
    ("film", "220 000+ films et séries"),
    ("check", "Replay (Catch-Up) et EPG"),
    ("shield", "Anti-coupure et VPN inclus"),
    ("headset", "Support 24/7"),
]

GUIDES = [
    # slug, titre, catégorie, icône, résumé
    ("qu-est-ce-que-iptv", "Qu’est-ce que l’IPTV ? Explication complète (2026)", "Bases", "book",
     "Qu’est-ce que l’IPTV ? Fonctionnement de la télé par internet, matériel nécessaire, Xtream Codes et M3U, appareils compatibles et différences avec le satellite."),
    ("meilleures-applications-iptv", "Les meilleures applications IPTV en 2026", "Applications", "play",
     "Les meilleures applications IPTV en 2026 : TiviMate, IPTV Smarters Pro et les lecteurs pour Smart TV et Apple, comparés selon votre appareil et votre usage."),
    ("iptv-android-box", "Box Android IPTV : bien la choisir et la préparer", "Matériel", "box",
     "Choisir une box Android IPTV : box certifiée ou générique, caractéristiques à vérifier, préparation avant l’installation et réglages pour garder une box rapide."),
    ("guide-tivimate", "Guide TiviMate : installation et configuration", "Applications", "monitor",
     "Guide TiviMate complet : installation sur Android TV et Fire TV, ajout de la playlist, guide des programmes (EPG), favoris, replay et fonctions Premium."),
    ("iptv-smarters-pro", "IPTV Smarters Pro : installer et configurer", "Applications", "phone",
     "IPTV Smarters Pro : installation sur Android, Fire TV, iPhone et Windows, connexion Xtream Codes, réglages recommandés et solutions aux erreurs fréquentes."),
    ("iptv-fire-stick", "Fire TV Stick et IPTV : astuces pour une lecture fluide", "Optimisation", "stick",
     "Fire TV Stick lent ou qui coupe ? Réseau, mémoire, réglages cachés et bonnes habitudes pour rendre votre Fire TV Stick rapide et stable pour l’IPTV."),
    ("panne-iptv", "Panne IPTV : résoudre les coupures et le buffering", "Dépannage", "wrench",
     "Panne IPTV, buffering ou chaîne qui coupe ? Diagnostic en 5 minutes, causes fréquentes, réglages réseau et appareil pour retrouver une lecture fluide."),
    ("boitier-iptv", "Quel boîtier IPTV choisir en 2026 ?", "Matériel", "box",
     "Quel boîtier IPTV choisir en 2026 ? Fire TV Stick, box Android TV, Apple TV 4K ou boîtier MAG : comparatif, critères qui comptent et erreurs à éviter."),
]

CITIES = [
    ("iptv-paris", "Paris"),
    ("iptv-lyon", "Lyon"),
    ("iptv-marseille", "Marseille"),
]

LEGAL = [
    ("conditions-generales", "Conditions générales"),
    ("confidentialite", "Politique de confidentialité"),
    ("remboursement", "Politique de remboursement"),
    ("cookies", "Politique cookies"),
]

NAV = [
    ("", "Accueil"),
    ("#comparer", "Comparer"),
    ("#offres", "Offres"),
    ("#offres-4k", "4K IPTV"),
    ("blog/", "Blog"),
    ("a-propos/", "À propos"),
    ("contact/", "Contact"),
    ("#faq", "FAQ"),
]

# ---------------------------------------------------------------- images
IMG_ALT = {
    "hero-sunday-iptv.jpg": "Abonnement IPTV France — famille regardant la télévision avec l’interface {brand}",
    "blog-hero-salon.jpg": "Blog IPTV {brand} — homme regardant l’interface IPTV sur une grande télé dans un salon éclairé en rouge",
    "blog-hero-iptv.jpg": "Blog IPTV {brand} — guides et astuces pour regarder l’IPTV en France",
    "guide-qu-est-ce-que-iptv.jpg": "Qu’est-ce que l’IPTV ? — télévision avec des centaines de chaînes en streaming",
    "guide-meilleures-applications-iptv.jpg": "Meilleures applications IPTV en 2026 — lecteurs IPTV sur TV",
    "guide-iptv-android-box.jpg": "Installer l’IPTV sur une box Android — boîtier Android branché à la télévision",
    "guide-tivimate.jpg": "Guide TiviMate — grille des programmes TV (EPG) avec les chaînes françaises",
    "guide-iptv-smarters-pro.jpg": "IPTV Smarters Pro — installer et configurer le lecteur IPTV sur TV",
    "guide-iptv-fire-stick.jpg": "IPTV sur Amazon Fire TV Stick — télécommande Fire Stick devant la télévision",
    "guide-panne-iptv.jpg": "Panne IPTV — match de foot figé avec chargement en cours, que faire ?",
    "guide-boitier-iptv.jpg": "Quel boîtier IPTV choisir en 2026 — boîtiers de streaming devant la télévision",
    "ville-iptv-paris.jpg": "IPTV Paris — regarder la télévision par internet à Paris, tour Eiffel en arrière-plan",
    "ville-iptv-lyon.jpg": "IPTV Lyon — abonnement IPTV à Lyon dès 5 € par mois",
    "ville-iptv-marseille.jpg": "IPTV Marseille — abonnement IPTV à Marseille, Vieux-Port en arrière-plan",
    "essai-gratuit-iptv.jpg": "Essai IPTV gratuit 24 heures — tester {brand} sans engagement",
    "a-propos-sunday-iptv.jpg": "À propos de {brand} — fournisseur IPTV pour la France",
    "contact-sunday-iptv.jpg": "Contact {brand} — support WhatsApp 24/7",
    "hero-sunday-iptv-photo.jpg": "Abonnement IPTV France — famille regardant la télévision avec l’interface {brand}",
    "poster-action.jpg": "Films d’action — les blockbusters de l’année",
    "poster-science-fiction.jpg": "Films de science-fiction — sagas et univers étendus",
    "poster-series.jpg": "Séries — saisons complètes en VOD",
    "poster-sport.jpg": "Sport — matchs et compétitions en direct",
    "installer-windows.jpg": "Installer l'IPTV sur Windows — ordinateur portable avec l'interface IPTV",
    "choisir-fournisseur-iptv.jpg": "{brand} — sport, films, séries et chaînes TV sur votre télévision",
    "qu-est-ce-que-iptv-1.jpg": "Qu’est-ce que l’IPTV — couple regardant la télévision par internet reliée à une box",
    "qu-est-ce-que-iptv-2.jpg": "IPTV sur tous vos écrans — télé, smartphone, tablette et ordinateur portable",
    "meilleures-applications-iptv-1.jpg": "Meilleures applications IPTV — choisir son lecteur IPTV avec la télécommande",
    "meilleures-applications-iptv-2.jpg": "Comparatif des applications IPTV — deux interfaces de lecteur IPTV sur la télé",
    "iptv-android-box-1.jpg": "Box Android IPTV — bien choisir entre box certifiée et box générique",
    "iptv-android-box-2.jpg": "Préparer une box Android IPTV — branchement Ethernet et menu des réglages",
    "guide-tivimate-1.jpg": "TiviMate — guide des programmes (EPG) en grille sur la télévision",
    "guide-tivimate-2.jpg": "TiviMate — ajouter une chaîne aux favoris avec la télécommande",
    "iptv-smarters-pro-1.jpg": "IPTV Smarters Pro — connexion Xtream Codes avec nom d’utilisateur, mot de passe et URL",
    "iptv-smarters-pro-2.jpg": "IPTV Smarters Pro — interface en tuiles Live TV, Films, Séries et Replay",
    "iptv-fire-stick-1.jpg": "Fire TV Stick avec adaptateur Ethernet — fini les coupures IPTV",
    "iptv-fire-stick-2.jpg": "Fire TV Stick plus rapide — libérer l’espace de stockage dans les réglages",
    "panne-iptv-1.jpg": "Panne IPTV — test de débit sur smartphone pendant un match figé",
    "panne-iptv-2.jpg": "Panne IPTV résolue — câble Ethernet entre la box internet et la télévision",
    "boitier-iptv-1.jpg": "Quel boîtier IPTV choisir — clé de streaming, box Android, boîtier et décodeur",
    "boitier-iptv-2.jpg": "Comparatif des boîtiers IPTV — deux télécommandes devant une image 4K",
    "essai-gratuit-1.jpg": "Essai IPTV gratuit 24 h — demande d’essai par message sur smartphone",
    "essai-gratuit-2.jpg": "Essai IPTV gratuit — amis regardant un match en direct avant de s’abonner",
    "installer-iptv-smart-tv-1.jpg": "IPTV sur Smart TV sans boîtier — boutique d’applications du téléviseur",
    "installer-iptv-smart-tv-2.jpg": "IPTV sur Smart TV — ajouter son abonnement avec Xtream Codes ou M3U",
    "installer-iptv-fire-tv-1.jpg": "IPTV sur Fire TV Stick — étape 1 : activer les options pour les développeurs",
    "installer-iptv-fire-tv-2.jpg": "IPTV sur Fire TV Stick — chargement des chaînes après la connexion de l’abonnement",
    "installer-iptv-android-1.jpg": "IPTV sur Android — application IPTV dans la boutique sur smartphone et tablette",
    "installer-iptv-android-2.jpg": "IPTV sur Android — diffuser du téléphone vers la télévision",
    "installer-iptv-ios-1.jpg": "IPTV sur iPhone et iPad — application IPTV avec les rubriques Live TV, Films et Séries",
    "installer-iptv-ios-2.jpg": "IPTV sur iPad — diffusion d’un match sur la télévision avec AirPlay",
    "installer-iptv-mag-1.jpg": "Boîtier MAG — étiquette avec l’adresse MAC sous le boîtier",
    "installer-iptv-mag-2.jpg": "Boîtier MAG — portail IPTV avec la liste des chaînes, comme une box opérateur",
    "installer-iptv-windows-1.jpg": "IPTV sur Windows — connexion Xtream Codes sur un ordinateur portable",
    "installer-iptv-windows-2.jpg": "IPTV sur Windows — ordinateur portable relié à la télévision en HDMI",
    "chaines-tv.jpg": "Plus de 32 000 chaînes TV en direct — grille des chaînes {brand}",
}
IMG_SIZE = {"hero-sunday-iptv.jpg": (1920, 1280), "hero-sunday-iptv-photo.jpg": (1920, 1280), "poster-action.jpg": (560, 1120), "poster-science-fiction.jpg": (560, 1120), "poster-series.jpg": (560, 1120), "poster-sport.jpg": (560, 1120), "blog-hero-iptv.jpg": (1920, 640), "blog-hero-salon.jpg": (2400, 790), "a-propos-sunday-iptv.jpg": (1200, 600), "choisir-fournisseur-iptv.jpg": (1952, 806)}

# Versions WebP plus légères (générées automatiquement dans images/) pour les téléphones.
RESP_WIDTHS = (480, 800, 1200, 1920)
# largeur affichée de l'image selon sa classe (attribut sizes)
IMG_SIZES = {
    "hero-photo": "100vw",
    "poster-img": "(min-width: 860px) 270px, 50vw",
    "thumb-img": "(min-width: 980px) 360px, (min-width: 640px) 50vw, 100vw",
    "body-img": "(min-width: 1180px) 760px, (min-width: 960px) calc(100vw - 420px), 100vw",
    "article-img": "(min-width: 1180px) 760px, (min-width: 960px) calc(100vw - 420px), 100vw",
    "wide-img": "(min-width: 840px) 800px, 100vw",
}

def responsive_set(name, w):
    """Crée (si besoin) les variantes WebP de images/<name> et renvoie la liste srcset."""
    try:
        from PIL import Image
    except ImportError:          # Pillow absent : on garde simplement le JPG
        return ""
    src = ROOT / "images" / name
    stem = src.stem
    parts = []
    for rw in [x for x in RESP_WIDTHS if x < w] + [w]:
        out = ROOT / "images" / f"{stem}-{rw}.webp"
        if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
            im = Image.open(src).convert("RGB")
            if rw < im.width:
                im = im.resize((rw, round(im.height * rw / im.width)), Image.LANCZOS)
            im.save(out, "WEBP", quality=78, method=6)
        parts.append(f"{{R}}images/{stem}-{rw}.webp {rw}w")
    return ", ".join(parts)

def img(name, cls="page-img", lazy=True):
    w, h = IMG_SIZE.get(name, (1200, 800))
    alt = html.escape(IMG_ALT[name].format(brand=SITE["brand"]), quote=True)
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    srcset = responsive_set(name, w)
    sizes = next((v for k, v in IMG_SIZES.items() if k in cls.split()), "(min-width: 1140px) 1100px, 100vw")
    resp = f' srcset="{srcset}" sizes="{sizes}"' if srcset else ""
    return f'<img class="{cls}" src="{{R}}images/{name}"{resp} alt="{alt}" width="{w}" height="{h}"{load}>'

def gsv_meta():
    v = SITE.get("google_verification")
    return f'\n<meta name="google-site-verification" content="{html.escape(v, quote=True)}">' if v else ""

def og_image_url():
    base = f"https://{SITE['domain']}/" if SITE["domain"] else "https://tiaboussama-cpu.github.io/itv-tst-/"
    return base + "images/hero-sunday-iptv.jpg"

# ---------------------------------------------------------------- gabarit
# ---------------------------------------------------------------- messages WhatsApp pré-remplis
DEVICE_LINE = "Mon appareil : (Smart TV, Fire Stick, box Android, iPhone…)"

def msg_order(dur, price):
    return (f"Bonjour {SITE['brand']} 👋\n"
            f"Je souhaite commander l’abonnement {dur} à {price} €.\n\n"
            f"{DEVICE_LINE}\n"
            "Application utilisée : (si vous en avez déjà une)\n\n"
            "Merci de m’envoyer le lien de paiement.")

def msg_trial():
    return (f"Bonjour {SITE['brand']} 👋\n"
            "Je souhaite profiter de l’essai gratuit de 24 h avant de m’abonner.\n\n"
            f"{DEVICE_LINE}\n\n"
            "Merci !")

def msg_question():
    return f"Bonjour {SITE['brand']} 👋\nJ’ai une question : "

def wa_attr(msg):
    return f'data-wa="{html.escape(msg, quote=True)}"'

def logo(r, big=False):
    return (f'<a class="logo" href="{r}index.html" aria-label="{SITE["brand"]} – accueil">'
            f'<span class="logo-stack"><span class="logo-word">{SITE["brand_a"]}</span> '
            f'<span class="logo-sub">{SITE["brand_b"]}</span></span></a>')

def header(r, active):
    links = []
    for href, label in NAV:
        if href.startswith("#"):
            url = f"{r}index.html{href}"
        else:
            url = f"{r}{href}" if href else f"{r}index.html"
        cls = ' class="active"' if active == label else ""
        links.append(f'<a href="{url}"{cls}>{label}</a>')
    links.append(f'<a class="btn btn-red" href="{r}index.html#offres">→ Commander</a>')
    return f"""
<div class="notice" id="notice">
  <div class="wrap">
    <span>⚡ <b>Essai gratuit 24 h</b> · activation en moins d’une heure · support WhatsApp 24/7.</span>
    <button class="notice-close" aria-label="Fermer le bandeau">×</button>
  </div>
</div>
<header class="site-header">
  <div class="wrap header-row">
    {logo(r)}
    <nav class="nav" id="nav" aria-label="Navigation principale">{''.join(links)}</nav>
    <a class="btn btn-red" href="{r}index.html#offres">→ Commander</a>
    <button class="menu-toggle" aria-controls="nav" aria-expanded="false" aria-label="Ouvrir le menu">☰</button>
  </div>
</header>"""

def footer(r):
    g = "".join(f'<li><a href="{r}{s}/">{t.split(" :")[0].split(" (")[0]}</a></li>' for s, t, *_ in GUIDES)
    c = "".join(f'<li><a href="{r}{s}/">IPTV {n}</a></li>' for s, n in CITIES)
    l = "".join(f'<li><a href="{r}{s}/">{t}</a></li>' for s, t in LEGAL)
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="f-top">
      <a class="logo" href="{r}index.html"><span class="logo-stack"><span class="logo-word">{SITE["brand_a"]}</span><span class="logo-sub">{SITE["brand_b"]}</span></span></a>
      <p>Abonnement IPTV pour la France, la Belgique et la Suisse. Formules dès 5 € par mois, sans engagement.</p>
    </div>
    <div class="f-cols">
      <div><h3>Pages</h3><ul>
        <li><a href="{r}index.html">Accueil</a></li>
        <li><a href="{r}essai-gratuit/">Essai gratuit</a></li>
        <li><a href="{r}index.html#offres">Offres</a></li>
        <li><a href="{r}blog/">Blog IPTV</a></li>
      </ul></div>
      <div><h3>Guides</h3><ul>{g}</ul></div>
      <div><h3>Villes</h3><ul>{c}</ul></div>
      <div><h3>Société</h3><ul>
        <li><a href="{r}a-propos/">À propos</a></li>
        <li><a href="{r}contact/">Contact</a></li>
        {l}
      </ul></div>
      <div><h3>Contact</h3><ul>
        <li><a href="#" {wa_attr(msg_question())}>WhatsApp</a><span class="f-247">24/7</span></li>
        <li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
        <li style="color:#8d929b">Réponse rapide, 7 j/7</li>
      </ul></div>
    </div>
    <div class="f-row">
      <div class="f-chips"><span>Paiement :</span><span class="pay">{PAY_LOGOS}</span></div>
      <div class="f-chips"><span>Appareils :</span>{device_chips(r)}</div>
    </div>
    <div class="f-bottom">
      <span>© <span id="year">{SITE["year"]}</span> {SITE["brand"]}. Tous droits réservés.</span>
      <span>Support 24/7 · Sans engagement · Essai gratuit 24 h</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="#" {wa_attr(msg_question())} aria-label="Nous écrire sur WhatsApp">{WA_SVG}</a>"""

def home_jsonld():
    """Données structurées de l'accueil, générées à partir des mêmes données que la page
    (SITE, PLANS, FAQ_HOME) : aucune note, aucun avis, rien d'inventé."""
    import json
    base = site_url()
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE["brand"],
        "url": base,
        "logo": base + "icon-512.png",
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_HOME],
    }
    product = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": f"Abonnement IPTV {SITE['brand']}",
        "description": "Abonnement IPTV : 32 000+ chaînes en direct, 220 000+ films et séries, 4K, Full HD et HD, replay et EPG, sans engagement.",
        "image": og_image_url(),
        "brand": {"@type": "Brand", "name": SITE["brand"]},
        "offers": [{"@type": "Offer", "name": f"Abonnement {name} — {dur}", "price": price,
                    "priceCurrency": "EUR", "availability": "https://schema.org/InStock",
                    "url": base + "#offres"} for name, dur, price, per, tag in PLANS],
    }
    return "".join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                   for x in (org, faq_ld, product))

def page(path, title, desc, body, active="", depth=None, head_extra=""):
    depth = path.count("/") if depth is None else depth
    r = "../" * depth
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta name="theme-color" content="#111111">{gsv_meta()}
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og_image_url()}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_image_url()}">{head_extra}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;700;800&family=Roboto:wght@700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;700;800&family=Roboto:wght@700;800;900&display=swap"></noscript>
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="stylesheet" href="{r}style.css?v=20">
</head>
<body id="top">
{header(r, active)}
<main>
{body.replace("{R}", r)}
</main>
{footer(r)}
<script>window.SITE_WHATSAPP = "{SITE["whatsapp"]}"; window.SITE_BRAND = "{SITE["brand"]}";</script>
<script src="{r}script.js?v=3"></script>
</body>
</html>
"""
    # liens propres : "../" ou "./" plutôt que ".../index.html" (pas de index.html dans l'adresse)
    doc = doc.replace(f'href="{r}index.html', f'href="{r or "./"}')
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return out

# ---------------------------------------------------------------- blocs réutilisables
def plan_cards(prefix="Abonnement"):
    cards = []
    for name, dur, price, per, tag in PLANS:
        hot = tag == "Le plus choisi"
        feats = "".join(f"<li>{ico(i)}<span>{t}</span></li>" for i, t in PLAN_FEATURES)
        ribbon = f'<span class="ribbon">{tag}</span>' if hot else ""
        badge = f'<span class="badge">{tag}</span>' if tag and not hot else ""
        cta = "Commander 12 mois" if hot else "Commander"
        cards.append(f"""
      <article class="plan{' hot' if hot else ''}">
        {ribbon}
        <p class="p-name">{prefix} {name}</p>
        <div class="p-head"><p class="p-dur">{dur}</p>{badge}</div>
        <div class="p-cost"><p class="p-price">{price} €</p><p class="p-per">{per}</p></div>
        <ul>{feats}</ul>
        <div class="pay">{PAY_LOGOS}</div>
        <a class="btn {'btn-white' if hot else 'btn-red'}" href="#" {wa_attr(msg_order(dur, price))} data-order-dur="{dur}" data-order-price="{price}">{cta}</a>
      </article>""")
    return "".join(cards)

def guide_cards(r="{R}", cls="g-card"):
    out = []
    for slug, title, cat, icon, summary in GUIDES:
        pic = GUIDE_IMAGES.get(slug)
        thumb = img(pic, "thumb-img") if pic else ico(icon)
        if cls == "g-card":
            out.append(f'<a class="g-card" href="{r}{slug}/"><div class="g-img">{thumb}</div><span>{title}</span></a>')
        else:
            out.append(f'<a class="post" href="{r}{slug}/"><div class="g-img">{thumb}</div>'
                       f'<div class="p-body"><span class="p-cat">{cat}</span><h3>{title}</h3><p>{summary}</p></div></a>')
    return "".join(out)

FAQ_HOME = [
    ("Combien de temps faut-il pour la livraison ?", "En général moins d’une heure après le paiement. Vous recevez vos identifiants et un guide d’installation adapté à votre appareil par WhatsApp ou par e-mail."),
    ("Quels moyens de paiement acceptez-vous ?", "Le paiement se fait par carte bancaire (Visa, Mastercard) via une page de paiement sécurisée Stripe. Demandez le lien de paiement sur WhatsApp."),
    ("Puis-je tester avant d’acheter ?", "Oui, un essai gratuit de 24 heures est disponible. Il vous permet de vérifier la qualité et les chaînes sur votre propre connexion."),
    ("Combien d’écrans puis-je utiliser en même temps ?", "Un abonnement correspond à une connexion simultanée. Pour plusieurs écrans en même temps, demandez une offre multi-connexions."),
    ("Quelle vitesse internet faut-il ?", "Environ 10 Mb/s pour la HD et 25 Mb/s pour la 4K. Le câble Ethernet donne les meilleurs résultats."),
    ("Quelle application IPTV est la meilleure ?", "TiviMate et IPTV Smarters sont les plus utilisées sur Android et Fire Stick. Sur Smart TV et iPhone, nous vous indiquons l’application adaptée."),
    ("Y a-t-il un renouvellement automatique ?", "Non. Vous payez une seule fois pour la durée choisie. À la fin de la période, vous décidez librement de renouveler ou non."),
    ("Que faire si une chaîne ne fonctionne pas ?", "Contactez le support sur WhatsApp en précisant la chaîne et votre appareil. Nous répondons 24 h/24."),
    ("L’abonnement fonctionne-t-il à l’étranger ?", "Oui, le service fonctionne partout où vous avez une connexion internet stable, en France comme en voyage."),
    ("Le VPN est-il obligatoire ?", "Non, mais un VPN est inclus si vous souhaitez l’utiliser, par exemple sur certains réseaux qui limitent le streaming."),
]

def faq(items):
    return "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>"
                   for i, (q, a) in enumerate(items))

# ---------------------------------------------------------------- accueil
POSTER_TILES = [
    ("Action", "Les blockbusters de l’année", "linear-gradient(160deg,#ff8a00,#7a1d00 55%,#1a0600)", "poster-action.jpg"),
    ("Science-fiction", "Sagas et univers étendus", "linear-gradient(160deg,#2bc0e4,#1a2a6c 55%,#05070f)", "poster-science-fiction.jpg"),
    ("Séries", "Saisons complètes en VOD", "linear-gradient(160deg,#c471ed,#5b1a7a 55%,#12051a)", "poster-series.jpg"),
    ("Sport", "Matchs et compétitions en direct", "linear-gradient(160deg,#56ab2f,#174d12 55%,#041205)", "poster-sport.jpg"),
]

def build_home():
    posters = "".join(f'<a class="poster" href="#offres" style="--g:{g}">{img(pic, "poster-img")}<span class="genre">{gname}</span><strong>{gname}</strong><small>{sub}</small></a>'
                      for gname, sub, g, pic in POSTER_TILES)
    body = f"""
<section class="hero hero-has-photo">
  <div class="hero-bg">
    {img("hero-sunday-iptv-photo.jpg", "hero-photo", lazy=False)}
  </div>
  <div class="wrap hero-content">
    <h1>Abonnement IPTV : la meilleure offre IPTV en France</h1>
    <p>Profitez de milliers de chaînes du monde entier, du sport en direct et d’un immense catalogue de films et séries, sur tous vos écrans. Activation rapide, sans engagement, dès 5 € par mois.</p>
    <span class="hero-badge">{ico("check")} <span>Essai gratuit <b>24 h</b> · sans engagement</span></span><br>
    <a class="btn btn-red" href="#offres">Finaliser ma commande</a>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <h2 class="h-lg upper">Quels films et séries regarder avec l’IPTV ?</h2>
    <p class="lede">Avec {SITE["brand"]}, vous accédez aux dernières sorties cinéma et aux séries du moment dès leur disponibilité. Notre catalogue VOD est mis à jour en continu : action, science-fiction, séries complètes, documentaires et programmes pour enfants, tout est réuni dans une seule application.</p>
    <div class="posters">{posters}</div>
  </div>
</section>

<section class="section-tight" id="avantages">
  <div class="wrap">
    <h2 class="h-lg center" style="margin-bottom:30px">Pourquoi choisir {SITE["brand"]} ?</h2>
    <div class="trio">
      <div class="trio-card">{ico("rocket")}<h3>Un service IPTV rapide</h3><p>Nos serveurs sont répartis en Europe pour une diffusion fluide et un démarrage instantané des chaînes.</p></div>
      <div class="trio-card">{ico("monitor")}<h3>Qualité de streaming élevée</h3><p>Chaînes et films en 4K, Full HD et HD : l’image s’adapte à votre connexion pour une expérience optimale.</p></div>
      <div class="trio-card">{ico("headset")}<h3>Support en direct</h3><p>Une équipe joignable 24 h/24 sur WhatsApp ou par e-mail pour l’installation comme pour les questions.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    {img("chaines-tv.jpg", "page-img tv-photo")}
    <div class="split-text">
      <h2 class="h-md">Quelles chaînes TV trouver avec l’IPTV en France ?</h2>
      <p>Votre abonnement IPTV donne accès à plus de 32 000 chaînes en direct dans le monde, plus de 220 000 films et séries à la demande et un guide des programmes (EPG) complet sur tous vos appareils. Commandez aujourd’hui et regardez votre première chaîne en moins d’une heure.</p>
      <a class="btn btn-red" href="#offres">Passer commande</a>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap center">
    <p class="kicker">Confiance &amp; sécurité</p>
    <h2 class="h-lg">Acheter un abonnement IPTV, sans risque</h2>
    <div class="trust">
      <div class="trust-card">{ico("ban")}<h3>Sans engagement</h3><p>Un paiement unique pour la durée choisie. Pas de contrat, pas de préavis, pas de petites lignes.</p></div>
      <div class="trust-card">{ico("receipt")}<h3>Aucun frais caché</h3><p>Dès 5 € par mois sur 12 mois. Le prix affiché est le prix payé : pas de frais d’activation.</p></div>
      <div class="trust-card">{ico("calx")}<h3>Pas de renouvellement automatique</h3><p>Votre abonnement s’arrête à la fin de la période. Vous voulez continuer ? Vous décidez, quand vous voulez.</p></div>
    </div>
    <p class="footnote">Consultez nos <a href="{{R}}conditions-generales/">conditions générales</a> et notre <a href="{{R}}remboursement/">politique de remboursement</a> pour tous les détails.</p>
  </div>
</section>

<section class="section" id="offres">
  <div class="wrap">
    <div class="pricing-head">
      <h2 class="h-xl">Abonnement IPTV {SITE["brand"]}</h2>
      <p class="sub-h">Tout compris : chaînes, films, séries et sport</p>
      <p>Toutes nos formules donnent accès au même contenu : les chaînes en direct du monde entier, le catalogue complet de films et séries, le replay et le guide des programmes. Seule la durée change. Plus elle est longue, plus le prix mensuel baisse : dès 5 € par mois avec l’offre 12 mois.</p>
    </div>
    <div class="plans">{plan_cards()}</div>
  </div>
</section>

<section class="section-tight" id="offres-4k">
  <div class="wrap center">
    <h2 class="h-lg">La 4K incluse dans chaque abonnement</h2>
    <p class="lede">Pas d’option « 4K » à payer en plus : chaque formule comprend les chaînes et les films disponibles en Ultra HD, en plus de la Full HD et de la HD. Il suffit d’une connexion de 25 Mb/s et d’un appareil compatible 4K.</p>
  </div>
</section>

<section class="section" id="comparer">
  <div class="wrap">
    <div class="center">
      <h2 class="h-lg">Comparer les offres IPTV</h2>
      <p class="lede">Pourquoi choisir {SITE["brand"]} plutôt qu’une liste gratuite ou une offre au rabais ? Voici les différences qui comptent : qualité, stabilité et service client.</p>
    </div>
    <div class="compare-wrap">
      <table class="compare">
        <thead><tr><th>Fonction</th><th class="us">{SITE["brand"]} 🏆</th><th>Listes IPTV gratuites</th><th>Offres à bas prix</th></tr></thead>
        <tbody>
          <tr><td>Point fort</td><td class="us">Stabilité et service</td><td>Gratuit</td><td>Prix très bas</td></tr>
          <tr><td>Qualité des chaînes</td><td class="us"><span class="chip-gold">4K</span>Full HD et HD</td><td>Variable, souvent SD</td><td>HD compressée</td></tr>
          <tr><td>Serveurs</td><td class="us"><span class="t-gold">Serveurs répartis</span> en Europe</td><td>Hors ligne fréquemment</td><td>Serveur unique surchargé</td></tr>
          <tr><td>Films et séries</td><td class="us"><span class="t-gold">220 000+</span> titres</td><td>Quasi inexistant</td><td>Catalogue limité</td></tr>
          <tr><td>Support client</td><td class="us"><span class="t-green">✓</span> WhatsApp 24/7</td><td>Aucun</td><td>E-mail, réponse lente</td></tr>
          <tr><td>Anti-coupure</td><td class="us"><span class="t-gold">Oui</span>, inclus</td><td>Non</td><td>Basique</td></tr>
          <tr><td>Essai gratuit</td><td class="us"><span class="t-green">✓</span> 24 heures</td><td>—</td><td>Rarement</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap center">
    <h2 class="h-xl">Comment choisir le bon fournisseur IPTV ?</h2>
    <p class="sub-h">Toute la saison en direct, et vos séries à la demande</p>
    <p class="lede">Avec autant de fournisseurs sur le marché, il est difficile de faire le bon choix. Vérifiez trois choses : la stabilité des serveurs pendant les grands événements, la réactivité du support et la possibilité de tester avant de payer. Chez {SITE["brand"]}, l’essai gratuit de 24 heures vous permet de juger sur pièce.</p>
    {img("choisir-fournisseur-iptv.jpg", "page-img showcase-img")}
    <div class="stat-tabs">
      <div><strong>24/7</strong><span>Support client</span></div>
      <div><strong>32 000+</strong><span>Chaînes</span></div>
      <div><strong>220 000+</strong><span>Films &amp; séries</span></div>
    </div>
  </div>
</section>

<section class="section" id="appareils">
  <div class="wrap split rev">
    <div class="dev-icons">
      <a href="{{R}}installer-iptv-smart-tv/">{ico("tv")}Smart TV</a><a href="{{R}}installer-iptv-fire-tv/">{ico("stick")}Fire TV Stick</a><a href="{{R}}iptv-android-box/">{ico("box")}Box Android</a><a href="{{R}}installer-iptv-ios/">{ico("apple")}Apple TV</a>
      <a href="{{R}}installer-iptv-android/">{ico("phone")}Smartphone</a><a href="{{R}}installer-iptv-windows/">{ico("laptop")}PC Windows</a><a href="{{R}}installer-iptv-mag/">{ico("box")}Boîtier MAG</a><a href="{{R}}meilleures-applications-iptv/">{ico("play")}Kodi</a>
    </div>
    <div class="split-text">
      <h2 class="h-md">Sur quels appareils fonctionne l’IPTV ?</h2>
      <p>Notre service IPTV est compatible avec tous vos appareils : Smart TV Samsung et LG, box et smartphones Android, iPhone, iPad et Apple TV, Amazon Fire TV Stick, Kodi et boîtiers MAG. Que vous regardiez sur votre télé ou en déplacement, l’installation prend quelques minutes et vous avez accès à plus de 32 000 chaînes.</p>
      <a class="btn btn-red" href="#offres">Passer commande</a>
    </div>
  </div>
</section>

<section class="steps-sec" id="commander">
  <div class="wrap">
    <h2 class="h-xl">Comment commander un abonnement IPTV ?</h2>
    <div class="zig">
      <div class="z1"><h3>Passez votre commande</h3><p>Choisissez la formule qui vous convient et indiquez votre appareil ainsi que l’application que vous utilisez. Réglez ensuite par carte bancaire via le lien de paiement sécurisé.</p></div>
      <div class="z2"><h3>Recevez vos identifiants</h3><p>Sous 15 à 60 minutes, vous recevez vos accès par WhatsApp ou par e-mail. Pensez à vérifier vos spams. Vous êtes pressé ? Écrivez-nous sur WhatsApp pour accélérer l’activation.</p></div>
      <div class="z3"><h3>Profitez de votre abonnement</h3><p>Installez l’application sur votre appareil préféré et regardez immédiatement toutes les chaînes, les films et les séries. Bienvenue chez {SITE["brand"]} !</p></div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap center">
    <h2 class="h-md">Découvrez tous nos guides IPTV</h2>
    <p class="lede">Nouveau dans l’IPTV ou envie de tirer le meilleur de votre abonnement ? Nos guides vous accompagnent pas à pas : installation sur Smart TV ou Fire Stick, réglage de l’EPG, résolution des problèmes courants.</p>
    <div class="carousel">
      <button class="c-btn c-prev" aria-label="Précédent">‹</button>
      <div class="c-track">{guide_cards()}</div>
      <button class="c-btn c-next" aria-label="Suivant">›</button>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap seo-grid">
    <div><h2>Qu’est-ce que l’IPTV et comment ça marche ?</h2><p>L’IPTV (Internet Protocol Television) diffuse la télévision par internet plutôt que par satellite, câble ou antenne. Les chaînes et les vidéos arrivent sous forme de flux sur votre appareil, via une application. Il suffit d’une connexion internet et de vos identifiants. <a href="{{R}}qu-est-ce-que-iptv/">Lire le guide complet</a>.</p></div>
    <div><h2>Que contient un abonnement IPTV ?</h2><p>Un abonnement IPTV regroupe les chaînes en direct, un catalogue de films et séries à la demande, le replay des programmes et un guide électronique (EPG). Chez {SITE["brand"]}, tout est inclus dans chaque formule, sans bouquet supplémentaire.</p></div>
    <div><h2>Comment regarder la télé sans box ?</h2><p>Avec l’IPTV, plus besoin de décodeur : une Smart TV, une clé Fire TV ou un smartphone suffit. Vous installez une application, vous entrez vos identifiants et vous regardez la télé sur l’écran de votre choix.</p></div>
    <div><h2>Quelle est la meilleure application IPTV sur Android ?</h2><p>TiviMate est souvent considérée comme la plus complète sur Android TV, tandis qu’IPTV Smarters Pro est simple à prendre en main. Comparez-les dans notre guide des <a href="{{R}}meilleures-applications-iptv/">meilleures applications IPTV</a>.</p></div>
    <div><h2>Quel boîtier IPTV choisir en 2026 ?</h2><p>Fire TV Stick 4K, box Android, Apple TV ou boîtier MAG : chacun a ses avantages selon votre budget et votre télé. Notre <a href="{{R}}boitier-iptv/">comparatif des boîtiers</a> vous aide à trancher.</p></div>
    <div><h2>Que faire en cas de panne IPTV ?</h2><p>Une coupure vient le plus souvent de la connexion, du Wi-Fi ou du cache de l’application. Redémarrez votre appareil, passez en Ethernet si possible et suivez notre guide <a href="{{R}}panne-iptv/">panne IPTV</a>. Le support reste joignable 24/7.</p></div>
    <div><h2>L’IPTV partout en France</h2><p>{SITE["brand"]} fonctionne dans toute la France, en fibre comme en ADSL, et vous suit en déplacement. Découvrez nos pages dédiées à l’<a href="{{R}}iptv-paris/">IPTV à Paris</a>, à l’<a href="{{R}}iptv-lyon/">IPTV à Lyon</a> et à l’<a href="{{R}}iptv-marseille/">IPTV à Marseille</a>.</p></div>
    <div><h2>Optimiser son appareil pour l’IPTV</h2><p>Un appareil bien réglé fait toute la différence : consultez nos <a href="{{R}}iptv-fire-stick/">astuces pour un Fire TV Stick fluide</a>, notre guide pour <a href="{{R}}iptv-android-box/">bien choisir sa box Android</a> et les réglages de <a href="{{R}}guide-tivimate/">TiviMate</a> et d’<a href="{{R}}iptv-smarters-pro/">IPTV Smarters Pro</a>.</p></div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap">
    <div class="faq-head">
      <p class="small">FAQ</p>
      <h2 class="h-xl" style="margin-top:8px">Questions fréquentes</h2>
      <p class="lede">Vous avez une question sur l’IPTV ? Vous la trouverez sûrement ici. Sinon, notre équipe répond 24 h/24 sur WhatsApp ou par e-mail.</p>
    </div>
    <div class="faq-list">{faq(FAQ_HOME)}</div>
  </div>
</section>
"""
    page("index.html", f"Abonnement IPTV France : meilleure offre IPTV 2026 | {SITE['brand']}",
         "Abonnement IPTV dès 5 € par mois : 32 000+ chaînes, 220 000+ films et séries, 4K, essai gratuit 24 h, sans engagement.",
         body, active="Accueil", depth=0, head_extra=home_jsonld())

# ---------------------------------------------------------------- article générique
# ---------------------------------------------------------------- guides par appareil
# Le texte de chaque guide est dans _build/appareils/<slug>.txt (format décrit dans parse_guide).
DEVICE_GUIDES = [
    # slug, libellé, icône, titre H1 (HTML), titre court, image, résumé
    ("installer-iptv-smart-tv", "Smart TV", "tv",
     'Installer l’IPTV sur <span class="red">Smart TV</span>', "Installer l’IPTV sur Smart TV Samsung, LG et Android TV",
     "hero-sunday-iptv-photo.jpg",
     "Installer l’IPTV sur Smart TV Samsung, LG, Sony, Philips ou TCL : choisir l’application, ajouter votre abonnement, régler l’EPG et résoudre les problèmes."),
    ("installer-iptv-fire-tv", "Fire TV", "stick",
     'Installer l’IPTV sur <span class="red">Fire TV Stick</span>', "Installer l’IPTV sur Amazon Fire TV Stick",
     "guide-iptv-fire-stick.jpg",
     "Installer l’IPTV sur Fire TV Stick et Fire TV Cube : options développeurs, Downloader, installation de l’application et connexion de votre abonnement."),
    ("installer-iptv-android", "Android", "android",
     'Installer l’IPTV sur <span class="red">Android</span>', "Installer l’IPTV sur Android : smartphone, tablette et box",
     "guide-iptv-android-box.jpg",
     "Installer l’IPTV sur Android : smartphone, tablette, box ou téléviseur Android TV. Quelle application choisir, installation et configuration pas à pas."),
    ("installer-iptv-ios", "iOS", "apple",
     'Installer l’IPTV sur <span class="red">iPhone, iPad</span> et Apple TV', "Installer l’IPTV sur iPhone, iPad et Apple TV",
     "contact-sunday-iptv.jpg",
     "Installer l’IPTV sur iPhone, iPad et Apple TV : applications de l’App Store, configuration de votre abonnement et diffusion sur la télé avec AirPlay."),
    ("installer-iptv-mag", "MAG", "box",
     'Configurer l’IPTV sur un <span class="red">boîtier MAG</span>', "Configurer l’IPTV sur un boîtier MAG",
     "guide-boitier-iptv.jpg",
     "Configurer l’IPTV sur un boîtier MAG : adresse MAC, URL du portail, navigation, réglages image et son, dépannage et comparaison avec une box Android."),
    ("installer-iptv-windows", "Windows", "laptop",
     'Installer l’IPTV sur <span class="red">Windows</span>', "Installer l’IPTV sur un PC Windows",
     "installer-windows.jpg",
     "Installer l’IPTV sur Windows : téléchargement d’IPTV Smarters Pro sur le site officiel, connexion Xtream Codes, réglages recommandés et dépannage."),
]

def device_chips(r):
    return "".join(f'<a class="c dev-chip" href="{r}{slug}/">{ico(icon)}{label}</a>'
                   for slug, label, icon, *_ in DEVICE_GUIDES)

def _inline(t):
    import re as _re
    t = html.escape(t, quote=False)
    t = _re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = _re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    return t.replace("{brand}", SITE["brand"])

def parse_guide(text):
    """Format simple :
    ## Titre de section      -> nouvelle section (H2, dans le sommaire)
    ### Sous-titre           -> H3
    - élément / 1. élément   -> listes à puces / numérotées
    > texte                  -> encadré
    Q: question / R: réponse -> FAQ (n'importe où)
    [[cta]]                  -> encadré avec bouton WhatsApp (demande d'essai)
    ![nom-image.jpg]         -> image dans le texte (déclarer son alt dans IMG_ALT)
    ligne vide               -> sépare les paragraphes
    **gras** et [lien](url) sont acceptés ; {brand} et {R} sont remplacés."""
    sections, faq_items, cur, buf = [], [], None, []
    para, ul, ol = [], [], []
    def flush():
        nonlocal para, ul, ol
        if para: buf.append("<p>" + _inline(" ".join(para)) + "</p>"); para = []
        if ul: buf.append("<ul>" + "".join(f"<li>{_inline(x)}</li>" for x in ul) + "</ul>"); ul = []
        if ol: buf.append("<ol>" + "".join(f"<li>{_inline(x)}</li>" for x in ol) + "</ol>"); ol = []
    def close():
        nonlocal buf
        flush()
        if cur is not None: sections.append((cur, "".join(buf)))
        buf = []
    import re as _re
    q = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            close(); cur = _inline(line[3:])
        elif line.startswith("### "):
            flush(); buf.append(f"<h3>{_inline(line[4:])}</h3>")
        elif line.startswith("Q: "):
            flush(); q = _inline(line[3:])
        elif line.startswith("R: ") and q:
            faq_items.append((q, _inline(line[3:]))); q = None
        elif line == "[[cta]]":
            flush()
            buf.append(f'<div class="callout cta-inline"><p><strong>Envie de tester ?</strong> Essai gratuit de 24 h, '
                       f'activation rapide et aide à l’installation sur WhatsApp.</p>'
                       f'<a class="btn btn-red btn-sm" href="#" {wa_attr(msg_trial())}>Demander mon essai gratuit</a></div>')
        elif line.startswith("![") and line.endswith("]"):
            flush(); buf.append(img(line[2:-1].strip(), "page-img body-img"))
        elif line.startswith("> "):
            flush(); buf.append(f'<div class="callout">{_inline(line[2:])}</div>')
        elif line.startswith("<"):
            # HTML brut (tableaux) : copié tel quel, {brand}/{R} remplacés
            flush()
            raw = line.replace("{brand}", SITE["brand"])
            # les tableaux défilent dans leur cadre sur mobile au lieu d'élargir la page
            buf.append(f'<div class="table-wrap">{raw}</div>' if raw.startswith("<table") else raw)
        elif line.startswith("- "):
            if para or ol: flush()
            ul.append(line[2:])
        elif _re.match(r"\d+\. ", line):
            if para or ul: flush()
            ol.append(line.split(". ", 1)[1])
        elif not line:
            flush()
        else:
            if ul or ol: flush()
            para.append(line)
    close()
    return sections, faq_items

TRIAL_ARTICLE = ("essai-gratuit", "Essai IPTV gratuit sans risque", "Essai", "essai-gratuit-iptv.jpg",
                 "Essai IPTV gratuit de 24 heures : comment le demander, préparer votre appareil, ce qu’il faut vérifier pendant le test et comment choisir ensuite votre formule.")

def article_meta(slug):
    """slug -> (titre court, catégorie, image, résumé) pour tous les articles du blog."""
    if slug == TRIAL_ARTICLE[0]:
        return TRIAL_ARTICLE[1:]
    for s, title, cat, icon, summary in GUIDES:
        if s == slug:
            return title, cat, GUIDE_IMAGES.get(s), summary
    for s, label, icon, h1, short, image, summary in DEVICE_GUIDES:
        if s == slug:
            return short, f"Installation · {label}", image, summary
    raise KeyError(slug)

# Maillage interne : 3 articles liés par page (affichés en fin d’article).
RELATED = {
    "essai-gratuit": ["qu-est-ce-que-iptv", "meilleures-applications-iptv", "panne-iptv"],
    "qu-est-ce-que-iptv": ["meilleures-applications-iptv", "boitier-iptv", "essai-gratuit"],
    "meilleures-applications-iptv": ["guide-tivimate", "iptv-smarters-pro", "installer-iptv-smart-tv"],
    "iptv-android-box": ["installer-iptv-android", "guide-tivimate", "boitier-iptv"],
    "guide-tivimate": ["installer-iptv-fire-tv", "iptv-android-box", "meilleures-applications-iptv"],
    "iptv-smarters-pro": ["installer-iptv-ios", "installer-iptv-android", "meilleures-applications-iptv"],
    "iptv-fire-stick": ["installer-iptv-fire-tv", "guide-tivimate", "panne-iptv"],
    "panne-iptv": ["iptv-fire-stick", "boitier-iptv", "qu-est-ce-que-iptv"],
    "boitier-iptv": ["iptv-android-box", "installer-iptv-mag", "iptv-fire-stick"],
    "installer-iptv-smart-tv": ["meilleures-applications-iptv", "boitier-iptv", "panne-iptv"],
    "installer-iptv-fire-tv": ["iptv-fire-stick", "guide-tivimate", "panne-iptv"],
    "installer-iptv-android": ["iptv-android-box", "guide-tivimate", "iptv-smarters-pro"],
    "installer-iptv-ios": ["iptv-smarters-pro", "meilleures-applications-iptv", "essai-gratuit"],
    "installer-iptv-mag": ["boitier-iptv", "panne-iptv", "qu-est-ce-que-iptv"],
    "installer-iptv-windows": ["iptv-smarters-pro", "panne-iptv", "qu-est-ce-que-iptv"],
}

def related_block(slug):
    cards = []
    for s in RELATED.get(slug, []):
        title, cat, image, summary = article_meta(s)
        thumb = f'<div class="g-img">{img(image, "thumb-img")}</div>' if image else ""
        cards.append(f'<a class="post" href="{{R}}{s}/">{thumb}<div class="p-body"><span class="p-cat">{cat}</span>'
                     f'<h3>{title}</h3><p>{summary}</p></div></a>')
    if not cards:
        return ""
    return f'<div class="related"><h2 class="h-md">À lire aussi</h2><div class="post-grid related-grid">{"".join(cards)}</div></div>'

def device_sidebar(slug):
    items = "".join(f'<li><a href="{{R}}{s}/">{ico(icon)}{label}</a></li>'
                    for s, label, icon, *_ in DEVICE_GUIDES if s != slug)
    return f'<div class="toc-devices"><h4>Guides par appareil</h4><ul>{items}</ul></div>'

def build_txt_article(slug, kicker, h1, summary, image, folder):
    sections, faq_items = parse_guide((Path(__file__).resolve().parent / folder / f"{slug}.txt").read_text(encoding="utf-8"))
    words = sum(len(_re_words(x)) for _, x in sections) + sum(len(_re_words(q + " " + a)) for q, a in faq_items)
    mins = max(4, round(words / 220))
    article(f"{slug}/index.html", kicker, h1, summary, sections,
            faq_items=faq_items or None, read=f"{mins} min", image=image, slug=slug)
    print(f"   article {slug}: {words} mots")

def build_device_guides():
    for slug, label, icon, h1, short, image, summary in DEVICE_GUIDES:
        build_txt_article(slug, f"Installation {label}", h1, summary, image, "appareils")

def _re_words(htm):
    import re as _re
    return _re.sub(r"<[^>]+>", " ", htm).split()

def article(path, kicker, h1_html, intro, sections, faq_items=None, read="6 min", crumb="Blog", active="Blog", image=None, slug=None):
    toc_items = [(f"s{i}", s[0]) for i, s in enumerate(sections, 1)]
    if faq_items:
        toc_items.append(("faq", "Questions fréquentes"))
    toc = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc_items)
    content = "".join(f'<h2 id="s{i}">{t}</h2>{c}' for i, (t, c) in enumerate(sections, 1))
    if faq_items:
        content += f'<h2 id="faq">Questions fréquentes</h2><div class="faq-list" style="margin-top:10px">{faq(faq_items)}</div>'
    content += f"""
      <div class="end-cta">
        <h2 class="h-md">Testez {SITE["brand"]} gratuitement</h2>
        <p>Essai gratuit de 24 heures, activation rapide et support 24/7 sur WhatsApp.</p>
        <a class="btn btn-white" href="#" {wa_attr(msg_trial())}>Demander mon essai</a>
      </div>"""
    if slug:
        content += related_block(slug)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d’Ariane"><a href="{{R}}index.html">⌂</a> / <a href="{{R}}blog/">{crumb}</a> / <span>{kicker}</span></nav>
    <div class="article-grid">
      <div>
        <p class="kicker kicker-red">{kicker}</p>
        <h1>{h1_html}</h1>
        <p class="intro">{intro}</p>
        <div class="meta"><span>{SITE["year"]}</span><span>{read} de lecture</span><span>Équipe {SITE["brand"]}</span></div>
        {img(image, "page-img article-img", lazy=False) if image else ""}
        <div class="prose" style="margin-top:50px">{content}</div>
      </div>
      <aside class="toc">
        <h4>Sommaire</h4>
        <ol>{toc}</ol>
        {device_sidebar(slug) if slug else ""}
        <div class="cta-box"><p>Envie d’essayer ? Essai gratuit 24 h, sans engagement.</p><a class="btn btn-red btn-sm" href="{{R}}index.html#offres">Voir les offres</a></div>
      </aside>
    </div>
  </div>
</section>"""
    title_txt = html.unescape(h1_html.replace('<span class="red">', "").replace("</span>", "").replace("<br>", " "))
    page(path, f"{title_txt} | {SITE['brand']}", intro, body, active=active)

def P(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)

def UL(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def OL(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

# ---------------------------------------------------------------- pages
def build_trial():
    slug, title, cat, image, summary = TRIAL_ARTICLE
    build_txt_article(slug, "Essai IPTV gratuit", 'Essai IPTV <span class="red">gratuit</span><br>sans risque',
                      "Essai IPTV gratuit de 24 heures : testez la qualité, la stabilité et les chaînes sur votre propre connexion avant de payer, avec l’aide de notre support.",
                      image, "articles")

def device_cards(r="{R}"):
    return "".join(
        f'<a class="post" href="{r}{slug}/"><div class="g-img">{img(image, "thumb-img")}</div>'
        f'<div class="p-body"><span class="p-cat">Installation · {label}</span><h3>{short}</h3><p>{summary}</p></div></a>'
        for slug, label, icon, h1, short, image, summary in DEVICE_GUIDES)

BLOG_PER_PAGE = 9   # articles par page du blog (pagination /blog/, /blog/page/2/, …)

def blog_cards():
    """Toutes les cartes d’articles du blog, dans l’ordre d’affichage."""
    cards = ['<a class="post" href="{R}essai-gratuit/"><div class="g-img">' + img("essai-gratuit-iptv.jpg", "thumb-img") +
             '</div><div class="p-body"><span class="p-cat">Essai</span><h3>Essai IPTV gratuit sans risque</h3>'
             '<p>Comment tester l’IPTV pendant 24 heures et ce qu’il faut vérifier avant de choisir.</p></div></a>']
    for html_cards in (guide_cards(cls="post"), device_cards()):
        cards += ['<a class="post"' + c for c in html_cards.split('<a class="post"') if c]
    return cards

ARROW_L = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5m6-6-6 6 6 6"/></svg>'
ARROW_R = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'

def blog_url(n):
    return "{R}blog/#articles" if n == 1 else f"{{R}}blog/page/{n}/"

def pager(cur, total):
    if total < 2:
        return ""
    def arrow(n, svg, label):
        if 1 <= n <= total:
            return f'<a class="pg pg-arrow" href="{blog_url(n)}" aria-label="{label}">{svg}</a>'
        return f'<span class="pg pg-arrow is-disabled" aria-hidden="true">{svg}</span>'
    nums = "".join(f'<span class="pg is-current" aria-current="page">{n}</span>' if n == cur
                   else f'<a class="pg" href="{blog_url(n)}" aria-label="Page {n}">{n}</a>'
                   for n in range(1, total + 1))
    return (f'<nav class="pager" aria-label="Pages du blog">{arrow(cur - 1, ARROW_L, "Page précédente")}'
            f'{nums}{arrow(cur + 1, ARROW_R, "Page suivante")}</nav>')

def build_blog():
    cards = blog_cards()
    total = max(1, -(-len(cards) // BLOG_PER_PAGE))
    for n in range(1, total + 1):
        chunk = "".join(cards[(n - 1) * BLOG_PER_PAGE: n * BLOG_PER_PAGE])
        if n == 1:
            hero = f"""
<section class="hero hero-has-photo hero-blog">
  <div class="hero-bg">
    {img("blog-hero-salon.jpg", "hero-photo", lazy=False)}
  </div>
  <div class="wrap hero-content">
    <h1>Blog IPTV : tout savoir sur l’IPTV en France</h1>
    <p>Bienvenue sur le blog {SITE["brand"]}, le point de départ pour regarder la télé par internet. Guides d’installation, comparatifs d’applications et solutions aux problèmes courants : tout pour profiter pleinement de votre abonnement.</p>
  </div>
</section>"""
            heading = '<h2 class="h-md" style="margin-bottom:24px">Tous les articles</h2>'
        else:
            hero = ""
            heading = (f'<nav class="crumbs" aria-label="Fil d’Ariane"><a href="{{R}}index.html">⌂</a> / <a href="{{R}}blog/">Blog</a> / <span>Page {n}</span></nav>'
                       f'<h1 class="h-lg" style="margin:14px 0 24px">Blog IPTV : tous les articles <span class="red">(page {n})</span></h1>')
        body = f"""{hero}
<section class="section-tight" id="articles" style="padding-bottom:80px{';padding-top:50px' if n > 1 else ''}">
  <div class="wrap">
    {heading}
    <div class="post-grid">{chunk}</div>
    {pager(n, total)}
  </div>
</section>"""
        suffix = "" if n == 1 else f" – page {n}"
        path = "blog/index.html" if n == 1 else f"blog/page/{n}/index.html"
        page(path, f"Blog IPTV : guides, astuces et comparatifs (2026){suffix} | {SITE['brand']}",
             "Guides d’installation IPTV, comparatifs d’applications et solutions aux pannes courantes." + (f" Page {n}." if n > 1 else ""),
             body, active="Blog")
    # retirer les pages devenues inutiles si le nombre d’articles diminue
    import shutil
    pdir = ROOT / "blog" / "page"
    if pdir.exists():
        for d in pdir.iterdir():
            if d.is_dir() and (not d.name.isdigit() or int(d.name) > total or int(d.name) < 2):
                shutil.rmtree(d)

def build_contact():
    body = f"""
<section class="section">
  <div class="wrap" style="max-width:1000px">
    <p class="kicker kicker-red">Contact</p>
    <h1 class="h-xl" style="max-width:520px">Comment pouvons-nous vous aider ?</h1>
    <p class="intro" style="color:#a9adb5;font-size:16px;margin-top:20px;max-width:520px">Remplissez le formulaire : votre message s’ouvre directement dans WhatsApp pour une réponse rapide, 24 h/24.</p>
    {img("contact-sunday-iptv.jpg", "page-img wide-img", lazy=False)}
    <div class="contact-grid" style="margin-top:50px">
      <form class="form" id="contact-form">
        <p class="kicker kicker-red">Envoyer un message</p>
        <div class="field"><label for="cf-name">Votre nom</label><input id="cf-name" name="name" placeholder="Prénom et nom" required></div>
        <div class="field"><label for="cf-subject">Sujet</label>
          <select id="cf-subject" name="subject"><option>Commander un abonnement</option><option>Essai gratuit 24 h</option><option>Aide à l’installation</option><option>Problème technique</option><option>Autre question</option></select></div>
        <div class="field"><label for="cf-msg">Votre message</label><textarea id="cf-msg" name="message" placeholder="Indiquez votre appareil et votre question." required></textarea></div>
        <button class="btn btn-red" type="submit">Envoyer via WhatsApp</button>
      </form>
      <aside>
        <div class="side-box"><h2>Moyens de contact</h2>
          <div class="method">{ico("chat")}<div><b>WhatsApp</b><span class="pill">Recommandé</span><small>+{SITE["whatsapp"][:3]} {SITE["whatsapp"][3:6]} {SITE["whatsapp"][6:9]} {SITE["whatsapp"][9:]}</small><small>Réponse la plus rapide, 24/7</small></div></div>
          <div class="method">{ico("mail")}<div><b>E-mail</b><small><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></small><small>Réponse dans la journée</small></div></div>
        </div>
        <div class="side-box"><h2>Disponibilité</h2>
          <div class="hours"><div><span>Lundi – vendredi</span><span>24 h/24</span></div><div><span>Samedi – dimanche</span><span>24 h/24</span></div><div><span>Jours fériés</span><span>24 h/24</span></div></div>
        </div>
        <div class="side-box"><h2>Déjà une réponse ?</h2>
          <p style="font-size:13px">Consultez notre <a class="red" href="{{R}}index.html#faq">FAQ</a>, nos <a class="red" href="{{R}}blog/">guides d’installation</a> ou notre guide <a class="red" href="{{R}}panne-iptv/">panne IPTV</a>. Pour mieux nous connaître, lisez notre page <a class="red" href="{{R}}a-propos/">à propos</a>.</p>
        </div>
      </aside>
    </div>
  </div>
</section>"""
    page("contact/index.html", f"Contact {SITE['brand']} | Support WhatsApp 24/7",
         "Contactez le support IPTV par WhatsApp ou e-mail, 24 h/24 et 7 j/7.", body, active="Contact")

def build_about():
    body = f"""
<section class="section">
  <div class="wrap" style="max-width:1000px">
    <p class="kicker kicker-red">À propos</p>
    <h1 class="h-xl" style="max-width:640px">Nous construisons une IPTV plus stable pour la France.</h1>
    <p style="color:#a9adb5;font-size:16px;margin-top:20px;max-width:560px">{SITE["brand"]} propose un service IPTV simple et fiable pour les foyers francophones. Notre priorité : la stabilité technique, des prix clairs et un service personnalisé.</p>
    {img("a-propos-sunday-iptv.jpg", "page-img wide-img", lazy=False)}
    <div class="stats4"><div><strong>32 000+</strong><span>Chaînes</span></div><div><strong>220 000+</strong><span>Films &amp; séries</span></div><div><strong>4K</strong><span>Ultra HD</span></div><div><strong>24/7</strong><span>Support</span></div></div>

    <div class="prose" style="margin-top:60px">
      <h2>Notre histoire</h2>
      {P("Nous sommes partis d’un constat simple : beaucoup d’offres IPTV promettent tout, mais coupent au moment du match et disparaissent quand on a besoin d’aide. Nous avons voulu faire l’inverse.", "Des serveurs dimensionnés pour les soirées chargées, un support humain joignable à toute heure et des formules sans engagement : c’est ce qui guide chacune de nos décisions.")}
      <h2>Pourquoi {SITE["brand"]}</h2>
    </div>
    <div class="why4">
      <div>{ico("globe")}<h3>Serveurs répartis</h3><p>Une infrastructure répartie en Europe pour limiter les coupures et garder un démarrage rapide.</p></div>
      <div>{ico("monitor")}<h3>Tous les appareils</h3><p>Smart TV, Fire Stick, Android, Apple, PC ou boîtier MAG : un seul abonnement, l’écran de votre choix.</p></div>
      <div>{ico("tv")}<h3>Offre internationale</h3><p>Des chaînes françaises, belges, suisses et du monde entier, avec un catalogue VOD mis à jour en continu.</p></div>
      <div>{ico("shield")}<h3>Confidentialité</h3><p>Nous ne demandons que les informations nécessaires à la commande, et un VPN est inclus.</p></div>
    </div>
    <div class="prose" style="margin-top:50px">
      <h2>Transparence</h2>
      {P("Le prix affiché est le prix payé. Pas de frais d’activation, pas de renouvellement automatique, et un essai gratuit de 24 heures pour juger avant de payer.",
         f'Nos engagements sont détaillés dans nos <a href="{{R}}conditions-generales/">conditions générales</a>, notre <a href="{{R}}remboursement/">politique de remboursement</a> et notre <a href="{{R}}confidentialite/">politique de confidentialité</a>.',
         f'Une question ? <a href="{{R}}contact/">Contactez-nous</a>, nous répondons 24 h/24. Pour bien démarrer, consultez nos <a href="{{R}}blog/">guides d’installation</a> ou demandez un <a href="{{R}}essai-gratuit/">essai gratuit</a>.')}
    </div>
  </div>
</section>"""
    page("a-propos/index.html", f"À propos de {SITE['brand']} | Fournisseur IPTV",
         "Qui sommes-nous : un service IPTV stable, des prix clairs et un support humain 24/7.", body, active="À propos")

GUIDE_IMAGES = {
    "qu-est-ce-que-iptv": "guide-qu-est-ce-que-iptv.jpg",
    "meilleures-applications-iptv": "guide-meilleures-applications-iptv.jpg",
    "iptv-android-box": "guide-iptv-android-box.jpg",
    "guide-tivimate": "guide-tivimate.jpg",
    "iptv-smarters-pro": "guide-iptv-smarters-pro.jpg",
    "iptv-fire-stick": "guide-iptv-fire-stick.jpg",
    "panne-iptv": "guide-panne-iptv.jpg",
    "boitier-iptv": "guide-boitier-iptv.jpg",
}

def build_guides():
    for slug, title, cat, icon, summary in GUIDES:
        main = title.split(" (")[0]
        words = main.split(" ", 1)
        h1 = f'{words[0]} <span class="red">{words[1]}</span>' if len(words) > 1 else main
        build_txt_article(slug, cat, h1, summary, GUIDE_IMAGES.get(slug), "articles")

def build_cities():
    for slug, city in CITIES:
        body = f"""
<section class="section">
  <div class="wrap" style="max-width:1000px">
    <nav class="crumbs"><a href="{{R}}index.html">⌂</a> / <span>IPTV {city}</span></nav>
    <p class="kicker kicker-red">IPTV {city}</p>
    <h1 class="h-xl">Abonnement IPTV à <span class="red">{city}</span></h1>
    <p style="color:#a9adb5;font-size:16px;margin-top:20px;max-width:600px">Que vous soyez en fibre ou en ADSL, {SITE["brand"]} fonctionne partout à {city} et dans les environs. Activation en moins d’une heure, essai gratuit 24 h et support 24/7.</p>
    <div class="city-cards trust">
      <div class="trust-card">{ico("wifi")}<h3>Fibre et ADSL</h3><p>Compatible avec toutes les box internet. 10 Mb/s suffisent pour la HD.</p></div>
      <div class="trust-card">{ico("clock")}<h3>Activation rapide</h3><p>Vos identifiants arrivent en général en moins d’une heure.</p></div>
      <div class="trust-card">{ico("headset")}<h3>Aide à l’installation</h3><p>Nous vous guidons pas à pas sur WhatsApp, quel que soit votre appareil.</p></div>
    </div>
    {img(f"ville-{slug}.jpg", "page-img wide-img")}
    <div class="prose" style="margin-top:50px">
      <h2>Regarder la télé par internet à {city}</h2>
      {P(f"Avec l’IPTV, plus besoin de parabole ni de décodeur : votre connexion internet suffit pour regarder les chaînes françaises et internationales, le sport en direct et un large catalogue de films et séries.", "Toutes nos formules incluent la 4K, le replay et le guide des programmes.")}
      <h2>Installer l’IPTV à {city} : nos guides pas à pas</h2>
      {P(f"Que vous habitiez un appartement en centre-ville ou une maison en périphérie de {city}, l’installation est la même : une application sur votre appareil, vos identifiants, et c’est parti. Choisissez le guide qui correspond à votre équipement :")}
      <ul>{"".join(f'<li><a href="{{R}}{s}/">{short}</a></li>' for s, label, icon, h1, short, image, summary in DEVICE_GUIDES)}</ul>
      {P(f'Vous ne savez pas encore quel appareil utiliser ? Notre comparatif <a href="{{R}}boitier-iptv/">quel boîtier IPTV choisir</a> vous aide à trancher. Et pour tester sans risque, demandez notre <a href="{{R}}essai-gratuit/">essai gratuit de 24 heures</a>.')}
      <h2>Une connexion stable à {city}</h2>
      {P(f"La plupart des logements de {city} sont éligibles à la fibre, idéale pour la 4K. En ADSL, la HD et la Full HD restent tout à fait confortables. Dans les deux cas, branchez si possible votre télé ou votre boîtier en Ethernet : c’est la meilleure protection contre les coupures. En cas de souci, consultez notre guide <a href=\"{{R}}panne-iptv/\">panne IPTV</a>.")}
      <h2>IPTV dans d’autres villes</h2>
      <ul>{"".join(f'<li><a href="{{R}}{s}/">IPTV {c}</a></li>' for s, c in CITIES if s != slug)}</ul>
    </div>
  </div>
</section>
<section class="section-tight" style="padding-bottom:80px"><div class="wrap"><div class="plans">{plan_cards()}</div></div></section>"""
        page(f"{slug}/index.html", f"IPTV {city} : abonnement IPTV dès 5 €/mois | {SITE['brand']}",
             f"Abonnement IPTV à {city} : 32 000+ chaînes, 4K, essai gratuit 24 h, activation rapide.", body)

LEGAL_CONTENT = {
    "conditions-generales": [
        ("Objet", P(f"Les présentes conditions encadrent l’utilisation des services proposés par {SITE['brand']} et la souscription d’un abonnement.")),
        ("Commande et paiement", P("La commande est confirmée après réception du paiement. Le prix payé correspond à la durée choisie, sans frais supplémentaires.")),
        ("Durée", P("L’abonnement prend effet à l’activation et se termine à la fin de la période choisie. Il n’est pas renouvelé automatiquement.")),
        ("Utilisation", P("L’abonnement est personnel et permet une connexion simultanée, sauf offre multi-connexions. Le partage des identifiants est interdit.")),
        ("Responsabilité", P("Le service dépend de la qualité de la connexion internet de l’utilisateur. Des interruptions ponctuelles peuvent survenir pour maintenance.")),
        ("Contact", P(f"Pour toute question : {SITE['email']} ou WhatsApp.")),
    ],
    "confidentialite": [
        ("Données collectées", P("Nous collectons uniquement les informations nécessaires à la commande et au support : nom, moyen de contact et appareil utilisé.")),
        ("Utilisation des données", P("Ces données servent à livrer l’abonnement, assurer le support et vous informer d’éventuelles interruptions. Elles ne sont jamais revendues.")),
        ("Conservation", P("Les données sont conservées pendant la durée de l’abonnement puis supprimées dans un délai raisonnable.")),
        ("Vos droits", P(f"Vous pouvez demander l’accès, la rectification ou la suppression de vos données en écrivant à {SITE['email']}.")),
    ],
    "remboursement": [
        ("Essai avant achat", P("Un essai gratuit de 24 heures est proposé avant tout achat pour vérifier la compatibilité du service avec votre installation.")),
        ("Demande de remboursement", P("En cas de problème technique que notre support ne parvient pas à résoudre, contactez-nous pour étudier une solution ou un remboursement.")),
        ("Délais", P("Les demandes sont traitées sous quelques jours ouvrés après échange avec le support.")),
    ],
    "cookies": [
        ("Qu’est-ce qu’un cookie ?", P("Un cookie est un petit fichier enregistré par votre navigateur lorsque vous visitez un site.")),
        ("Cookies utilisés", P("Ce site n’utilise pas de cookies publicitaires. Seules des préférences techniques peuvent être enregistrées localement, comme la fermeture du bandeau d’information.")),
        ("Gérer les cookies", P("Vous pouvez supprimer ou bloquer les cookies à tout moment depuis les réglages de votre navigateur.")),
    ],
}

def build_legal():
    for slug, title in LEGAL:
        sections = LEGAL_CONTENT[slug]
        content = "".join(f"<h2>{t}</h2>{c}" for t, c in sections)
        body = f"""
<section class="section">
  <div class="wrap" style="max-width:820px">
    <nav class="crumbs"><a href="{{R}}index.html">⌂</a> / <span>{title}</span></nav>
    <p class="kicker kicker-red">Informations légales</p>
    <h1 class="h-lg">{title}</h1>
    <p style="color:#8d929b;font-size:13px;margin-top:12px">Dernière mise à jour : {SITE["year"]}</p>
    <div class="prose" style="margin-top:36px">{content}
      <h2>Autres informations légales</h2>
      <ul>{"".join(f'<li><a href="{{R}}{s}/">{t}</a></li>' for s, t in LEGAL if s != slug)}</ul>
      <p>Une question sur ces documents ? <a href="{{R}}contact/">Contactez-nous</a> ou découvrez <a href="{{R}}a-propos/">qui nous sommes</a>.</p>
    </div>
  </div>
</section>"""
        page(f"{slug}/index.html", f"{title} | {SITE['brand']}", f"{title} de {SITE['brand']}.", body)

def build_404():
    body = f"""
<section class="notfound"><div class="wrap">
  <p class="big">404</p>
  <h1 class="h-lg">Page introuvable</h1>
  <p style="margin-top:14px">La page que vous cherchez n’existe pas ou a été déplacée.</p>
  <a class="btn btn-red" style="margin-top:20px" href="{BASE}">Retour à l’accueil</a>
</div></section>"""
    # 404.html est servi à n'importe quelle profondeur : liens absolus vers le site du projet
    out = page("404.html", f"Page introuvable | {SITE['brand']}", "Page introuvable.", body, depth=0)
    txt = out.read_text(encoding="utf-8")
    txt = txt.replace('href="style.css?v=20"', f'href="{BASE}style.css?v=20"').replace('src="script.js?v=3"', f'src="{BASE}script.js?v=3"')
    txt = txt.replace('href="./', f'href="{BASE}')
    for slug, *_ in DEVICE_GUIDES:
        txt = txt.replace(f'href="{slug}/', f'href="{BASE}{slug}/')
    for f in ("favicon.svg", "favicon-32.png", "apple-touch-icon.png"):
        txt = txt.replace(f'href="{f}"', f'href="{BASE}{f}"')
    for prefix in ["blog/", "a-propos/", "contact/", "essai-gratuit/"] + [f"{s}/" for s, *_ in GUIDES] + [f"{s}/" for s, _ in CITIES] + [f"{s}/" for s, _ in LEGAL]:
        txt = txt.replace(f'href="{prefix}', f'href="{BASE}{prefix}')
    out.write_text(txt, encoding="utf-8")

BASE = "/" if SITE["domain"] else "/itv-tst-/"

def site_url():
    return f"https://{SITE['domain']}/" if SITE["domain"] else "https://tiaboussama-cpu.github.io/itv-tst-/"

def build_seo_files():
    """robots.txt + sitemap.xml (toutes les pages sauf la 404)."""
    import datetime
    base = site_url()
    today = datetime.date.today().isoformat()
    urls = []
    for p in sorted(ROOT.rglob("index.html")):
        if "_build" in p.parts:
            continue
        rel = p.parent.relative_to(ROOT).as_posix()
        loc = base if rel == "." else f"{base}{rel}/"
        if rel == ".":
            prio = "1.0"
        elif rel in ("essai-gratuit", "blog"):
            prio = "0.8"
        elif rel in {s for s, _ in LEGAL}:
            prio = "0.3"
        else:
            prio = "0.6"
        urls.append((loc, prio))
    urls.sort(key=lambda u: (-float(u[1]), u[0]))
    # <loc> uniquement : la date de génération n'est pas une vraie date de modification
    body = "".join(f"  <url>\n    <loc>{loc}</loc>\n  </url>\n" for loc, prio in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /_build/\n\n" f"Sitemap: {base}sitemap.xml\n", encoding="utf-8")

if __name__ == "__main__":
    build_home(); build_trial(); build_blog(); build_contact(); build_about()
    build_guides(); build_device_guides(); build_cities(); build_legal(); build_404()
    cname = ROOT / "CNAME"
    if SITE["domain"]:
        cname.write_text(SITE["domain"] + "\n", encoding="utf-8")
    elif cname.exists():
        cname.unlink()
    build_seo_files()
    pages = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.html") if "_build" not in p.parts)
    print(f"{len(pages)} pages générées :")
    for p in pages:
        print("  ", p)
