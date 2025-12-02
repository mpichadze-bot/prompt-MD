#!/usr/bin/env python3
"""
prompt-MD: A markdown-based prompt management system
"""

import os
import sys
import argparse
import yaml
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class PromptManager:
    def __init__(self, base_dir: str = "prompts"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        
    def create_prompt(self, title: str, category: str, content: str, tags: List[str] = None) -> str:
        """Create a new prompt"""
        if tags is None:
            tags = []
            
        # Create category directory if it doesn't exist
        category_dir = self.base_dir / category
        category_dir.mkdir(exist_ok=True)
        
        # Generate filename from title
        filename = self._sanitize_filename(title) + ".md"
        filepath = category_dir / filename
        
        # Check if file already exists
        if filepath.exists():
            print(f"Error: Prompt '{title}' already exists!")
            return None
        
        # Create frontmatter
        frontmatter = {
            'title': title,
            'category': category,
            'tags': tags,
            'version': '1.0',
            'created': datetime.now().strftime('%Y-%m-%d'),
            'updated': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Write prompt file
        with open(filepath, 'w') as f:
            f.write('---\n')
            f.write(yaml.dump(frontmatter, default_flow_style=False))
            f.write('---\n\n')
            f.write(f"# {title}\n\n")
            f.write(content + '\n')
        
        print(f"✓ Created prompt: {filepath}")
        return str(filepath)
    
    def list_prompts(self, category: Optional[str] = None) -> List[Dict]:
        """List all prompts"""
        prompts = []
        
        search_dir = self.base_dir / category if category else self.base_dir
        
        for filepath in search_dir.rglob("*.md"):
            try:
                metadata = self._read_frontmatter(filepath)
                if metadata:
                    metadata['filepath'] = str(filepath)
                    prompts.append(metadata)
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
        
        return prompts
    
    def search_prompts(self, query: str = None, tag: str = None) -> List[Dict]:
        """Search prompts by query or tag"""
        all_prompts = self.list_prompts()
        results = []
        
        for prompt in all_prompts:
            if tag and tag in prompt.get('tags', []):
                results.append(prompt)
            elif query:
                # Search in title and content
                if query.lower() in prompt.get('title', '').lower():
                    results.append(prompt)
                else:
                    # Read file content
                    with open(prompt['filepath'], 'r') as f:
                        content = f.read()
                        if query.lower() in content.lower():
                            results.append(prompt)
        
        return results
    
    def view_prompt(self, title: str) -> Optional[str]:
        """View a specific prompt"""
        prompts = self.list_prompts()
        
        for prompt in prompts:
            if prompt['title'].lower() == title.lower():
                with open(prompt['filepath'], 'r') as f:
                    return f.read()
        
        return None
    
    def export_prompts(self, format: str = 'json') -> str:
        """Export all prompts"""
        prompts = self.list_prompts()
        
        if format == 'json':
            return json.dumps(prompts, indent=2)
        elif format == 'yaml':
            return yaml.dump(prompts, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _read_frontmatter(self, filepath: Path) -> Optional[Dict]:
        """Read YAML frontmatter from a markdown file"""
        with open(filepath, 'r') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        try:
            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                return frontmatter
        except Exception:
            return None
        
        return None
    
    def _sanitize_filename(self, title: str) -> str:
        """Convert title to safe filename"""
        return "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in title.lower().replace(' ', '_'))


def main():
    parser = argparse.ArgumentParser(description='prompt-MD: Manage your AI prompts')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new prompt')
    create_parser.add_argument('--title', required=True, help='Prompt title')
    create_parser.add_argument('--category', required=True, help='Prompt category')
    create_parser.add_argument('--content', default='Your prompt content here...', help='Prompt content')
    create_parser.add_argument('--tags', nargs='*', default=[], help='Tags (space-separated)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all prompts')
    list_parser.add_argument('--category', help='Filter by category')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search prompts')
    search_parser.add_argument('--query', help='Search query')
    search_parser.add_argument('--tag', help='Filter by tag')
    
    # View command
    view_parser = subparsers.add_parser('view', help='View a prompt')
    view_parser.add_argument('title', help='Prompt title')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export prompts')
    export_parser.add_argument('--format', choices=['json', 'yaml'], default='json', help='Export format')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = PromptManager()
    
    if args.command == 'create':
        manager.create_prompt(args.title, args.category, args.content, args.tags)
    
    elif args.command == 'list':
        prompts = manager.list_prompts(args.category)
        if prompts:
            print(f"\n📋 Found {len(prompts)} prompt(s):\n")
            for prompt in prompts:
                tags_str = ', '.join(prompt.get('tags', []))
                print(f"  • {prompt['title']}")
                print(f"    Category: {prompt['category']} | Tags: {tags_str}")
                print(f"    Updated: {prompt.get('updated', 'N/A')}\n")
        else:
            print("No prompts found.")
    
    elif args.command == 'search':
        results = manager.search_prompts(args.query, args.tag)
        if results:
            print(f"\n🔍 Found {len(results)} result(s):\n")
            for prompt in results:
                print(f"  • {prompt['title']} ({prompt['category']})")
        else:
            print("No results found.")
    
    elif args.command == 'view':
        content = manager.view_prompt(args.title)
        if content:
            print("\n" + "="*60)
            print(content)
            print("="*60)
        else:
            print(f"Prompt '{args.title}' not found.")
    
    elif args.command == 'export':
        output = manager.export_prompts(args.format)
        print(output)


if __name__ == '__main__':
    main()

