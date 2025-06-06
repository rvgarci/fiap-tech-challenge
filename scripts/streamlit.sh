#!/bin/bash
case "$1" in
    start)
        ./scripts/streamlit_start.sh
        ;;
    stop)
        ./scripts/streamlit_stop.sh
        ;;
    *)
        echo "Uso: $0 {start|stop}"
        exit 1
        ;;
esac
