// OVERCOAT PRISM - MASTER JAVASCRIPT ENGINE
// Synchronized with Ridevora Interaction Standards

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dynamic Year
  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // 2. Mobile Navigation Toggle
  const navToggle = document.querySelector('.nav-toggle');
  const mainNav = document.getElementById('main-nav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', () => {
      const isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // 3. Back to Top Button
  const toTop = document.querySelector('.to-top');
  if (toTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        toTop.classList.add('visible');
      } else {
        toTop.classList.remove('visible');
      }
    });
    toTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 4. Cookie Consent Dialog
  const cookieBanner = document.querySelector('.cookie');
  const cookieButtons = document.querySelectorAll('[data-consent]');
  const cookieOpenBtn = document.querySelector('[data-open-cookies]');

  if (cookieBanner) {
    if (!localStorage.getItem('op_cookie_consent')) {
      setTimeout(() => cookieBanner.classList.add('show'), 800);
    }
    cookieButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const choice = btn.getAttribute('data-consent');
        localStorage.setItem('op_cookie_consent', choice);
        cookieBanner.classList.remove('show');
      });
    });
    if (cookieOpenBtn) {
      cookieOpenBtn.addEventListener('click', () => {
        cookieBanner.classList.add('show');
      });
    }
  }

  // 5. Interactive Stepper & Bespoke Fitting Calculator (booking.html)
  const bookingForm = document.getElementById('booking-form');
  if (bookingForm) {
    let currentStep = 1;
    let selectedSilhouette = { name: 'Double-Breasted Officer Greatcoat', rate: 280 };
    let selectedExtras = 0;
    let sessions = 1;

    const panels = document.querySelectorAll('.b-panel');
    const stepIndicators = document.querySelectorAll('.stepper li');
    const sumPiece = document.getElementById('sum-car');
    const sumTrip = document.getElementById('sum-trip');
    const sumLines = document.getElementById('sum-lines');
    const sumTotal = document.getElementById('sum-total');

    function updateSummary() {
      if (sumPiece) sumPiece.textContent = selectedSilhouette.name;
      if (sumTrip) {
        sumTrip.innerHTML = `<li><span>Fitting Atelier:</span> <b>Chicago Magnificent Mile</b></li>
                             <li><span>Consultation Scope:</span> <b>Master Tailor Patterning</b></li>`;
      }
      const baseCost = selectedSilhouette.rate;
      const total = baseCost + selectedExtras;
      if (sumLines) {
        sumLines.innerHTML = `<li><span>Initial Bespoke Fitting &amp; Consultation:</span> <b>$${baseCost}</b></li>
                              <li><span>Selected Curation &amp; Cloth Sampling:</span> <b>$${selectedExtras}</b></li>`;
      }
      if (sumTotal) sumTotal.textContent = `$${total.toLocaleString()}`;
    }

    function goToStep(step) {
      currentStep = step;
      panels.forEach(p => {
        p.classList.toggle('active', parseInt(p.getAttribute('data-step')) === currentStep);
      });
      stepIndicators.forEach(li => {
        const s = parseInt(li.getAttribute('data-step'));
        li.classList.toggle('active', s === currentStep);
      });
      window.scrollTo({ top: bookingForm.offsetTop - 80, behavior: 'smooth' });
    }

    document.querySelectorAll('[data-next]').forEach(btn => {
      btn.addEventListener('click', () => {
        if (currentStep < 4) goToStep(currentStep + 1);
      });
    });

    document.querySelectorAll('[data-prev]').forEach(btn => {
      btn.addEventListener('click', () => {
        if (currentStep > 1) goToStep(currentStep - 1);
      });
    });

    // Pick cards
    document.querySelectorAll('.pick-card').forEach(card => {
      card.addEventListener('click', () => {
        document.querySelectorAll('.pick-card').forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        const name = card.querySelector('h4').textContent;
        const rate = parseInt(card.getAttribute('data-rate')) || 280;
        selectedSilhouette = { name, rate };
        updateSummary();
      });
    });

    // Extras
    document.querySelectorAll('.extra-item input[type="checkbox"]').forEach(box => {
      box.addEventListener('change', () => {
        selectedExtras = 0;
        document.querySelectorAll('.extra-item input[type="checkbox"]:checked').forEach(c => {
          selectedExtras += parseInt(c.value) || 0;
        });
        updateSummary();
      });
    });

    // Form submit
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const terms = document.getElementById('b-terms');
      if (terms && !terms.checked) {
        alert('Please review and agree to the Terms & Conditions and Bespoke Tailoring Policy.');
        return;
      }
      alert('Thank you for requesting a bespoke fitting appointment with Overcoat Prism. Our master tailor concierge will review your schedule and transmit your confirmed appointment card within two business hours.');
      bookingForm.reset();
      goToStep(1);
    });

    updateSummary();
  }

  // 6. Contact Form feedback
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thank you for contacting Overcoat Prism Atelier. Our concierge desk will review your message and reply within one business day.');
      contactForm.reset();
    });
  }
});
