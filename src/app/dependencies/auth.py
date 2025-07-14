# src/app/dependencies/auth.py

import os
from functools import lru_cache

from fastapi import Header, HTTPException, status


@lru_cache()
def get_expected_token():
    token = os.getenv("ADMIN_TOKEN")
    if not token:
        raise HTTPException(
            status_code=500,
            detail="Token de administrador não configurado no servidor.",
        )
    return token


def get_admin_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido. Use: Bearer <token>",
        )

    token = authorization.split(" ")[1]
    expected_token = get_expected_token()

    if token != expected_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token inválido ou não autorizado.",
        )
