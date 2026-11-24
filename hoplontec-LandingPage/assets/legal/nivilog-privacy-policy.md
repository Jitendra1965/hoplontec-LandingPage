# NiviLog Privacy Policy

Version 2026-11-24.3 · Updated November 24, 2026

**Pre-release draft. NiviLog is coming soon. This document describes the current development version.**

## Who is responsible

Hoplontec Inc ("Hoplontec", "we", "us") publishes NiviLog, a personal food and wellbeing journal for adults aged 18 and over. Our business is based in Delaware, United States. This policy explains the information handled by the app and by us when you contact us about it. It does not describe all activity on our separate website or on services you choose to use.

**Mail:** 1111B S Governors Ave #87194, Dover, DE 19904, USA

**Privacy enquiries and requests:** [legal@armur.org](mailto:legal@armur.org)

**Website:** [hoplontec.io](https://hoplontec.io)

**Public copy of this policy:** [NiviLog Privacy Policy](https://hoplontec.io/nivilog-privacy.html)

## Your choices before you start

You must acknowledge this policy and agree to the separate Terms of Use before entering the journal. Acknowledging the policy does not give blanket permission to use your information. We separately ask for your explicit consent to process health-related information for the local journal and nutrition estimates. Without it, these features cannot operate.

Pattern analysis, Google Sheets sync and voice input are separate choices, initially off. Declining them does not prevent ordinary typed journaling. You can change these choices or withdraw journal consent in **Settings → Privacy & security**. Withdrawal stops the relevant features; it does not automatically erase records or affect the lawfulness of earlier processing. Requests already delivered to a provider cannot be recalled.

You may decline the Terms or journal consent and still use the authenticated controls to export or erase existing local records. These controls are also available through **Manage existing local data** on the welcome screen, without making a new age declaration.

## Information the app handles

NiviLog handles the following information when you provide it or enable the corresponding feature:

- **Journal information:** foods, portions, meal times, notes, symptoms, mood, energy, goals and other details you enter, including drafts and edited versions. Nutrition totals and, if enabled, associations between records are derived from this information. These records and inferences can reveal health information.
- **Photos and text:** images you select or capture for meal suggestions, the resulting suggestions, and text you type or dictate. Images can incidentally contain other people or identifying details; select only what you intend to process.
- **Google connection information:** the account identifier and email used for your connection, authorization managed by Google's sign-in software, spreadsheet identifiers, and cached entries and revision history downloaded from your Sheet. NiviLog does not ask for your Google password.
- **Choices and device information:** your adult declaration and its time, privacy choices, document versions and acceptance times, appearance/accessibility preferences, and the result of a device authentication request. NiviLog receives no fingerprint, face template or device passcode from the authentication prompt. We do not ask for your birth date or identity document during onboarding.
- **Messages you send to Hoplontec:** your contact details and the information you choose to include in your message. Health information is not needed to make a support or privacy enquiry.

Information comes from you, your device, your connected Google Sheet and calculations performed by the app. The food catalogue supplies reference estimates; it does not supply personal information about you.

## How information is used

**Local journal and estimates.** NiviLog stores and displays your entries, saves drafts and revisions, and estimates nutrition using its offline food catalogue and the portions you confirm. Supported photo and text suggestions run on the device. The app does not send journal text or photos to OpenAI or another hosted AI inference service. A model or platform component may need an initial download; the download provider can receive ordinary network information such as an IP address.

**Optional patterns.** With your separate consent, the app compares your entries with symptoms, mood and energy locally. These associations are uncertain. They do not diagnose allergies, predict a safe amount of food, or establish that a food caused a symptom. NiviLog does not use them to make decisions with legal or similarly significant effects about you.

**Optional Google Sheets sync.** With your consent and Google authorization, the app reads and writes saved entries, nutrition, check-ins and revision history in your Google account, in the NiviLog folder and Sheet it creates or connects to. Drafts and nutrition goals remain local. Your Sheet contains readable data: the app's local encryption does not encrypt the Sheet's contents. People or services with access through your Google sharing settings may be able to read them. Google's terms, privacy practices, retention and account controls also apply. See [Google's Privacy Policy](https://policies.google.com/privacy).

**Optional voice.** With your consent and device permission, the operating system's speech service turns speech into text. Depending on your device, language and settings, that provider may receive audio and process it online. The app uses the resulting text and does not maintain its own audio archive. Typing remains available. See your [Apple privacy controls](https://www.apple.com/legal/privacy/) or [Google privacy controls](https://policies.google.com/privacy), as applicable.

**Security and privacy controls.** The app authenticates access, encrypts local private files, records privacy choices, and carries out export, deletion and migration. These controls operate without giving Hoplontec access to your journal.

## Who receives information

This version has no Hoplontec journal server, advertising SDK or analytics SDK. Journal contents are not automatically transmitted to Hoplontec. We do not sell health information, share it for targeted advertising, or upload it for AI model training. No journal information is sent to advertisers or data brokers by the app.

Information can leave your device when you enable Google sync, use a speech service that processes online, follow an external link, or export/share records. Recipients include Google for your connected account, the speech provider on your device, and recipients you select. Device and app-store providers may separately handle downloads, network traffic and diagnostics according to their own settings and policies. Their activities are not all controlled by NiviLog.

**Hoplontec cannot access your journal or connected Google Sheet through NiviLog. Your journal is not stored on Hoplontec’s servers.**

If you contact Hoplontec, we receive the information you choose to include in your message and use it to respond to your enquiry. Please do not send health details, journal exports, or screenshots containing personal health information.

## Storage, retention and security

Local journals, Google account caches, nutrition goals and the privacy/acceptance history use application-level encryption. The key is protected by the device's secure storage. Age-confirmation metadata and appearance preferences are ordinary local settings. Device authentication controls access; anyone able to satisfy your device's authentication may be able to open your journal.

The app requests platform protections against backup and background exposure. These depend on the device and operating system. Decrypted information can remain in the running app's memory. Encryption cannot protect a readable export, a shared Sheet, all screenshots, or a compromised device, and no system guarantees complete security.

Local records remain until you remove them. Editing or deleting a synced entry can retain earlier revisions in the local account history and in the Sheet. Removing an entry from the visible journal is therefore not complete historical erasure. **Erase all local data** removes this installation's owned journal files, account caches, goals, privacy/acceptance history, age confirmation and encryption key. Appearance preferences remain. Destroying the key or losing secure storage can make unsynced records unrecoverable; Hoplontec cannot recover the key for you.

Local erasure does not delete Google files, revoke Google access, remove copies on other devices, or recall exports. Delete cloud copies in Google Drive, review shared copies and Google account access, and erase other installations separately. Reconnecting to a retained Sheet can download its records again. Provider backups, trash and revision retention remain subject to that provider's controls.

Photos are not stored as journal attachments. Original photos may remain in your library or operating-system picker caches. Exports are readable JSON files. The app attempts to clear its temporary export/share files at the next app start, before another export and during local erasure; failed cleanup can leave a temporary file until cleanup succeeds. Copies saved by you or another app remain outside these controls.

For communications you send us, retention depends on completing the request, resolving any related dispute and applicable legal retention duties. We limit retention to those purposes; you may ask what remains and request deletion. We do not retain a separate publisher copy of your local journal or acceptance record through normal app use.

## Access, correction, deletion and complaints

You can review and correct current journal entries in the app and export existing local records from Privacy & security. Export includes cached revisions, drafts, goals and privacy/acceptance history; it does not fetch records that exist only in the cloud. It requires device authentication and produces an unencrypted copy. Review the retention section before using entry deletion or local erasure.

Contact us at the address above for privacy questions, complaints or requests relating to information we hold. Depending on the law that applies, your rights may include access, correction, deletion, portability, restriction, objection, withdrawing consent and appealing a refused request. We will respond within applicable legal time limits, explain any refusal and available review route, and request only proportionate verification. Do not include journal contents with your enquiry. Exercising privacy rights does not authorize advertising or unrelated processing.

For local-only records, Hoplontec cannot remotely identify, retrieve, change or erase your device's contents. We can explain the device controls; access still depends on your device credentials and encryption key. You may also raise a complaint with the regulator that has jurisdiction, including the [UK Information Commissioner's Office](https://ico.org.uk/make-a-complaint/), the [Office of the Australian Information Commissioner](https://www.oaic.gov.au/privacy/privacy-complaints), or a relevant US state regulator. In India, statutory grievance and complaint routes depend on the law in force for the processing concerned.

## Regional information and international processing

**United States.** The app can handle consumer health information even where HIPAA does not apply. Where state privacy or consumer-health laws apply, their protections and request rights remain available. The categories, sources, purposes and recipients described above also apply to consumer health information. We do not collect precise location or use location-based health-facility targeting. There is no sale of health data to authorize.

**United Kingdom.** Where UK data-protection law applies, we rely on consent for the local journal and optional processing described here, and explicit consent for health data. Limited non-health information may be necessary to administer the app agreement or respond to a request, for legitimate interests in handling support and protecting security where those interests do not override your rights, or to meet a legal obligation. Those grounds do not replace explicit consent for optional health-data use. You can ask about the applicable ground and object to processing based on legitimate interests.

**Australia.** Where Australian privacy law applies, access, correction, sensitive-information consent and complaint rights remain available. Our complaint contact is above; you may escalate an unresolved privacy complaint to the OAIC where it has jurisdiction.

**India.** Applicable Indian privacy requirements remain available. The Digital Personal Data Protection Act and Rules have phased commencement; this policy does not assume that all their provisions are already in force. We will update the notice and request procedures as applicable requirements take effect.

Hoplontec is based in the United States. Local-only journal processing remains on your device. Information you send to Hoplontec is handled in the United States, and optional Google or operating-system services can process information in other countries under their own policies. Choosing sync or speech is not a waiver of mandatory international-transfer protections. Any transfer arranged by Hoplontec must satisfy applicable law; contact us for information about a particular transfer and applicable safeguards.

## Age restrictions and policy changes

NiviLog is intended only for adults aged 18 or over. We ask for an age declaration, not proof of age. If someone under 18 has used the app, ordinary journal use should stop; authenticated export and erasure remain available. Contact us about information sent to Hoplontec concerning a child so we can address it under applicable law.

The app displays the policy version and records your acknowledgement locally. A changed bundled policy or Terms requires renewed review and acceptance before journal use; optional permissions start off again at that point. A new purpose requiring consent will not be enabled simply by publishing an update. You can keep a copy of this policy and the Terms and decline future changes while retaining access to authenticated local export and erasure.
