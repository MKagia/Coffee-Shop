## Coffee Shop Domain Modeling

## Overview

This project models a Coffee Shop domain using object-oriented programming in Python. It includes three main entities — `Customer`, `Coffee`, and `Order` — and captures their relationships and behaviors. It serves as an educational exercise to practice Python class design, relationships, validation, and aggregation.

## Domain Model

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

This creates a many-to-many relationship between `Customer` and `Coffee` through the `Order` class.
