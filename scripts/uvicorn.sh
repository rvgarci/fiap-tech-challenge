#!/bin/bash
case "$1" in
    start)
        ./start_uvicorn.sh
        ;;
    stop)
        ./uvicorn_stop.sh
        ;;
    *)
        echo "Uso: $0 {start|stop}"
        exit 1
        ;;
esac
