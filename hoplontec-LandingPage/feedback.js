/* Progressive enhancement only: native POST, validation and CAPTCHA still work
 * without JavaScript. No analytics, form-content storage, fetch or email address. */
(() => {
  'use strict';
  const form = document.querySelector('#feedback-form');
  if (form) {
    const button = form.querySelector('button[type="submit"]');
    const originalLabel = button.textContent;
    let sending = false;
    form.addEventListener('submit', (event) => {
      if (form.dataset.configured !== 'true' || sending) {
        event.preventDefault();
        return;
      }
      // Browser constraint validation happens before this event. Only an opaque
      // reference is added; it is per submission, never an installation/user ID.
      const bytes = new Uint8Array(16);
      if (globalThis.crypto?.getRandomValues) {
        crypto.getRandomValues(bytes);
        const reference = Array.from(bytes, byte => byte.toString(16).padStart(2, '0')).join('');
        form.elements.namedItem('reference').value = reference;
        form.elements.namedItem('_next').value = `${form.dataset.next}#reference=${reference}`;
      }
      sending = true;
      button.textContent = form.dataset.pending;
      button.disabled = true;
      form.setAttribute('aria-busy', 'true');
    });
    // Back from the provider or restoring from browser cache must allow retry.
    window.addEventListener('pageshow', () => {
      sending = false;
      button.disabled = false;
      button.textContent = originalLabel;
      form.removeAttribute('aria-busy');
    });
  }
  const receipt = document.querySelector('#feedback-reference');
  if (receipt) {
    const reference = new URLSearchParams(location.hash.slice(1)).get('reference');
    if (/^[a-f0-9]{32}$/.test(reference || '')) {
      receipt.querySelector('code').textContent = reference;
      receipt.hidden = false;
      // No referrer and no external scripts; the fragment never reaches GitHub.
      history.replaceState(null, '', location.pathname);
    }
  }
})();
