#!/usr/bin/env python3
"""Generates index.html, privacy.html and support.html for Twitchy Samurai.

Every page carries all six languages; the language bar jumps between them.
Edit the text below and run:  python3 build.py
"""
from pathlib import Path

LANGS = [("en", "English"), ("de", "Deutsch"), ("fr", "Français"), ("es", "Español"), ("it", "Italiano"), ("ja", "日本語")]
EMAIL = "mashu.support@gmail.com"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
GOOGLE_PARTNERS = "https://policies.google.com/technologies/partner-sites"

PRIVACY = {
    "en": {
        "title": "Privacy Policy",
        "updated": "Last updated: September 27, 2026",
        "intro": "This policy explains how the iOS app “Twitchy Samurai” (“the App”) handles information.",
        "sections": [
            ("Information we collect", ["The App does not collect personal information such as your name or email address. It has no account registration."]),
            ("Advertising", [
                "The App shows ads through Google AdMob, a service provided by Google. To serve and measure ads, AdMob may use information such as your device’s advertising identifier (IDFA), IP address and general usage data.",
                "The advertising identifier is used only if you allow tracking in the iOS App Tracking Transparency prompt. If you don’t, you will still see ads, but they will not be personalized.",
                "For how Google uses data, see: {google}",
            ]),
            ("Users in the EEA, the UK and Switzerland", [
                "Before any ads are shown, the App asks for your consent through Google’s consent tool (User Messaging Platform), as required by the GDPR. You can change your choice at any time from “Privacy settings” on the App’s title screen.",
            ]),
            ("Information stored on your device", ["Your best solo streak and your settings are stored only on your device. They are never sent to us."]),
            ("Children", ["The App is not directed at children under 13."]),
            ("Contact", ["For questions about this policy, email: {email}"]),
            ("Changes to this policy", ["We may update this policy when laws or the App change. The updated policy takes effect when it is posted on this page."]),
        ],
        "google_privacy": "Google Privacy Policy",
        "google_partners": "How Google uses information from sites or apps that use its services",
    },
    "de": {
        "title": "Datenschutzerklärung",
        "updated": "Zuletzt aktualisiert: 27. September 2026",
        "intro": "Diese Erklärung beschreibt, wie die iOS-App „Twitchy Samurai“ („die App“) mit Informationen umgeht.",
        "sections": [
            ("Welche Daten wir erheben", ["Die App erhebt keine personenbezogenen Daten wie Name oder E-Mail-Adresse. Es gibt keine Kontoregistrierung."]),
            ("Werbung", [
                "Die App zeigt Werbung über Google AdMob, einen Dienst von Google. Um Werbung auszuliefern und zu messen, kann AdMob Informationen wie die Werbe-ID deines Geräts (IDFA), die IP-Adresse und allgemeine Nutzungsdaten verwenden.",
                "Die Werbe-ID wird nur verwendet, wenn du das Tracking in der iOS-Abfrage „App-Tracking-Transparenz“ erlaubst. Wenn nicht, siehst du weiterhin Werbung, aber keine personalisierte.",
                "Wie Google Daten verwendet, erfährst du hier: {google}",
            ]),
            ("Nutzer im EWR, im Vereinigten Königreich und in der Schweiz", [
                "Bevor Werbung angezeigt wird, bittet die App gemäß DSGVO über das Einwilligungstool von Google (User Messaging Platform) um deine Einwilligung. Du kannst deine Auswahl jederzeit über „Datenschutz-Einstellungen“ auf dem Startbildschirm der App ändern.",
            ]),
            ("Auf deinem Gerät gespeicherte Daten", ["Deine beste Solo-Serie und deine Einstellungen werden nur auf deinem Gerät gespeichert. Sie werden niemals an uns gesendet."]),
            ("Kinder", ["Die App richtet sich nicht an Kinder unter 13 Jahren."]),
            ("Kontakt", ["Bei Fragen zu dieser Erklärung schreib uns: {email}"]),
            ("Änderungen", ["Wir können diese Erklärung anpassen, wenn sich Gesetze oder die App ändern. Die aktualisierte Fassung gilt ab Veröffentlichung auf dieser Seite."]),
        ],
        "google_privacy": "Datenschutzerklärung von Google",
        "google_partners": "Wie Google Daten von Websites oder Apps von Partnern verwendet",
    },
    "fr": {
        "title": "Politique de confidentialité",
        "updated": "Dernière mise à jour : 27 septembre 2026",
        "intro": "Cette politique explique comment l’application iOS « Twitchy Samurai » (« l’Application ») traite les informations.",
        "sections": [
            ("Informations collectées", ["L’Application ne collecte aucune donnée personnelle comme votre nom ou votre adresse e-mail. Elle ne nécessite aucun compte."]),
            ("Publicité", [
                "L’Application affiche des publicités via Google AdMob, un service fourni par Google. Pour diffuser et mesurer les publicités, AdMob peut utiliser des informations comme l’identifiant publicitaire de votre appareil (IDFA), votre adresse IP et des données d’utilisation générales.",
                "L’identifiant publicitaire n’est utilisé que si vous autorisez le suivi dans la demande « Transparence du suivi des apps » d’iOS. Sinon, des publicités continuent de s’afficher, mais elles ne sont pas personnalisées.",
                "Pour savoir comment Google utilise les données : {google}",
            ]),
            ("Utilisateurs de l’EEE, du Royaume-Uni et de Suisse", [
                "Avant d’afficher des publicités, l’Application demande votre consentement via l’outil de consentement de Google (User Messaging Platform), conformément au RGPD. Vous pouvez modifier votre choix à tout moment depuis « Paramètres de confidentialité » sur l’écran d’accueil de l’Application.",
            ]),
            ("Informations stockées sur votre appareil", ["Votre meilleure série en solo et vos réglages sont stockés uniquement sur votre appareil. Ils ne nous sont jamais envoyés."]),
            ("Enfants", ["L’Application ne s’adresse pas aux enfants de moins de 13 ans."]),
            ("Contact", ["Pour toute question sur cette politique, écrivez-nous : {email}"]),
            ("Modifications", ["Nous pouvons modifier cette politique en cas d’évolution de la loi ou de l’Application. La version mise à jour s’applique dès sa publication sur cette page."]),
        ],
        "google_privacy": "Règles de confidentialité de Google",
        "google_partners": "Comment Google utilise les informations des sites ou applications qui utilisent ses services",
    },
    "es": {
        "title": "Política de privacidad",
        "updated": "Última actualización: 27 de septiembre de 2026",
        "intro": "Esta política explica cómo la app para iOS «Twitchy Samurai» («la App») trata la información.",
        "sections": [
            ("Información que recopilamos", ["La App no recopila información personal como tu nombre o tu correo electrónico. No requiere registro de cuenta."]),
            ("Publicidad", [
                "La App muestra anuncios mediante Google AdMob, un servicio de Google. Para mostrar y medir los anuncios, AdMob puede usar información como el identificador de publicidad de tu dispositivo (IDFA), tu dirección IP y datos generales de uso.",
                "El identificador de publicidad solo se usa si permites el rastreo en el aviso «Transparencia de rastreo de apps» de iOS. Si no lo permites, seguirás viendo anuncios, pero no serán personalizados.",
                "Para saber cómo usa Google los datos: {google}",
            ]),
            ("Usuarios del EEE, el Reino Unido y Suiza", [
                "Antes de mostrar anuncios, la App solicita tu consentimiento mediante la herramienta de consentimiento de Google (User Messaging Platform), tal como exige el RGPD. Puedes cambiar tu elección en cualquier momento desde «Ajustes de privacidad» en la pantalla de inicio de la App.",
            ]),
            ("Información guardada en tu dispositivo", ["Tu mejor racha en solitario y tus ajustes se guardan solo en tu dispositivo. Nunca se nos envían."]),
            ("Menores", ["La App no está dirigida a menores de 13 años."]),
            ("Contacto", ["Si tienes preguntas sobre esta política, escríbenos a: {email}"]),
            ("Cambios", ["Podemos actualizar esta política si cambian las leyes o la App. La versión actualizada entra en vigor cuando se publica en esta página."]),
        ],
        "google_privacy": "Política de privacidad de Google",
        "google_partners": "Cómo usa Google la información de sitios web o aplicaciones que utilizan sus servicios",
    },
    "it": {
        "title": "Informativa sulla privacy",
        "updated": "Ultimo aggiornamento: 27 settembre 2026",
        "intro": "Questa informativa spiega come l’app per iOS “Twitchy Samurai” (“l’App”) tratta le informazioni.",
        "sections": [
            ("Informazioni raccolte", ["L’App non raccoglie dati personali come nome o indirizzo e-mail. Non richiede la registrazione di un account."]),
            ("Pubblicità", [
                "L’App mostra annunci tramite Google AdMob, un servizio fornito da Google. Per pubblicare e misurare gli annunci, AdMob può usare informazioni come l’identificatore pubblicitario del dispositivo (IDFA), l’indirizzo IP e dati generali di utilizzo.",
                "L’identificatore pubblicitario viene usato solo se consenti il tracciamento nella richiesta “Trasparenza sul tracciamento delle app” di iOS. In caso contrario vedrai comunque annunci, ma non personalizzati.",
                "Per sapere come Google usa i dati: {google}",
            ]),
            ("Utenti nel SEE, nel Regno Unito e in Svizzera", [
                "Prima di mostrare annunci, l’App chiede il tuo consenso tramite lo strumento di consenso di Google (User Messaging Platform), come richiesto dal GDPR. Puoi modificare la tua scelta in qualsiasi momento da “Impostazioni privacy” nella schermata iniziale dell’App.",
            ]),
            ("Informazioni salvate sul dispositivo", ["La tua miglior serie in solo e le tue impostazioni sono salvate solo sul tuo dispositivo. Non ci vengono mai inviate."]),
            ("Minori", ["L’App non è rivolta a minori di 13 anni."]),
            ("Contatti", ["Per domande su questa informativa, scrivici a: {email}"]),
            ("Modifiche", ["Potremmo aggiornare questa informativa in caso di modifiche alla legge o all’App. La versione aggiornata è valida dal momento della pubblicazione su questa pagina."]),
        ],
        "google_privacy": "Norme sulla privacy di Google",
        "google_partners": "Come Google utilizza le informazioni dei siti o delle app che utilizzano i suoi servizi",
    },
    "ja": {
        "title": "プライバシーポリシー",
        "updated": "最終更新日：2026年9月27日",
        "intro": "本ポリシーは、iOSアプリ「Twitchy Samurai」（以下「本アプリ」）における情報の取り扱いについて説明するものです。",
        "sections": [
            ("収集する情報", ["本アプリは、氏名・メールアドレス等の個人情報を収集しません。アカウント登録機能もありません。"]),
            ("広告について", [
                "本アプリは、Google社が提供する広告配信サービス「Google AdMob」を利用しています。AdMobは、広告の配信・効果測定のために、端末の広告識別子（IDFA）、IPアドレス、一般的な利用状況などの情報を利用する場合があります。",
                "広告識別子は、iOSの「Appによるトラッキングの要求（App Tracking Transparency）」でユーザーが許可した場合にのみ利用されます。許可しない場合でも、パーソナライズされていない広告が表示されます。",
                "Google社によるデータの取り扱いについては、以下をご確認ください：{google}",
            ]),
            ("EEA・英国・スイスのユーザーの方へ", [
                "本アプリは、GDPRに基づき、広告を表示する前にGoogle社の同意管理ツール（User Messaging Platform）で同意を確認します。選択内容は、本アプリのトップ画面の「プライバシー設定」からいつでも変更できます。",
            ]),
            ("端末内に保存する情報", ["ひとりプレイの最高連勝記録と設定は、お使いの端末内にのみ保存されます。外部に送信されることはありません。"]),
            ("お子様について", ["本アプリは13歳未満のお子様を対象としていません。"]),
            ("お問い合わせ", ["本ポリシーに関するお問い合わせは、以下のメールアドレスまでご連絡ください：{email}"]),
            ("ポリシーの変更", ["本ポリシーの内容は、法令やサービス内容の変更に応じて予告なく変更される場合があります。変更後のポリシーは本ページに掲載した時点で効力を生じるものとします。"]),
        ],
        "google_privacy": "Google プライバシーポリシー",
        "google_partners": "Google がパートナーのサイトやアプリを使用する際のデータ活用方法",
    },
}

SUPPORT = {
    "en": {
        "title": "Support",
        "about_h": "About the game",
        "about": "Twitchy Samurai is a quick-draw reflex game. Strike the instant the gold ! appears, and don’t fall for the traps.",
        "howto_h": "How to play",
        "howto": [
            "Tap the screen the instant the gold ! appears.",
            "Don’t tap for the traps: a gold ?, a blue !, or the signal sound with nothing on screen.",
            "Tapping too early is a false start, and you lose the round.",
            "SOLO: beat the time limit. It gets shorter with every win.",
            "DUEL: two players, one phone. Each takes one end of the screen. First to 3 wins.",
        ],
        "contact_h": "Contact",
        "contact": "For bug reports, feedback or questions, email:",
    },
    "de": {
        "title": "Support",
        "about_h": "Über das Spiel",
        "about": "Twitchy Samurai ist ein Reaktionsspiel im Stil eines Schnellzieh-Duells. Schlag in dem Moment zu, in dem das goldene ! erscheint, und fall nicht auf die Fallen herein.",
        "howto_h": "So wird gespielt",
        "howto": [
            "Tippe auf den Bildschirm, sobald das goldene ! erscheint.",
            "Tippe nicht bei den Fallen: ein goldenes ?, ein blaues ! oder nur das Signalgeräusch ohne Anzeige.",
            "Wer zu früh tippt, macht einen Fehlstart und verliert die Runde.",
            "SOLO: Schlag das Zeitlimit. Es wird mit jedem Sieg kürzer.",
            "DUELL: Zwei Spieler, ein Handy. Jeder nimmt ein Ende des Bildschirms. Wer zuerst 3 hat, gewinnt.",
        ],
        "contact_h": "Kontakt",
        "contact": "Fehlerberichte, Feedback oder Fragen bitte per E-Mail an:",
    },
    "fr": {
        "title": "Assistance",
        "about_h": "À propos du jeu",
        "about": "Twitchy Samurai est un jeu de réflexes façon duel de dégainage. Frappez dès que le ! doré apparaît, sans tomber dans les pièges.",
        "howto_h": "Comment jouer",
        "howto": [
            "Touchez l’écran dès que le ! doré apparaît.",
            "Ne touchez pas pour les pièges : un ? doré, un ! bleu, ou le son du signal sans rien à l’écran.",
            "Toucher trop tôt est un faux départ : vous perdez la manche.",
            "SOLO : battez la limite de temps. Elle raccourcit à chaque victoire.",
            "DUEL : deux joueurs, un téléphone. Chacun prend un bout de l’écran. Le premier à 3 gagne.",
        ],
        "contact_h": "Contact",
        "contact": "Pour signaler un bug, donner votre avis ou poser une question, écrivez à :",
    },
    "es": {
        "title": "Soporte",
        "about_h": "Sobre el juego",
        "about": "Twitchy Samurai es un juego de reflejos al estilo de un duelo a desenvainar. Ataca en cuanto aparezca el ! dorado y no caigas en las trampas.",
        "howto_h": "Cómo jugar",
        "howto": [
            "Toca la pantalla en cuanto aparezca el ! dorado.",
            "No toques con las trampas: un ? dorado, un ! azul o el sonido de la señal sin nada en pantalla.",
            "Tocar antes de tiempo es una salida en falso y pierdes la ronda.",
            "SOLO: supera el límite de tiempo. Se acorta con cada victoria.",
            "DUELO: dos jugadores, un móvil. Cada uno toma un extremo de la pantalla. Gana quien llegue a 3.",
        ],
        "contact_h": "Contacto",
        "contact": "Para informar de errores, enviar comentarios o hacer preguntas, escribe a:",
    },
    "it": {
        "title": "Assistenza",
        "about_h": "Il gioco",
        "about": "Twitchy Samurai è un gioco di riflessi in stile duello all’estrazione rapida. Colpisci nell’istante in cui appare il ! dorato e non cadere nelle trappole.",
        "howto_h": "Come si gioca",
        "howto": [
            "Tocca lo schermo appena appare il ! dorato.",
            "Non toccare per le trappole: un ? dorato, un ! blu o il suono del segnale senza niente sullo schermo.",
            "Toccare troppo presto è una falsa partenza e perdi il round.",
            "SOLO: batti il limite di tempo. Si accorcia a ogni vittoria.",
            "DUELLO: due giocatori, un telefono. Ognuno prende un’estremità dello schermo. Vince chi arriva a 3.",
        ],
        "contact_h": "Contatti",
        "contact": "Per segnalare bug, lasciare un commento o fare domande, scrivi a:",
    },
    "ja": {
        "title": "サポート",
        "about_h": "アプリについて",
        "about": "「Twitchy Samurai」は、居合の早抜き勝負をモチーフにした反射神経ゲームです。金の「!」が出た瞬間に斬り、ワナには引っかからないようにしましょう。",
        "howto_h": "遊び方",
        "howto": [
            "金の「!」が出た瞬間に画面をタップします",
            "ワナ（金の「?」、青の「!」、画面に何も出ずに音だけ鳴る）ではタップしないでください",
            "合図より前にタップするとフライングで負けになります",
            "ひとり：制限時間内に斬れば勝ち。勝つたびに制限時間が短くなります",
            "対戦：1台のiPhoneの両端をふたりで持って対戦します。先に3勝した方の勝ちです",
        ],
        "contact_h": "お問い合わせ",
        "contact": "不具合報告・ご意見・ご質問は、以下のメールアドレスまでお願いします。",
    },
}

INDEX = {
    "en": ("A quick-draw reflex game. Strike only on the gold !", "Support", "Privacy Policy"),
    "de": ("Ein Reaktionsspiel im Schnellzieh-Duell. Schlag nur beim goldenen ! zu.", "Support", "Datenschutzerklärung"),
    "fr": ("Un jeu de réflexes façon duel de dégainage. Frappez seulement sur le ! doré.", "Assistance", "Politique de confidentialité"),
    "es": ("Un juego de reflejos de duelo a desenvainar. Ataca solo con el ! dorado.", "Soporte", "Política de privacidad"),
    "it": ("Un gioco di riflessi da duello all’estrazione rapida. Colpisci solo sul ! dorato.", "Assistenza", "Informativa sulla privacy"),
    "ja": ("居合の早抜き勝負の反射神経ゲーム。金の「!」が出たら斬れ。", "サポート", "プライバシーポリシー"),
}

CSS = """
  :root { --ink: #2A2135; --gold: #B8860B; --line: #e7e2ec; --muted: #6f6878; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans", sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; line-height: 1.75; color: var(--ink); }
  h1 { font-size: 1.6em; margin-bottom: 0.2em; }
  h2 { font-size: 1.15em; margin-top: 1.8em; border-bottom: 2px solid var(--line); padding-bottom: 4px; }
  a { color: var(--gold); }
  nav.langs { display: flex; flex-wrap: wrap; gap: 6px 14px; padding: 10px 0; border-bottom: 1px solid var(--line); margin-bottom: 8px; font-size: 0.95em; }
  section.lang { padding-top: 12px; }
  section.lang + section.lang { border-top: 4px solid var(--line); margin-top: 48px; }
  .updated { color: var(--muted); font-size: 0.9em; }
  .back { margin-top: 2em; }
  .center { text-align: center; }
  a.button { display: inline-block; margin: 6px; padding: 10px 24px; background: var(--ink); color: #fff; text-decoration: none; border-radius: 24px; font-weight: 600; }
"""


def page(title: str, body: str) -> str:
    nav = "".join(f'<a href="#{code}">{name}</a>' for code, name in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<nav class="langs">{nav}</nav>
{body}
</body>
</html>
"""


def privacy() -> str:
    out = []
    for code, _ in LANGS:
        p = PRIVACY[code]
        google = (f'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">{p["google_privacy"]}</a> / '
                  f'<a href="{GOOGLE_PARTNERS}" target="_blank" rel="noopener">{p["google_partners"]}</a>')
        email = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
        parts = [f'<section class="lang" id="{code}" lang="{code}">', f'<h1>{p["title"]}</h1>',
                 f'<p class="updated">{p["updated"]}</p>', f'<p>{p["intro"]}</p>']
        for heading, paras in p["sections"]:
            parts.append(f"<h2>{heading}</h2>")
            parts += [f"<p>{para.format(google=google, email=email)}</p>" for para in paras]
        parts.append('<p class="back"><a href="./index.html">Twitchy Samurai</a></p></section>')
        out.append("\n".join(parts))
    return page("Privacy Policy | Twitchy Samurai", "\n".join(out))


def support() -> str:
    out = []
    for code, _ in LANGS:
        s = SUPPORT[code]
        items = "".join(f"<li>{x}</li>" for x in s["howto"])
        out.append(f"""<section class="lang" id="{code}" lang="{code}">
<h1>{s["title"]}</h1>
<h2>{s["about_h"]}</h2>
<p>{s["about"]}</p>
<h2>{s["howto_h"]}</h2>
<ul>{items}</ul>
<h2>{s["contact_h"]}</h2>
<p>{s["contact"]}</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="back"><a href="./index.html">Twitchy Samurai</a></p>
</section>""")
    return page("Support | Twitchy Samurai", "\n".join(out))


def index() -> str:
    out = []
    for code, _ in LANGS:
        tagline, sup, priv = INDEX[code]
        out.append(f"""<section class="lang center" id="{code}" lang="{code}">
<h1>Twitchy Samurai</h1>
<p>{tagline}</p>
<p><a class="button" href="./support.html#{code}">{sup}</a><a class="button" href="./privacy.html#{code}">{priv}</a></p>
</section>""")
    return page("Twitchy Samurai", "\n".join(out))


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    (root / "privacy.html").write_text(privacy())
    (root / "support.html").write_text(support())
    (root / "index.html").write_text(index())
    print("wrote index.html, privacy.html, support.html")
