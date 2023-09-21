FROM alpine
WORKDIR /app
COPY match .
RUN apk add --no-cache curl && apk add --no-cache gcompat
RUN adduser --disabled-password --gecos '' match && \
    chown -R match: /app && chmod +x match
USER match
EXPOSE 8080