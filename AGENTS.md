# AGENTS.md - Guía de Contexto y Reglas para Agentes de IA

Este documento define la arquitectura, restricciones de dominio y reglas de desarrollo para este proyecto web en Django.

---

## 1. Alcance y Estructura de Aplicaciones

El sitio es una plataforma web para una marca de belleza y cuidado de la piel (*skincare*), organizada en 4 aplicaciones:

1. **`proyectoyaneapp`:** Páginas informativas principales (Inicio/Home, Quiénes somos, Políticas de privacidad).
2. **`proyectoyaneshop`:** **CATÁLOGO DIGITAL EXCLUSIVO.**
   - **REGLA DE ORO:** Esta app funciona únicamente como escaparate digital. **NO** implementar carrito de compras, **NO** incluir pasarela de pagos, **NO** crear modelos de orden ni gestión de checkout.
   - Responsabilidad: Mostrar productos, categorías, imágenes, descripción, y precio
3. **`proyectoyanecontact`:** Formularios de contacto, ubicación física y botones/enlaces directos de conversión a WhatsApp para consulta de productos.
4. **`proyectoyaneblog`:** Publicación de artículos, consejos de skincare y rutinas de belleza.

---

## 2. Comandos de Entorno y Verificación

Ejecuta estos comandos para validar cualquier cambio antes de dar una tarea por terminada:

- **Servidor de desarrollo:** `python manage.py runserver`
- **Migraciones:**
  - Crear: `python manage.py makemigrations`
  - Aplicar: `python manage.py migrate`
- **Pruebas:** `pytest` (o `python manage.py test`)
- **Linter y Formato:** `ruff check .` / `black .`

---

## 3. Estructura de Código y Arquitectura

Sigue estas convenciones en el desarrollo con Django:

- **Vistas delgadas (Thin Views):** Las vistas en `views.py` solo deben encargarse de recibir la petición, validar con formularios/serializers y responder con la plantilla correspondiente.
- **Consultas a la base de datos:** Para consultas complejas o filtrados avanzados en `proyectoyaneshop`, centraliza la lógica en un archivo `selectors.py` dentro de la app.
- **Optimización de ORM:** Evita el problema de consultas N+1 en el catálogo. Usa siempre `select_related('category')` al listar productos.

---

## 4. Frontend y Estilos (Bootstrap 5)

- **Framework:** Usa **Bootstrap 5** para todo el diseño responsivo (*mobile-first*).
- **Formularios:** Formatea los formularios de Django usando `django-crispy-forms` con la integración `crispy-bootstrap5`.
- **Componentes UI de la tienda:**
  - **Grilla de catálogo:** Usa el sistema de grid de Bootstrap (`row`, `col-12`, `col-md-4`) con tarjetas (`.card` e `h-100`).
  - **Botón de contacto:** En la vista de detalle del producto, incluye un botón directo a WhatsApp con el mensaje predefinido para consultar por ese producto específico.

---

## 5. Reglas Generales de Django

1. **Usuario Personalizado:** Si se hace referencia al modelo de usuario, utiliza siempre `from django.contrib.auth import get_user_model; User = get_user_model()`.
2. **Variables Sensibles:** Nunca expongas credenciales ni llaves API en el código. Lee la configuración mediante variables de entorno (`.env`).
3. **Archivos Estáticos y Media:** Maneja correctamente las imágenes subidas por los usuarios especificando la ruta destino en `ImageField`:
   - En **`proyectoyaneshop`**: usa `upload_to="products/"`.
   - En **`proyectoyaneblog`**: usa `upload_to="blogs/"`.

---

## 6. Protocolo de Trabajo para la IA

1. **Respeta los límites:** No intentes agregar funcionalidades de e-commerce transaccional (pagos/carritos) a menos que se solicite explícitamente.
2. **Revisión de Migraciones:** Si agregas o modificas un modelo en cualquiera de las 4 apps, ejecuta `makemigrations` y confirma que la migración se haya generado limpiamente.
3. **Verificación:** Antes de entregar el código, confirma que no rompe la suite de tests existente.
