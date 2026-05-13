# Messenger Integration Evaluation

**Project:** Mission Vault CLI  
**Date:** May 2026  
**Status:** Decision Made — Dual-Platform Strategy Adopted

---

## Summary

Mission Vault needs to expand from a local CLI tool into multi-channel access so users can add and view missions via WhatsApp and web messenger. Three platforms were evaluated. The outcome is a **dual-platform strategy**: 360dialog handles the WhatsApp AI agent, and iboss handles the structured web/messenger chatbot.

---

## Platforms Evaluated

### 1. 360dialog — Selected for WhatsApp AI Agent

**What it is:** A WhatsApp Business API provider that ships a native AI agent integration directly connected to Google Gemini.

| Attribute | Detail |
|-----------|--------|
| Role | WhatsApp AI agent (conversational) |
| AI Backend | Google Gemini (direct integration) |
| Price — Standard | £200/month (API call limits apply) |
| Price — Unlimited | £500/month |
| Gemini Pro tier | Generous limits, usage-based beyond free tier |

**Strengths:**
- Already live and tested — lowest friction for the upcoming demo
- AI-native: users talk naturally, Gemini interprets intent
- Gemini Pro provides strong performance at reasonable cost
- Good value at £200/mo for most usage levels

**Weaknesses:**
- API call limits on the £200 tier (exact cap to be confirmed with 360dialog)
- Single AI provider dependency (Gemini only)
- Upgrade to £500/mo is a significant cost jump if limits are hit

**Verdict:** ✅ Selected for WhatsApp channel. Best fit for AI-driven conversational access to Mission Vault.

---

### 2. iboss — Selected for Messenger/Chatbot Channel

**What it is:** An Egyptian-based messaging and chatbot platform with a proprietary API, a visual flowchart builder, and structured chatbot capabilities.

| Attribute | Detail |
|-----------|--------|
| Role | Structured chatbot / messenger channel |
| AI | Rule-based (flowchart-driven, not generative AI) |
| Provider base | Egypt — local support advantage |
| API | Own API (documentation to be confirmed) |

**Strengths:**
- Strong flowchart/chatbot builder — good for guided, menu-driven interactions
- Local Egyptian provider: accessible support, understands local market
- Own API means direct integration without third-party dependencies
- Chatbot is reliable and predictable for structured flows

**Weaknesses:**
- Not AI-native — responses are rule-based, not conversational
- Requires manual flow design and maintenance
- Pricing not yet confirmed

**Verdict:** ✅ Selected for web/messenger channel. Best fit for structured guided flows (e.g. "Add a mission", "View vault", category selection).

---

### 3. Twilio / "Tie" — Deferred

**What it is:** A third platform with some WhatsApp capability. Subscription model and exact feature set are unclear.

| Attribute | Detail |
|-----------|--------|
| WhatsApp support | Present, details unclear |
| Pricing | Unknown — meeting needed |
| Status | Deferred pending discovery call |

**Verdict:** ⏸ Deferred. A meeting should be booked to understand the subscription tiers and WhatsApp offering before any further evaluation.

---

## Recommended Architecture

The two selected platforms serve different user journeys and complement each other:

```
WhatsApp User
    └── Message → 360dialog → Gemini AI Agent
                                  └── Parse intent (add/view mission)
                                        └── Mission Vault API / vault_data.json

Web/Messenger User
    └── Message → iboss Chatbot (flowchart)
                      └── Structured menu → "Add Mission" / "View Vault"
                            └── Mission Vault API / vault_data.json
```

Both channels share the same underlying data store (`vault_data.json`) via a shared Mission Vault API layer (to be built).

---

## Cost Analysis

| Platform | Monthly Cost | Notes |
|----------|-------------|-------|
| 360dialog | £200 | Monitor API limits; upgrade to £500 if exceeded |
| iboss | TBD | Confirm pricing |
| Gemini Pro | Usage-based | Generous free tier; cost scales with volume |
| **Total (est.)** | **£200+ / mo** | Pending iboss pricing |

---

## Demo Scope (Immediate)

For the upcoming demo the focus is on **360dialog + Gemini** (WhatsApp AI agent) since it is already live. iboss integration will be demonstrated via flowchart design or a separate follow-up demo.

---

## Next Steps

- [ ] Confirm iboss pricing and obtain API documentation
- [ ] Confirm 360dialog API call limits on the £200/mo tier
- [ ] Build Mission Vault webhook endpoint to receive 360dialog events
- [ ] Design iboss chatbot flows: Add Mission, View Vault, Category Selection
- [ ] Book discovery call with Twilio/"Tie" for Phase 2 evaluation
- [ ] Demo to stakeholder: WhatsApp AI agent via 360dialog + Gemini
- [ ] Post-demo: decide on upgrade path based on API usage observed
