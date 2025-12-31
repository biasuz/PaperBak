# CLAUDE.md - AI Assistant Guide for PaperBak

**Last Updated:** 2025-12-31
**Repository:** PaperBak
**Status:** New Project / Initial Setup

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Development Workflow](#development-workflow)
4. [Code Conventions](#code-conventions)
5. [Git Workflow](#git-workflow)
6. [AI Assistant Guidelines](#ai-assistant-guidelines)
7. [Testing Strategy](#testing-strategy)
8. [Documentation Standards](#documentation-standards)

---

## Project Overview

### Current State
This is a **new repository** in its initial setup phase. The project currently contains:
- Minimal README.md with project name
- No source code yet
- No build configuration
- No dependencies defined

### Project Purpose
**PaperBak** - Based on the project name, this appears to be related to paper-based backup systems, possibly for encoding digital data onto physical paper for archival purposes.

**Note to AI Assistants:** When developing features, verify the exact project purpose with the user before making assumptions about functionality.

---

## Repository Structure

### Recommended Structure (To Be Established)

```
PaperBak/
├── src/                    # Source code
│   ├── core/              # Core functionality
│   ├── utils/             # Utility functions
│   ├── cli/               # CLI interface (if applicable)
│   └── lib/               # Library code
├── tests/                 # Test files
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── fixtures/         # Test fixtures and data
├── docs/                  # Additional documentation
├── examples/              # Usage examples
├── scripts/               # Build and utility scripts
├── .github/               # GitHub workflows and templates
├── README.md              # Project overview and quick start
├── CLAUDE.md              # This file - AI assistant guide
├── LICENSE                # License file (TBD)
├── CONTRIBUTING.md        # Contribution guidelines (TBD)
└── package.json           # Project metadata and dependencies (TBD)
```

### Current Structure
```
PaperBak/
├── .git/                  # Git repository data
├── README.md              # Minimal project name only
└── CLAUDE.md              # This file
```

---

## Development Workflow

### Setting Up Development Environment

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd PaperBak
   ```

2. **Install Dependencies** (When applicable)
   ```bash
   # This will be defined once package.json exists
   npm install  # or yarn install, or other package manager
   ```

3. **Run Tests** (When applicable)
   ```bash
   # Test commands to be defined
   npm test
   ```

### Branch Strategy

- **main**: Production-ready code
- **claude/**: Prefix for AI-assisted development branches
  - Format: `claude/claude-md-<session-id>`
  - Example: `claude/claude-md-mjtyiu7q0vrdx7kz-7KG0V`
- **feature/**: Feature development branches
- **fix/**: Bug fix branches
- **docs/**: Documentation-only changes

---

## Code Conventions

### General Principles

1. **Simplicity Over Complexity**
   - Avoid over-engineering
   - Don't add features that aren't requested
   - Keep solutions focused and minimal
   - Three similar lines are better than premature abstraction

2. **Security First**
   - Validate all external inputs
   - Prevent OWASP Top 10 vulnerabilities (XSS, SQL injection, command injection, etc.)
   - Never commit secrets or credentials
   - Use environment variables for configuration

3. **Code Quality**
   - Write self-documenting code with clear naming
   - Add comments only where logic isn't self-evident
   - Prefer dedicated helper functions over inline complexity
   - Remove dead code completely (no commented-out code)

### Language-Specific Conventions

**To be established based on chosen technology stack.**

Recommendations:
- Choose one primary language for consistency
- Define naming conventions (camelCase, snake_case, PascalCase)
- Establish file organization patterns
- Set code formatting standards (use Prettier, Black, or similar)

### File Naming

- Use lowercase with hyphens for file names: `file-name.ext`
- Test files: `*.test.js`, `*.spec.js`, or `*_test.py`
- Keep names descriptive but concise

---

## Git Workflow

### Commit Guidelines

1. **Commit Message Format**
   ```
   <type>: <subject>

   <body (optional)>
   ```

   Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

   Examples:
   - `feat: add base64 encoding for paper backup`
   - `fix: correct QR code generation padding`
   - `docs: update README with installation instructions`

2. **Commit Best Practices**
   - Write clear, descriptive messages focusing on "why" not "what"
   - Keep commits atomic (one logical change per commit)
   - Don't commit files with secrets (.env, credentials.json)
   - Run tests before committing

### Pull Request Workflow

1. **Creating PRs**
   - Ensure all tests pass
   - Update documentation as needed
   - Provide clear PR description with:
     - Summary of changes (1-3 bullet points)
     - Test plan checklist
   - Reference related issues

2. **PR Review**
   - Address review feedback promptly
   - Keep PR scope focused
   - Rebase on main if needed

### Git Commands Reference

```bash
# Create new branch
git checkout -b claude/feature-name-<session-id>

# Stage and commit changes
git add .
git commit -m "feat: add new feature"

# Push to remote (with retry logic for network failures)
git push -u origin <branch-name>

# Fetch specific branch
git fetch origin <branch-name>

# Pull updates
git pull origin <branch-name>
```

---

## AI Assistant Guidelines

### Before Making Changes

1. **Always Read First**
   - NEVER propose changes to code you haven't read
   - Read entire files before modifying them
   - Understand context before suggesting changes

2. **Use Task Management**
   - Use TodoWrite tool for multi-step tasks (3+ steps)
   - Mark tasks as in_progress before starting
   - Complete one task before moving to next
   - Mark completed immediately after finishing

3. **Verify Assumptions**
   - Ask clarifying questions when requirements are unclear
   - Don't assume functionality based on project name alone
   - Check for existing patterns before introducing new ones

### When Making Changes

1. **Scope Control**
   - Only make requested changes
   - Don't add unrequested features or refactoring
   - Don't add error handling for impossible scenarios
   - Trust internal code and framework guarantees

2. **Documentation**
   - Update relevant docs when changing functionality
   - Don't add docstrings to unchanged code
   - Keep comments minimal and meaningful

3. **Testing**
   - Run existing tests after changes
   - Add tests for new functionality
   - Don't mark tasks complete if tests fail

### Tool Usage Preferences

1. **File Operations**
   - Use `Read` for reading files (not `cat`)
   - Use `Edit` for modifying files (not `sed/awk`)
   - Use `Write` for new files (not `echo >`)
   - Use `Glob` for finding files (not `find`)
   - Use `Grep` for searching content (not `grep`)

2. **Exploration**
   - Use `Task` tool with `subagent_type=Explore` for codebase exploration
   - Use parallel tool calls when operations are independent
   - Avoid bash commands for file operations

3. **Git Operations**
   - Always use branch format: `claude/description-<session-id>`
   - Use `git push -u origin <branch-name>`
   - Retry network failures up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
   - Never push to main directly

---

## Testing Strategy

### Testing Philosophy

1. **Test Coverage**
   - Aim for high coverage of critical paths
   - Focus on behavior, not implementation
   - Test edge cases and error conditions

2. **Test Types**
   - **Unit Tests**: Test individual functions/modules
   - **Integration Tests**: Test component interactions
   - **End-to-End Tests**: Test complete workflows (when applicable)

3. **Test Organization**
   - Keep tests close to source code or in dedicated `tests/` directory
   - Use descriptive test names: `test_<function>_<scenario>_<expected>`
   - Group related tests together

### Running Tests

```bash
# To be defined based on chosen framework
# Examples:
npm test              # JavaScript/TypeScript
pytest                # Python
cargo test            # Rust
go test ./...         # Go
```

---

## Documentation Standards

### Code Documentation

1. **Inline Comments**
   - Explain "why" not "what"
   - Document non-obvious behavior
   - Keep comments up-to-date with code

2. **Function/Method Documentation**
   - Document public APIs
   - Include parameter descriptions
   - Specify return values and exceptions
   - Provide usage examples for complex functions

### Project Documentation

1. **README.md**
   - Project overview and purpose
   - Installation instructions
   - Quick start guide
   - Basic usage examples
   - Link to additional documentation

2. **CONTRIBUTING.md** (To be created)
   - How to set up development environment
   - Coding standards
   - Testing requirements
   - PR process

3. **API Documentation** (If applicable)
   - Auto-generate from code comments
   - Keep examples up-to-date
   - Version documentation with releases

### Changelog

- Maintain CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/)
- Update with each release
- Categories: Added, Changed, Deprecated, Removed, Fixed, Security

---

## Technology Stack

### To Be Determined

The following decisions need to be made:

1. **Primary Language**: Python, JavaScript/TypeScript, Rust, Go, or other?
2. **Build System**: npm, cargo, make, or other?
3. **Testing Framework**: Jest, pytest, cargo test, or other?
4. **Code Formatting**: Prettier, Black, rustfmt, or other?
5. **Linting**: ESLint, pylint, clippy, or other?
6. **CI/CD**: GitHub Actions, GitLab CI, or other?

**Action for AI Assistants:** Before adding dependencies or build configuration, confirm the technology choices with the user.

---

## Project-Specific Notes

### PaperBak Considerations

If this project is indeed about paper-based backups:

1. **Data Encoding**
   - Consider QR codes, bar codes, or custom encoding schemes
   - Handle data redundancy and error correction
   - Support for splitting large files across multiple pages

2. **Print Formatting**
   - Page layout and margins
   - Print density vs. scanning reliability
   - Support for different paper sizes

3. **Data Recovery**
   - Scanning and OCR capabilities
   - Error detection and correction
   - Data verification and checksums

4. **Security**
   - Optional encryption before encoding
   - Key management considerations
   - Privacy of printed data

**Note:** These are speculative based on the project name. Verify actual requirements with the user.

---

## Common Commands Quick Reference

```bash
# Development
<package-manager> install    # Install dependencies
<package-manager> test       # Run tests
<package-manager> build      # Build project

# Git workflow
git checkout -b claude/<description>-<session-id>
git add .
git commit -m "<type>: <description>"
git push -u origin <branch-name>

# View status
git status
git log --oneline -10
```

---

## Maintenance

### Updating This Document

- Update when project structure changes significantly
- Update when new conventions are established
- Update when technology stack is chosen/changed
- Include update date at the top
- Keep examples current

### Review Schedule

- Review quarterly or after major milestones
- Archive outdated sections
- Keep document concise and actionable

---

## Questions or Issues?

When encountering unclear situations:

1. Check existing documentation
2. Look for similar patterns in the codebase
3. Ask the user for clarification
4. Document decisions made for future reference

---

**Remember:** This document guides AI assistants and human developers. Keep it accurate, concise, and up-to-date.
