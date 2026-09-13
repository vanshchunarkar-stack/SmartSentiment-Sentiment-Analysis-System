# Security Policy

## Reporting Security Vulnerabilities

We take security seriously. If you discover a security vulnerability in SmartSentiment, please **do not** open a public issue. Instead:

1. **Email Security Report** – Send details to: [Open an issue and we'll provide contact]
2. **Include Details:**
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if you have one)

3. **Response Timeline:**
   - We aim to acknowledge security reports within 48 hours
   - We'll work with you to verify and fix the issue
   - We'll coordinate disclosure timing

## Security Best Practices

When using SmartSentiment:

### Data Privacy
- Never commit sensitive data (API keys, tokens) to the repository
- Use environment variables for sensitive configuration
- Sanitize user input before processing

### Dependencies
- Keep dependencies updated to latest stable versions
- Review `requirements.txt` for known vulnerabilities
- Use virtual environments to isolate dependencies

### Model Files
- Keep trained models in `.gitignore`
- Don't share model files publicly if trained on sensitive data
- Use appropriate file permissions on model artifacts

## Supported Versions

| Version | Status | Support Until |
|---------|--------|---|
| Latest | ✅ Supported | Active development |
| Previous | ⚠️ Limited | Security fixes only |
| Older | ❌ Unsupported | No updates |

## Known Issues

Currently tracking:
- None known at this time

## Security Checklist

- [ ] No hardcoded secrets in code
- [ ] Input validation implemented
- [ ] Dependencies are up-to-date
- [ ] Virtual environment used for development
- [ ] `.gitignore` configured properly

## Additional Resources

- [OWASP Top 10 for Python](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [GitHub Security Features](https://docs.github.com/en/code-security)

## Acknowledgments

We appreciate the security research community's help in keeping SmartSentiment secure.
