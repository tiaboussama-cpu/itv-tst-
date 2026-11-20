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
