# Android Trusted Web Activity - Release & Security Governance
> Generic checklist derived from a supplied Android wrapper. The hosted web application and its business functions are not included in the archive and remain UNKNOWN.

## Architectural scope
A TWA launches a hosted web application in a browser-backed activity. The Android shell contains the package, launcher, icon, splash, domain relationship, App Links, permissions and Gradle build configuration. The web site supplies its own business behavior.

## Observed Android shell elements
The manifest declares INTERNET, ACCESS_COARSE_LOCATION and ACCESS_FINE_LOCATION permissions, a launcher Trusted Web Activity, HTTPS app link, FileProvider and service delegation. Declared permissions do not prove actual collection, actual granted access or any feature.

## Domain & signing verification
Document package name, target domain, asset links statement, release certificate SHA-256 fingerprint, valid origin association and behavior when verification fails. Use fictional example hostnames in public templates.

## Build and distribution
Capture Gradle/Android versions, min/target SDK, version code, signed AAB/APK provenance, reproducibility steps, PlayProtect outcome, installation and upgrade path. Source code alone is not an installable binary.

## Permissions and minimization
For every declared permission record legal/functional need, platform rationale, runtime permission request behavior, denial fallback and responsible owner. Location permissions must be justified by a verifiable use case; consider removal if unused. Review Android backup and FileProvider paths.

## Test journeys
HTTPS access, offline/degraded connection, deep-link matching, Android back/navigation, browser fallback, permission granted/denied/revoked, file-sharing flow, screen orientation, cold start, resume, upgrade and clean install.

## Security and privacy
Review web TLS, authentication, redirect allowlist, CSP, cookies, local storage, logs and data retention. These require inspection of hosted web code and backend, not merely the Android manifest.

## Handover
Include source inventory, build configuration, signing custody, release notes, support, domain control, incident fallback and store publication artifacts. Protect keystores and secrets.

## Gaps
Functional requirements of the hosted web app, live services, location usage, backend endpoints, logging behavior, production telemetry and accessibility cannot be established from the supplied ZIP. Keep these entries as TO VALIDATE until inspected.

## Acceptance
No release approval without tested web origin, valid asset links, documented permissions, signed package, device tests and assigned run owner.