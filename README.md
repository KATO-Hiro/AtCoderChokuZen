# AtCoderChokuZen

[![Build Status](https://travis-ci.com/KATO-Hiro/AtCoderChokuZen.svg?branch=master)](https://travis-ci.com/github/KATO-Hiro/AtCoderChokuZen)
[![codecov](https://codecov.io/gh/KATO-Hiro/AtCoderChokuZen/branch/master/graph/badge.svg)](https://codecov.io/gh/KATO-Hiro/AtCoderChokuZen)
[![Issues](https://img.shields.io/github/issues/KATO-Hiro/AtCoderChokuZen)](https://github.com/KATO-Hiro/AtCoderChokuZen/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/KATO-Hiro/AtCoderChokuZen.svg)](https://github.com/KATO-Hiro/AtCoderChokuZen/pulls)
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/KATO-Hiro/AtCoderChokuZen/blob/master/LICENSE)

## Description

A twitter bot that notifies you just before [AtCoder](https://atcoder.jp/) contest (The messages can be forwarded push-notification via [Discord](https://discord.com/)). The purpose is to reduce the number of times you forget to join contests. The bot was inspired by [tweets](https://twitter.com/chokudai/status/1267051182154936321).

***DEMO***

| Twitter | Discord |
|:-------------------------:|:-------------------------:|
|![Sample tweet](images/sample_tweet.png)|![Sample channel](images/sample_discord_chat.png)|

## Features

- Notify you to participate at regular intervals when the day of the contest comes.

- Contest information will be delivered to your smartphone via push notifications using [Discord](https://discord.com/)).

## Usage

### View from Twitter timeline

- Just click on the follow button on [Twitter](https://twitter.com/AtCoderChokuZen).

### Push notifications to your smartphone

- Install Discord app from [Apple Store](https://apps.apple.com/us/app/discord/id985746746) or [Google Play](https://play.google.com/store/apps/details?id=com.discord&hl=en).

- Access the [invite link](https://discord.gg/6feQqG5).

- Input your email and password if needs.

- Settings for Notifications in Discord.
  1. Tap "AtCoder ChokuZen Bot" […]

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![discord_en](images/discord_en.png)|![discord_jp](images/discord_jp.png)|

  2. Tap "Notifications"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![discord_notifications_en](images/discord_notifications_en.png)|![discord_notifications_jp](images/discord_notifications_jp.png)|

  3. SERVER NOTIFICATION SETTINGS
    - Select "Only @mentions"
    - Turn on "Mobile Push Notifications"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![discord_notification_settings_en](images/discord_notification_settings_en.png)|![discord_notification_settings_jp](images/discord_notification_settings_jp.png)|

- Settings for Notifications in your smartphone (iOS sample).
  1. Tap "Settings"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![iphone_settings_en](images/iphone_settings_en.png)|![iphone_settings_jp](images/iphone_settings_jp.png)|

  2. Tap "Notifications"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![iphone_notifications_en](images/iphone_notifications_en.png)|![iphone_notifications_jp](images/iphone_notifications_jp.png)|

  3. Tap "Discord"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![iphone_discord_en](images/iphone_discord_en.png)|![iphone_discord_jp](images/iphone_discord_jp.png)|

  4. Turn on "Allow Notifications"

  | English | 日本語 |
  |:-------------------------:|:-------------------------:|
  |![iphone_discord_settings_en](images/iphone_discord_settings_en.png)|![iphone_discord_settings_jp](images/iphone_discord_settings_jp.png)|

## Frequently Asked Questions (よくある質問)

### Push notifications not working

Recheck the following steps:

- Recheck settings for "Notification" on your smartphone and Discord (See: Usage).
- Restart Discord app.
- Restart your smartphone.
- Reinstall Discord app.

### プッシュ通知が届かない

以下の項目を順に確認・実行すると、通知される可能性が高くなると思います。

- スマートフォン本体およびDiscordの通知の設定を再度確認する（設定の例は、使い方を参照してください）
- Discord appを再起動する
- スマートフォンを再起動する
- Discord appを再インストールする

### See

> https://support.discord.com/hc/en-us/articles/218892547--Mobile-Notifications-Settings-101

> https://aprico-media.com/posts/4798

> https://aprico-media.com/posts/4799

> https://kazu22002.hatenablog.com/entry/2015/09/24/070000

## How to clone the repository

Paste the following commands at a Terminal prompt.

```terminal
$ mkdir hoge
$ cd hoge
$ git clone git@github.com:KATO-Hiro/AtCoderChokuZen.git
```

### Set up Twitter API in local env

1. Sign into your Twitter account, and apply for [a developer account](https://developer.twitter.com/).

2. After being approved, click "Create an app", and input App info. Next, click "Key and tokens" tab and "Create" button, you can get "Consumer API Keys" and "Access token info".

Note: The above keys give access to your Twitter account. Keep it confidential and never store them in this repository.

3. Create .env files or copy .env.sample as .env.

```terminal
$ touch .env
```

Open your editor, filling in your Twitter keys like below. XXXXX means your "Consumer API Keys" or "Access token info".

```
CONSUMER_KEY=XXXXX
CONSUMER_SECRET=XXXXX
ACCESS_TOKEN=XXXXX
ACCESS_SECRET=XXXXX
```

Note that .env file is in the project's .gitignore, so it won't be checked into this repository.

#### See

> https://qiita.com/kngsym2018/items/2524d21455aac111cdee

> https://qiita.com/hedgehoCrow/items/2fd56ebea463e7fc0f5b

### Debug in your local env

Paste the following commands at a Terminal prompt in your cloned directory.

```terminal
# Setup container
$ docker-compose build

# Run container
$ docker-compose up -d

# Stop container
$ docker-compose stop

# Run a command
$ docker-compose run --rm web hogehoge
```

## Requirement

- Docker Desktop 19+
- Python 3.8.x
- pip

### Test framework and CI

- [Pytest](https://docs.pytest.org/en/stable/)
- [Travis CI](https://travis-ci.com/)

### Hosting

- Heroku

### Optional

- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/containers)

## Links

[AtCoder](https://atcoder.jp/)

[Original tweet](https://twitter.com/chokudai/status/1267051182154936321)

[Readme Driven Development; RDD](https://qiita.com/b4b4r07/items/c80d53db9a0fd59086ec)

## Author

[@KATO-Hiro](https://twitter.com/k_hiro1818)

## License

[MIT](http://KATO-Hiro.mit-license.org)
