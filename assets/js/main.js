/* ============================================================
   PRAMAS DIWAN — shared site behaviour
   ============================================================ */
(function(){
  "use strict";

  var WHATSAPP_NUMBER = "919999999999"; // TODO: replace with real WhatsApp business number
  window.PD_WHATSAPP_NUMBER = WHATSAPP_NUMBER;

  function waLink(message){
    return "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(message);
  }
  window.PD_waLink = waLink;

  document.addEventListener("DOMContentLoaded", function(){

    /* ---------- Mobile nav toggle ---------- */
    var toggle = document.querySelector(".nav-toggle");
    var navLinks = document.querySelector(".nav-links");
    if(toggle && navLinks){
      toggle.addEventListener("click", function(){
        navLinks.classList.toggle("open");
        var open = navLinks.classList.contains("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.style.overflow = open ? "hidden" : "";
      });
      navLinks.querySelectorAll("a").forEach(function(a){
        a.addEventListener("click", function(){
          navLinks.classList.remove("open");
          document.body.style.overflow = "";
        });
      });
    }

    /* ---------- Wire up every WhatsApp CTA ---------- */
    document.querySelectorAll("[data-whatsapp]").forEach(function(el){
      var msg = el.getAttribute("data-whatsapp") || "Hi Pramas, I'd like to know more about your coaching programs.";
      el.setAttribute("href", waLink(msg));
      el.setAttribute("target", "_blank");
      el.setAttribute("rel", "noopener");
    });

    /* ---------- Floating WhatsApp + sticky mobile CTA bar ---------- */
    var floatBtn = document.querySelector(".float-whatsapp");
    if(floatBtn){
      floatBtn.setAttribute("href", waLink("Hi Pramas, I found your website and I'd like to talk about coaching."));
      floatBtn.setAttribute("target", "_blank");
      floatBtn.setAttribute("rel", "noopener");
    }
    var sticky = document.querySelector(".sticky-cta");
    if(sticky){
      document.body.classList.add("has-sticky");
      window.addEventListener("scroll", function(){
        if(window.scrollY > 480){ sticky.classList.add("show"); }
        else { sticky.classList.remove("show"); }
      }, { passive:true });
    }

    /* ---------- FAQ accordion ---------- */
    document.querySelectorAll(".faq-item").forEach(function(item){
      var q = item.querySelector(".faq-q");
      var a = item.querySelector(".faq-a");
      if(!q || !a) return;
      q.addEventListener("click", function(){
        var isOpen = item.classList.contains("open");
        item.closest(".faq-list").querySelectorAll(".faq-item.open").forEach(function(openItem){
          if(openItem !== item){
            openItem.classList.remove("open");
            openItem.querySelector(".faq-a").style.maxHeight = null;
            openItem.querySelector(".faq-q").setAttribute("aria-expanded","false");
          }
        });
        if(isOpen){
          item.classList.remove("open");
          a.style.maxHeight = null;
          q.setAttribute("aria-expanded","false");
        } else {
          item.classList.add("open");
          a.style.maxHeight = a.scrollHeight + "px";
          q.setAttribute("aria-expanded","true");
        }
      });
    });

    /* ---------- Before / After drag slider ---------- */
    document.querySelectorAll(".ba-slider").forEach(function(slider){
      var before = slider.querySelector(".ba-before");
      var handle = slider.querySelector(".ba-handle");
      if(!before || !handle) return;
      var dragging = false;

      function setPos(clientX){
        var rect = slider.getBoundingClientRect();
        var pct = ((clientX - rect.left) / rect.width) * 100;
        pct = Math.max(6, Math.min(94, pct));
        before.style.width = pct + "%";
        handle.style.left = pct + "%";
      }
      function down(e){ dragging = true; slider.classList.add("dragging"); }
      function move(e){
        if(!dragging) return;
        var x = e.touches ? e.touches[0].clientX : e.clientX;
        setPos(x);
      }
      function up(){ dragging = false; slider.classList.remove("dragging"); }

      slider.addEventListener("mousedown", function(e){ down(e); setPos(e.clientX); });
      slider.addEventListener("touchstart", function(e){ down(e); setPos(e.touches[0].clientX); }, {passive:true});
      window.addEventListener("mousemove", move);
      window.addEventListener("touchmove", move, {passive:true});
      window.addEventListener("mouseup", up);
      window.addEventListener("touchend", up);

      // simple auto-demo sweep on load for visual interest
      setTimeout(function(){
        before.style.transition = "width 1.2s ease";
        handle.style.transition = "left 1.2s ease";
        setPos(slider.getBoundingClientRect().left + slider.getBoundingClientRect().width * 0.5);
        setTimeout(function(){
          before.style.transition = "";
          handle.style.transition = "";
        }, 1300);
      }, 500);
    });

    /* ---------- Scroll reveal ---------- */
    var revealEls = document.querySelectorAll(".reveal");
    if("IntersectionObserver" in window && revealEls.length){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(entry.isIntersecting){
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      }, { threshold:.12, rootMargin:"0px 0px -60px 0px" });
      revealEls.forEach(function(el){ io.observe(el); });
    } else {
      revealEls.forEach(function(el){ el.classList.add("in"); });
    }

    /* ---------- Animated stat counters ---------- */
    var counters = document.querySelectorAll("[data-counter]");
    if("IntersectionObserver" in window && counters.length){
      var cio = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(!entry.isIntersecting) return;
          var el = entry.target;
          var target = parseFloat(el.getAttribute("data-counter"));
          var suffix = el.getAttribute("data-suffix") || "";
          var dur = 1400, start = null;
          function step(ts){
            if(!start) start = ts;
            var p = Math.min((ts - start) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            var val = target % 1 === 0 ? Math.round(target * eased) : (target * eased).toFixed(1);
            el.textContent = val + suffix;
            if(p < 1) requestAnimationFrame(step);
          }
          requestAnimationFrame(step);
          cio.unobserve(el);
        });
      }, { threshold:.5 });
      counters.forEach(function(el){ cio.observe(el); });
    }

    /* ---------- Blog category filter ---------- */
    var filterBtns = document.querySelectorAll(".blog-filters button");
    var blogCards = document.querySelectorAll("[data-category]");
    if(filterBtns.length){
      filterBtns.forEach(function(btn){
        btn.addEventListener("click", function(){
          filterBtns.forEach(function(b){ b.classList.remove("active"); });
          btn.classList.add("active");
          var cat = btn.getAttribute("data-filter");
          blogCards.forEach(function(card){
            var show = cat === "all" || card.getAttribute("data-category") === cat;
            card.style.display = show ? "" : "none";
          });
        });
      });
    }

    /* ---------- Generic form handling (no backend — shows confirmation + opens WhatsApp) ---------- */
    document.querySelectorAll("form[data-lead-form]").forEach(function(form){
      form.addEventListener("submit", function(e){
        e.preventDefault();
        var data = new FormData(form);
        var name = data.get("name") || "there";
        var summary = [];
        data.forEach(function(value, key){
          if(value) summary.push(key + ": " + value);
        });
        var msg = "Hi Pramas, I just submitted the form on your website.\n" + summary.join("\n");

        var successBox = form.parentElement.querySelector(".form-success");
        if(successBox){
          form.style.display = "none";
          successBox.classList.add("show");
        }
        var waBtn = form.parentElement.querySelector(".form-success [data-whatsapp-submit]");
        if(waBtn){
          waBtn.setAttribute("href", waLink(msg));
          waBtn.setAttribute("target","_blank");
          waBtn.setAttribute("rel","noopener");
        }
        // In production: replace this block with a fetch() POST to your form backend / CRM.
        console.log("Lead captured:", Object.fromEntries(data.entries()));
      });
    });

    /* ---------- Footer year ---------- */
    document.querySelectorAll("[data-year]").forEach(function(el){
      el.textContent = new Date().getFullYear();
    });

  });
})();
