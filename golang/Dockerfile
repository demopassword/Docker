#single stage
FROM golang:alpine
WORKDIR /app
COPY main.go .
RUN apk add --no-cache curl && go mod init noah.io/ark/rest && go build main.go
# CMD ["./main"]


# multistage build
# FROM golang:alpine AS builder
# ENV GO111MODULE=on \
#     CGO_ENABLED=0 \
#     GOOS=linux \
#     GOARCH=amd64

# WORKDIR /build
# COPY go.mod go.sum main.go ./
# RUN go mod download
# RUN go build -o main .
# WORKDIR /dist
# RUN cp /build/main .

# FROM scratch
# COPY --from=builder /dist/main .
# ENTRYPOINT ["/main"]