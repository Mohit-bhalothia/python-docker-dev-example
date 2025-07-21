FROM ruby:3.1-alpine

RUN apk add --no-cache curl build-base
RUN gem install sinatra rackup puma

WORKDIR /app
COPY . .

EXPOSE 4567
CMD ["ruby", "app.rb"]
