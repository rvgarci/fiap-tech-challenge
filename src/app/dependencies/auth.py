# src/app/dependencies/auth.py

import os

from fastapi import Header, HTTPException, status


def get_admin_token(authorization: str = Header(...)):
    expected_token = os.getenv("ADMIN_TOKEN")

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de token inválido. Use: Bearer <token>",
        )

    token = authorization.split(" ")[1]

    if token != expected_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token inválido ou não autorizado.",
        )
