from fastapi.security import OAuth2PasswordBearer

"""
Esta dependencia únicamente extrae el JWT del header:

Authorization: Bearer <JWT>

Devuelve únicamente:

eyJhbGc...

No valida la firma.
No consulta la base de datos.
No sabe quién es el usuario.

Solo extrae el token.
"""

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

"""
Luego otra dependencia (get_current_user)
utilizará ese JWT para:

1. Verificar la firma.
2. Verificar expiración.
3. Extraer el "sub".
4. Buscar el usuario en PostgreSQL.
"""