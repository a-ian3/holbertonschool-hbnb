# 📘 Documentation Technique - HBnB Evolution

## 1. Introduction

Ce document technique a pour objectif de définir l'architecture logicielle, les entités métiers, et les interactions principales de l'application **HBnB Evolution**, une version simplifiée d'un système de réservation de logements similaire à AirBnB.

Cette documentation servira de référence principale pour la phase de développement, en assurant une compréhension partagée du fonctionnement de l’application.

---

## 2. Architecture Haut Niveau

L’application est basée sur une **architecture en couches (3-tier architecture)**, qui permet une meilleure séparation des responsabilités.

### 2.1 Diagramme de packages UML

```mermaid
classDiagram
class PresentationLayer {
    <<Package>>
    +UserService
    +PlaceService
    +ReviewService
    +AmenityService
}
class BusinessLogicLayer {
    <<Package>>
    +User
    +Place
    +Review
    +Amenity
    +HBnBFacade
}
class PersistenceLayer {
    <<Package>>
    +UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
}
PresentationLayer --> BusinessLogicLayer : via HBnBFacade
BusinessLogicLayer --> PersistenceLayer : accède aux Repositories


