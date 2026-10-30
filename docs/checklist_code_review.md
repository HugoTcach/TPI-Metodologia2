# Code Review - Refactoring TPI

**Revisores:** Farid Salomon, Gonzalo Vega
**Autores:** Mateo Serafini, Hugo Tcach

* [x] **Nomenclatura:** Nombres de variables, clases y métodos revelan intención.
* [x] **SRP:** Las responsabilidades se dividieron en capas (Servicio, Repositorio, Interfaz).
* [x] **DIP:** La lógica de negocio depende de abstracciones para la persistencia.
* [x] **Manejo de Errores:** Se utilizan excepciones personalizadas (`EstadoInvalidoError`).
* [x] **Duplicación:** Se eliminó el "Shotgun Surgery" centralizando el acceso a datos.

**Observaciones:** Se sugirió y aplicó el cambio a excepciones personalizadas en `cambiar_estado` para evitar el retorno de strings genéricos a la consola, facilitando la gestión de errores en la interfaz.