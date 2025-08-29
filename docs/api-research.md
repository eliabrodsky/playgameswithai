# API Research

This document surveys identity, address, phone, and Medicaid eligibility APIs. Only synthetic or tokenized data should be used unless the vendor offers a Business Associate Agreement (BAA) for HIPAA compliance.

| API | Provider | Capabilities | Auth | Pricing | BAA/HIPAA | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| ID.me | ID.me | Identity verification, document upload, selfie match | OAuth 2.0 | Pay-as-you-go | BAA available for government/healthcare clients | Suitable for PHI with BAA. |
| LexisNexis InstantID | LexisNexis Risk Solutions | KYC, SSN/ID validation | API key | Enterprise | BAA via contract | Handles full identity verification; requires BAA. |
| Socure | Socure | Digital identity verification, fraud detection | API key + OAuth | Tiered | BAA upon request | Strong KYC; PHI allowed with agreement. |
| IRS TIN Matching | IRS | SSN/TIN validation for payers | Certificate login | Free | No BAA; limited use | Only last4 or encrypted data recommended. |
| USPS Address Validation | USPS | Address standardization and validation | API key | Free tier | No BAA | Use with non-PHI or tokenized addresses. |
| Twilio Lookup | Twilio | Phone number validation, carrier/type info | API key | $0.005 per lookup | BAA available | Safe for phone data with BAA. |
| Change Healthcare Eligibility | Change Healthcare | X12 270/271 Medicaid & insurance eligibility | OAuth 2.0 | Paid | BAA supported | Supports Medicaid; full PHI allowed. |
| Eligible API | Eligible.com | Insurance eligibility & verification | API key | Paid | BAA supported | Medicaid support; requires contract. |

## Recommendation Matrix

| API | Suitability (1-5) | Pros | Cons | Risk |
| --- | --- | --- | --- | --- |
| ID.me | 4 | Widely accepted, BAA | Requires user interaction | Medium |
| LexisNexis InstantID | 4 | Comprehensive data | High cost | Medium |
| Socure | 4 | Developer-friendly, risk scoring | Contract required | Medium |
| USPS Address | 3 | Free, simple | Not BAA | Low (use tokenized) |
| Twilio Lookup | 4 | Easy integration | Cost per lookup | Low |
| Change Healthcare | 5 | Direct eligibility check | Complex onboarding | Medium |
| Eligible API | 4 | Supports Medicaid | Paid account | Medium |

Short term: mock eligibility signals.  Medium term: integrate with Change Healthcare or Eligible with BAA.  Long term: full KYC and audit via ID.me or Socure.
