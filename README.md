# prompt-MD 📝

A powerful markdown-based prompt management system for organizing, versioning, and sharing AI prompts.

## Features

- 📂 **Organized Storage**: Store prompts in markdown files with metadata
- 🔍 **Easy Search**: Find prompts by tags, categories, or keywords
- 📋 **Template System**: Create reusable prompt templates
- 🔄 **Version Control**: Track prompt changes and improvements
- 💻 **CLI Tool**: Manage prompts from the command line
- 📊 **Statistics**: Track prompt usage and effectiveness

## Installation

```bash
# Clone the repository
git clone https://github.com/mpichadze-bot/prompt-MD.git
cd prompt-MD

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Create a new prompt
python prompt_md.py create --title "My First Prompt" --category "general"

# List all prompts
python prompt_md.py list

# Search for prompts
python prompt_md.py search --tag "coding"

# View a specific prompt
python prompt_md.py view "My First Prompt"

# Export prompts
python prompt_md.py export --format json
```

## Project Structure

```
prompt-MD/
├── prompts/              # Your prompt library
│   ├── coding/          # Coding-related prompts
│   ├── writing/         # Writing prompts
│   ├── analysis/        # Analysis prompts
│   └── templates/       # Reusable templates
├── prompt_md.py         # Main CLI tool
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Prompt Format

Each prompt is stored as a markdown file with YAML frontmatter:

```markdown
---
title: Code Review Helper
category: coding
tags: [review, quality, best-practices]
version: 1.0
created: 2025-12-02
updated: 2025-12-02
---

# Code Review Helper

Please review the following code for:
- Code quality and readability
- Potential bugs or issues
- Performance improvements
- Best practices

{{CODE_BLOCK}}
```

## Examples

Check out the `prompts/` directory for example prompts including:
- Code generation and debugging
- Writing and content creation
- Data analysis and research
- Creative brainstorming

## Contributing

Contributions are welcome! Feel free to:
- Add new prompts to the library
- Improve the CLI tool
- Suggest new features
- Report bugs

## License

MIT License - feel free to use and modify as needed.

## Author

Created by mpichadze-bot

---

**Happy Prompting! 🚀**

