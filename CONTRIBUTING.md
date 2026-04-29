# 🤝 Contributing to LinkedIn Job & Skills Analyzer

First off — thanks for considering contributing! 🎉

This project is open-source and community-driven. Every contribution helps make career planning more accessible.

---

## 🌱 Ways to Contribute

You don't have to write code to help! Here are different ways:

| Type | What you can do |
|---|---|
| 🐛 **Bug reports** | Found something broken? [Open an issue](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/issues) |
| 💡 **Feature requests** | Have an idea? Share it in issues with the `enhancement` label |
| 📖 **Documentation** | Improve README, add tutorials, fix typos |
| 🎨 **Design** | Suggest UI improvements, share mockups |
| 💻 **Code** | Fix bugs, implement features (see below) |
| ⭐ **Star the repo** | Helps others discover the project |
| 📢 **Share** | Tell friends, tweet about it, write a blog post |

---

## 🛠️ Code Contributions

### 1. Set up your dev environment

See [docs/SETUP.md](docs/SETUP.md) for full instructions.

```bash
git clone https://github.com/YOUR-USERNAME/linkedin-job-analyzer-tool.git
cd linkedin-job-analyzer-tool
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your free Groq key
streamlit run app.py
```

### 2. Pick something to work on

- Browse [open issues](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/issues)
- Comment on an issue to claim it
- Or propose your own feature first via an issue

### 3. Make your changes

```bash
git checkout -b feat/your-feature-name

# ... make your changes ...

git add .
git commit -m "feat: short description of what you did"
git push origin feat/your-feature-name
```

### 4. Open a Pull Request

- Go to your fork on GitHub → **Compare & pull request**
- Describe what you changed and why
- Link the related issue (if any) with `Closes #123`

---

## ✅ PR Checklist

Before submitting, please ensure:

- [ ] Code runs locally without errors (`streamlit run app.py`)
- [ ] No API keys, secrets, or personal info committed
- [ ] New features have brief documentation in `docs/`
- [ ] Commit messages are clear and use [Conventional Commits](https://www.conventionalcommits.org/) style:
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation only
  - `refactor:` code restructure, no behaviour change
  - `chore:` tooling, dependencies

---

## 🎯 Code Style

- **Python:** PEP 8, prefer type hints
- **Keep it simple** — no unnecessary abstractions
- **Treat user inputs as untrusted** (resumes, job descriptions, URLs)
- **Use structured JSON output** from AI (no free-form parsing)
- **Don't add new dependencies lightly** — prefer stdlib when possible

---

## 💡 Good First Issues

Some ideas for newcomers:

- 🌍 Add internationalisation (i18n) — translate UI to other languages
- 📊 Add a "Compare two jobs side-by-side" feature
- 💾 Save user's favourite jobs to local storage / file
- 🎨 New themes (dark mode, high contrast)
- 🤖 Add support for other free AI providers (Together AI, Anthropic, Cohere)
- 📈 Visualisations — charts for skill trends with `plotly`
- 🔔 Email notifications for new matching jobs
- 📱 Mobile-responsive improvements

---

## 📜 Code of Conduct

Be respectful, constructive, and inclusive.
We follow a simple rule: **be kind**.

- No harassment, discrimination, or personal attacks
- Welcome newcomers and answer questions patiently
- Disagree with ideas, never with people

---

## 🙋 Questions?

- 🐛 [Open an issue](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/issues)
- 💬 [Start a discussion](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/discussions)
- 📧 Contact the maintainer: **arunsuthar98@gmail.com**

---

## 🌟 Recognition

All contributors are listed in the project README and our **[Contributors](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/graphs/contributors)** page.

Thanks for making this project better! 💙
