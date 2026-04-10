// ===== CART MANAGEMENT =====
const Cart = {
  items: JSON.parse(localStorage.getItem('ch_cart') || '[]'),

  save() {
    localStorage.setItem('ch_cart', JSON.stringify(this.items));
    this.updateBadge();
  },

  add(name, price, img) {
    const existing = this.items.find(i => i.name === name);
    if (existing) {
      existing.qty++;
    } else {
      this.items.push({ name, price, img, qty: 1 });
    }
    this.save();
    showToast(`${name} added to cart!`);
  },

  remove(name) {
    this.items = this.items.filter(i => i.name !== name);
    this.save();
  },

  updateQty(name, delta) {
    const item = this.items.find(i => i.name === name);
    if (item) {
      item.qty += delta;
      if (item.qty <= 0) this.remove(name);
      else this.save();
    }
  },

  total() {
    return this.items.reduce((sum, i) => sum + i.price * i.qty, 0);
  },

  count() {
    return this.items.reduce((sum, i) => sum + i.qty, 0);
  },

  clear() {
    this.items = [];
    this.save();
  },

  updateBadge() {
    const badge = document.querySelector('.cart-badge');
    if (badge) badge.textContent = this.count();
  }
};

// ===== AUTH =====
const Auth = {
  currentUser: JSON.parse(localStorage.getItem('ch_user') || 'null'),

  login(email, password) {
    const users = JSON.parse(localStorage.getItem('ch_users') || '[]');
    const user = users.find(u => u.email === email && u.password === password);
    if (user) {
      this.currentUser = user;
      localStorage.setItem('ch_user', JSON.stringify(user));
      return true;
    }
    return false;
  },

  signup(name, email, password) {
    const users = JSON.parse(localStorage.getItem('ch_users') || '[]');
    if (users.find(u => u.email === email)) return false;
    const user = { name, email, password };
    users.push(user);
    localStorage.setItem('ch_users', JSON.stringify(users));
    this.currentUser = user;
    localStorage.setItem('ch_user', JSON.stringify(user));
    return true;
  },

  logout() {
    this.currentUser = null;
    localStorage.removeItem('ch_user');
  }
};

// ===== TOAST =====
function showToast(msg) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2800);
}

// ===== HAMBURGER MENU =====
document.addEventListener('DOMContentLoaded', () => {
  Cart.updateBadge();

  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
  }

  // highlight active nav
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    if (link.href === window.location.href) link.classList.add('active');
  });
});
