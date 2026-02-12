# Jarvis: Sistema Distribuido de Inteligencia Personal Autónoma

Jarvis no es un chatbot. Es un sistema distribuido de inteligencia personal autónoma con control administrador total, memoria persistente extrema, sincronización multi-dispositivo y proactividad inteligente.

## 🏗️ Arquitectura Global

```
                ┌──────────────────────────┐
                │        Backend Core       │
                │  (Cerebro + Memoria)      │
                └────────────┬──────────────┘
                             │
         ┌───────────────────┴───────────────────┐
         │                                       │
 ┌───────────────┐                      ┌───────────────┐
 │   PC Agent     │                      │  Mobile Agent  │
 │ (Admin Layer)  │                      │ (iOS App)      │
 └───────────────┘                      └───────────────┘
```

## 🧠 Características Principales

* **Sistema Distribuido**: Multi-dispositivo (PC + móvil) con backend central seguro.
* **Control Administrador Total**: Agentes locales con privilegios elevados.
* **Proactividad Inteligente**: Detección de conflictos y recordatorios autónomos.
* **Memoria Cognitiva Persistente**: Híbrido PostgreSQL + Vector DB.
* **Activación por Voz**: Wake-word Engine ("Jarvis").
* **Wake-on-LAN**: Encendido remoto desde el móvil.
* **Streaming Bidireccional**: WebRTC cifrado para screenshots y streaming en vivo.
* **Seguridad Estricta**: Modo Paranoico, Kill Switch global y Autodefensa ante intrusión.

## 📁 Estructura del Repositorio

- `/backend`: Core del sistema (FastAPI + PostgreSQL + Vector DB).
- `/pc-agent`: Servicio de sistema para control administrativo (Windows/Mac).
- `/mobile-agent`: Aplicación móvil (Flutter).
- `/shared`: Tokens de diseño, esquemas de UI y protocolos.

## 🛡️ Seguridad

- TLS obligatorio y Firma digital de comandos.
- Autenticación 2FA y Device pairing único.
- **Modo Paranoico**: Doble confirmación visual para acciones críticas.
- **Auditoría Permanente**: Registro de cada acción con capturas y video.

---
*Jarvis: Elegante, formal y protector.*
