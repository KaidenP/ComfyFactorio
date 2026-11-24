---
title: Offer
tags: [factorio-api, runtime, concept]
---
# Offer

A single offer on a market entity.

## Fields

### price
- **Type:** array<[[MarketIngredient]]>
- **Optional**
List of prices.

### offer
- **Type:** [[TechnologyModifier]]
The action that will take place when a player accepts the offer. Usually a `"give-item"` modifier.
