# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in FileZipper, we appreciate your help in disclosing it to us in a responsible manner.

### How to Report

Please report security vulnerabilities by email to: [pranav.singh01010101@gmail.com](mailto:pranav.singh01010101@gmail.com)

Include the following information in your report:
- Description of the vulnerability
- Steps to reproduce
- Impact of the vulnerability
- Any mitigation or workarounds if known

### Our Commitment

- We will acknowledge receipt of your report within 48 hours
- We will keep you informed about the progress towards fixing the vulnerability
- We will credit you in our security advisories if you're the first to report the issue (unless you prefer to remain anonymous)

### Security Best Practices

When using FileZipper, please follow these security best practices:

1. **Keep Dependencies Updated**: Regularly update all dependencies to their latest secure versions.
2. **Input Validation**: Always validate and sanitize input data before processing.
3. **Secure Configuration**: Use secure configurations and avoid hardcoding sensitive information.
4. **Access Control**: Implement proper access controls when integrating FileZipper into your applications.
5. **Monitoring**: Monitor for unusual activities or performance issues that might indicate a security incident.

### Known Security Considerations

- FileZipper processes files in memory. Be cautious when processing very large files from untrusted sources.
- The compression format does not include encryption. For sensitive data, consider encrypting files before compression.

### Security Updates

Security updates will be released as patch versions following the [Semantic Versioning](https://semver.org/) specification. It is recommended to always use the latest version of FileZipper to ensure you have all security fixes.
