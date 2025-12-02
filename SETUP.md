# Setup and Deployment Guide

## ✅ Project Status

Your **prompt-MD** project is fully created and ready to push to GitHub!

**Location**: `/Users/mpichadze/prompt-MD`

## 📦 What's Included

- ✓ Full Python CLI tool for managing prompts
- ✓ 7 example prompts across multiple categories
- ✓ Complete documentation (README)
- ✓ MIT License
- ✓ Git repository initialized
- ✓ All files committed locally

## 🚀 Push to GitHub

To push this project to https://github.com/mpichadze-bot/prompt-MD, you need to authenticate with GitHub.

### Option 1: Using Personal Access Token (Recommended)

1. **Create a Personal Access Token** on GitHub:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Give it a name (e.g., "prompt-MD")
   - Select scopes: `repo` (full control)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

2. **Push to GitHub**:
   ```bash
   cd ~/prompt-MD
   git push -u origin main
   ```
   
   When prompted for username: Enter `mpichadze-bot`
   When prompted for password: **Paste your Personal Access Token**

### Option 2: Using SSH

1. **Set up SSH keys** (if you haven't already):
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   cat ~/.ssh/id_ed25519.pub
   ```

2. **Add the SSH key to GitHub**:
   - Copy the output from the cat command
   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste the key and save

3. **Change remote to SSH and push**:
   ```bash
   cd ~/prompt-MD
   git remote set-url origin git@github.com:mpichadze-bot/prompt-MD.git
   git push -u origin main
   ```

### Option 3: Using GitHub CLI (gh)

```bash
# Install GitHub CLI
brew install gh

# Authenticate
gh auth login

# Push
cd ~/prompt-MD
gh repo view mpichadze-bot/prompt-MD --web  # Verify repo exists
git push -u origin main
```

## 🎯 Quick Test

Test the CLI tool locally:

```bash
cd ~/prompt-MD

# List all prompts
python3 prompt_md.py list

# Search for coding prompts
python3 prompt_md.py search --tag coding

# View a specific prompt
python3 prompt_md.py view "Code Review Helper"

# Create a new prompt
python3 prompt_md.py create --title "My Custom Prompt" --category "custom" --tags test demo

# Export all prompts to JSON
python3 prompt_md.py export --format json
```

## 📂 Project Structure

```
prompt-MD/
├── README.md                           # Main documentation
├── LICENSE                             # MIT License
├── requirements.txt                    # Python dependencies
├── prompt_md.py                        # CLI tool (executable)
├── .gitignore                          # Git ignore rules
├── SETUP.md                            # This file
└── prompts/                            # Prompt library
    ├── coding/                         # Coding prompts
    │   ├── code_review.md
    │   ├── debug_helper.md
    │   └── explain_code.md
    ├── writing/                        # Writing prompts
    │   ├── blog_post.md
    │   └── email_writer.md
    ├── analysis/                       # Analysis prompts
    │   └── data_analysis.md
    └── templates/                      # Reusable templates
        └── basic_template.md
```

## 🔧 Next Steps

1. **Push to GitHub** using one of the methods above
2. **Verify on GitHub**: Visit https://github.com/mpichadze-bot/prompt-MD
3. **Customize**: Add your own prompts
4. **Share**: Invite collaborators or make it public

## 📝 Notes

- All commits are under the name `mpichadze-bot`
- The main branch is set up and ready
- Dependencies are already installed locally
- The CLI tool is executable

## 💡 Tips

- Create prompts using the CLI: `python3 prompt_md.py create`
- Organize prompts by category for easy management
- Use tags to make prompts searchable
- Export prompts to share with others

---

**Happy Prompting! 🎉**

