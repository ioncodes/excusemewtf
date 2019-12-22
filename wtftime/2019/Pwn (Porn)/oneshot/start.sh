#!/bin/bash

socat TCP-LISTEN:9054,reuseaddr,fork,su=chall EXEC:"./oneshot",stderr
