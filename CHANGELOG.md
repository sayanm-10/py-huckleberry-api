# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- towncrier release notes start -->

## [0.2.1] - 2026-03-08

### Bugfixes

- Allow empty Firebase `prefs.last*` summary maps to validate after a child's sleep, feeding, or diaper history has been cleared. ([#deleted-last-summary-payloads](https://github.com/Woyken/py-huckleberry-api/issues/deleted-last-summary-payloads))


## [0.2.0] - 2026-03-07

### Features

- Added `HuckleberryAPI.log_potty()` for potty events stored in the shared diaper tracker; potty changes are observed through the existing diaper listener. ([#potty-api](https://github.com/Woyken/py-huckleberry-api/issues/potty-api))
- Migrate the client to strict Firebase schema models, require an injected `aiohttp` websession, and remove the separate solids interval API path.
