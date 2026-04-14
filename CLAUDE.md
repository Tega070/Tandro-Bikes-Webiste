# CLAUDE.md — Project Intelligence File

This file tells Claude Code how to behave in this workspace.
Read this before touching any file in this project.

---

## Who I Am

I'm an intermediate frontend developer based in Tbilisi, Georgia.
I build business websites, local service sites, and landing pages.
I deploy on Vercel, Netlify, and Cloudflare.
My stack is mixed — HTML/CSS/JS for simple projects, Next.js for complex ones.
I am not a CSS framework expert yet — explain choices, don't just use them.

---

## How I Want You to Work

- **Mobile-first always.** Every layout starts at 320px. No exceptions.
- **Ask before assuming.** If something is unclear, ask one focused question.
- **Don't over-engineer.** Simple projects get simple solutions.
- **Single HTML files for client demos** — fast to show, easy to understand.
- **Commit to design decisions.** Don't hedge. Make a choice and explain why.
- **Never use generic fonts** (Inter, Roboto, Arial as display). Pick something distinctive.
- **Never hardcode API keys** in any file. See security section below.
- When I say "build me X", build the real thing — not a wireframe, not pseudocode.
- When I say "fix X", fix only X. Don't rewrite unrelated code.
- Keep comments short and useful. Don't over-comment obvious things.

---

## Project Structure (default)

```
project/
├── .env.local          # ← SECRET KEYS LIVE HERE. Never commit this.
├── .env.example        # ← Template with placeholder values. Commit this.
├── .gitignore          # ← Must include .env* entries. Always.
├── CLAUDE.md           # ← This file
├── index.html          # ← Single-file projects
├── src/
│   ├── components/     # ← Reusable pieces
│   ├── pages/          # ← Next.js pages or HTML pages
│   └── styles/         # ← CSS files if not inline
└── public/             # ← Static assets
```

---

## 🔐 API KEY SECURITY — READ THIS FIRST

### The Rule: Never commit secrets to Git. Ever.

If an API key is exposed in a public GitHub repo, it can be stolen within
minutes by automated bots. Resend, Supabase, and Telegram keys can be
abused to send spam, read your database, or rack up bills.

---

### Step 1: Create `.env.local` (never commit this)

This is where all real keys live. Create this file manually. Never share it.

```bash
# .env.local — NEVER COMMIT THIS FILE

# Resend (email sending)
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxx

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Telegram Bot
TELEGRAM_BOT_TOKEN=123456789:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TELEGRAM_CHAT_ID=your_chat_id_here
```

> ⚠️ `NEXT_PUBLIC_` prefix = visible in browser. Use ONLY for public Supabase URL and anon key.
> Never use `NEXT_PUBLIC_` for Resend, Telegram, or Supabase service role key.

---

### Step 2: Create `.env.example` (always commit this)

This file shows the structure without real values.
Teammates and future-you will know what keys are needed.

```bash
# .env.example — COMMIT THIS FILE (no real values)

# Resend
RESEND_API_KEY=re_your_key_here

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

### Step 3: Create `.gitignore` (must include these lines)

```gitignore
# Environment variables — NEVER commit these
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
.env*.local

# Dependencies
node_modules/
.next/
dist/
build/

# System files
.DS_Store
Thumbs.db

# Editor
.vscode/settings.json
*.log
```

---

### Step 4: How to Use Keys in Code

**Next.js (server-side — API routes, server components):**
```javascript
// pages/api/send-email.js or app/api/send-email/route.js
const apiKey = process.env.RESEND_API_KEY; // ✅ server only, safe
```

**Next.js (client-side — only for public keys):**
```javascript
// Only NEXT_PUBLIC_ vars work in browser
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL; // ✅ safe, it's public
const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY; // ❌ undefined in browser (correct!)
```

**Plain HTML/JS projects:**
If you're building a single HTML file that needs to call an API,
NEVER put the key in the HTML file. Instead:
- Use a serverless function (Vercel Edge Function, Netlify Function, Cloudflare Worker)
- The HTML calls YOUR function → YOUR function uses the key → returns result
- The key never touches the browser

---

### Step 5: Check Before Every Git Push

Run this mental checklist before `git push`:

- [ ] Is `.env.local` in `.gitignore`? 
- [ ] Did I accidentally type a real key anywhere in `.js`, `.html`, `.ts` files?
- [ ] Does `.env.example` have placeholder values, not real ones?
- [ ] Am I using `process.env.X` in code, not a hardcoded string?

**Quick terminal check (run before pushing):**
```bash
# Search for potential exposed keys in your project
grep -r "re_" src/ --include="*.js" --include="*.ts" --include="*.html"
grep -r "eyJ" src/ --include="*.js" --include="*.ts"
grep -r "bot" src/ --include="*.js" --include="*.ts"
```

If any real key shows up in that grep — fix it before pushing.

---

### If You Already Pushed a Key by Accident

1. **Immediately revoke the key** in the service dashboard (Resend, Supabase, Telegram)
2. Generate a new key
3. Remove it from git history:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all
git push origin --force
```
4. Update `.env.local` with the new key

---

## Resend Setup (quick reference)

```javascript
// Install: npm install resend
import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

await resend.emails.send({
  from: 'noreply@yourdomain.com',
  to: 'client@example.com',
  subject: 'New booking request',
  html: '<p>Someone booked an appointment.</p>',
});
```

---

## Supabase Setup (quick reference)

```javascript
// Install: npm install @supabase/supabase-js
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);
```

---

## Telegram Bot Setup (quick reference)

```javascript
// Send a message via Telegram Bot API (server-side only)
const token = process.env.TELEGRAM_BOT_TOKEN;
const chatId = process.env.TELEGRAM_CHAT_ID;

await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    chat_id: chatId,
    text: `New booking from website:\n${details}`,
  }),
});
```

---

## Deployment: Environment Variables

### Vercel:
1. Go to Project → Settings → Environment Variables
2. Add each key from `.env.local`
3. Set scope: Production / Preview / Development as needed
4. Never use the Vercel UI to copy keys — type them fresh

### Netlify:
1. Site → Site Configuration → Environment Variables
2. Add keys one by one
3. Redeploy after adding

### Cloudflare Pages:
1. Project → Settings → Environment Variables
2. Add as encrypted secrets

---

## Design Defaults (when not specified)

- Font pairing: Cormorant Garamond (headings) + DM Sans (body)
- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px
- Border radius: 4px (sharp/luxury), 8px (modern), 16px (friendly)
- Transition: 250ms ease
- Max content width: 1200px, centered
- Mobile padding: 16px horizontal minimum

---

## What I'm Building Mostly

- Beauty salons, barbershops, local service businesses in Tbilisi
- Landing pages to show clients as demos before they hire me
- Sites that need to look expensive on a phone screen in 5 seconds

Keep this in mind when making design and code decisions.
