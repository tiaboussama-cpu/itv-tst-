(function () {
  var number = (window.SITE_WHATSAPP || "").replace(/\D/g, "");

  // Liens WhatsApp avec message pré-rempli
  function waLink(msg) {
    return number ? "https://wa.me/" + number + "?text=" + encodeURIComponent(msg) : null;
  }
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var url = waLink(el.getAttribute("data-wa") || "");
    if (url) { el.href = url; el.target = "_blank"; el.rel = "noopener"; }
    else {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        alert("Numéro WhatsApp à configurer (SITE['whatsapp'] dans _build/build.py).");
      });
    }
  });

  // Fenêtre de commande : le client remplit appareil + application, puis WhatsApp s'ouvre
  var brand = window.SITE_BRAND || "Sunday IPTV";
  var DEVICES = ["Smart TV Samsung", "Smart TV LG", "Autre Smart TV", "Fire TV Stick", "Box Android", "iPhone / iPad", "Téléphone Android", "Boîtier MAG", "PC / Mac", "Autre"];
  var orderBtns = document.querySelectorAll("[data-order-dur]");
  if (orderBtns.length && typeof HTMLDialogElement === "function") {
    var dlg = document.createElement("dialog");
    dlg.className = "order-dlg";
    dlg.setAttribute("aria-labelledby", "od-title");
    dlg.innerHTML =
      '<form class="od-form" method="dialog" novalidate>' +
        '<button type="button" class="od-close" aria-label="Fermer">✕</button>' +
        '<p class="od-kicker">Votre commande</p>' +
        '<h2 id="od-title" class="od-title"></h2>' +
        '<label class="od-field"><span>Votre appareil <b class="red">*</b></span>' +
          '<select name="device" required><option value="">Choisissez votre appareil…</option>' +
          DEVICES.map(function (d) { return "<option>" + d + "</option>"; }).join("") +
          '</select><small class="od-err" hidden>Merci d’indiquer votre appareil.</small></label>' +
        '<label class="od-field"><span>Application utilisée <em>(facultatif)</em></span>' +
          '<input name="app" type="text" maxlength="60" placeholder="ex. IPTV Smarters, TiviMate…" autocomplete="off"></label>' +
        '<p class="od-label">Aperçu du message</p>' +
        '<pre class="od-preview"></pre>' +
        '<button type="submit" class="btn btn-red od-send">Envoyer sur WhatsApp</button>' +
        '<p class="od-note">Vous recevrez le lien de paiement sécurisé directement sur WhatsApp.</p>' +
      '</form>';
    document.body.appendChild(dlg);

    var f = dlg.querySelector("form"), current = null;
    var buildMsg = function () {
      var dev = f.device.value || "(Smart TV, Fire Stick, box Android, iPhone…)";
      var app = f.app.value.trim() || "aucune pour le moment";
      return "Bonjour " + brand + " 👋\n" +
        "Je souhaite commander l’abonnement " + current.dur + " à " + current.price + " €.\n\n" +
        "Mon appareil : " + dev + "\n" +
        "Application utilisée : " + app + "\n\n" +
        "Merci de m’envoyer le lien de paiement.";
    };
    var refresh = function () { dlg.querySelector(".od-preview").textContent = buildMsg(); };
    f.device.addEventListener("change", function () { dlg.querySelector(".od-err").hidden = true; f.device.classList.remove("invalid"); refresh(); });
    f.app.addEventListener("input", refresh);
    dlg.querySelector(".od-close").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });

    orderBtns.forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        current = { dur: btn.getAttribute("data-order-dur"), price: btn.getAttribute("data-order-price") };
        dlg.querySelector(".od-title").textContent = "Abonnement " + current.dur + " — " + current.price + "\u00a0€";
        dlg.querySelector(".od-err").hidden = true;
        f.device.classList.remove("invalid");
        refresh();
        dlg.showModal();
      });
    });

    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!f.device.value) {
        dlg.querySelector(".od-err").hidden = false;
        f.device.classList.add("invalid");
        f.device.focus();
        return;
      }
      var url = waLink(buildMsg());
      if (url) window.open(url, "_blank", "noopener");
      else alert("Numéro WhatsApp à configurer (SITE['whatsapp'] dans _build/build.py).");
      dlg.close();
    });
  }

  // Bandeau d'information
  var notice = document.getElementById("notice");
  try { if (notice && localStorage.getItem("notice-closed") === "1") notice.remove(); } catch (e) {}
  var close = document.querySelector(".notice-close");
  if (close) close.addEventListener("click", function () {
    notice.remove();
    try { localStorage.setItem("notice-closed", "1"); } catch (e) {}
  });

  // Menu mobile
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "✕" : "☰";
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); toggle.textContent = "☰"; });
    });
  }

  // Carrousel des guides
  document.querySelectorAll(".carousel").forEach(function (c) {
    var track = c.querySelector(".c-track");
    var step = function () { return track.clientWidth * 0.8; };
    c.querySelector(".c-prev").addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
    c.querySelector(".c-next").addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });
  });

  // FAQ : une seule question ouverte à la fois
  document.querySelectorAll(".faq-list").forEach(function (list) {
    var items = list.querySelectorAll("details");
    items.forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (d.open) items.forEach(function (o) { if (o !== d) o.open = false; });
      });
    });
  });

  // Formulaire de contact -> WhatsApp
  var form = document.getElementById("contact-form");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var msg = "Bonjour Sunday IPTV 👋\nJe m’appelle " + form.name.value + ".\nSujet : " + form.subject.value + "\n\n" + form.message.value;
    var url = waLink(msg);
    if (url) window.open(url, "_blank", "noopener");
    else alert("Numéro WhatsApp à configurer (SITE['whatsapp'] dans _build/build.py).");
  });

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
